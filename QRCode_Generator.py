print("Starting Script")
import qrcode
print("imported qrcode")
import pandas as pd
print("Imported pandas")
from google.oauth2 import service_account
print("Imported google.oauth")
from googleapiclient.discovery import build
print("Imported googleapiclient")
from io import BytesIO
print("Imported io")
from openpyxl import Workbook
print("Imported openpyxl")
from openpyxl.drawing.image import Image
print("Imported drawing")

# Google Sheets API Setup
SERVICE_ACCOUNT_FILE = 'halloween-party-438713-87c01c552e70.json'  # Path to JSON key file
SPREADSHEET_ID = '1qLVC2bo7JFmswxOXqM54fvG7emDIvKxFxUOzxvekohg'  # Google Sheet ID
RANGE_NAME = 'Form Responses 1!B:D'  # Range to read data (modify as needed)

# Set up credentials and service
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# Function to fetch data from Google Sheets
def get_sheet_data():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    
    # Convert to DataFrame and print columns
    df = pd.DataFrame(values[1:], columns=values[0])  # Skip the header row for column names
    print("Columns in Google Sheet:", df.columns)  # Print the column names
    return df

# Function to generate a new Excel file with QR codes
def generate_qr_excel(data):
    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendees with QR Codes"
    
    # Define headers
    headers = ["Name", "Email", "Number of People", "QR Code"]
    ws.append(headers)
    
    # Process each attendee
    for _, row in data.iterrows():
        attendee_name = row["What's your name?"]
        email = row["Email Address"]
        num_people_text = row["How many people are you bringing? "]

        # Parse number of people from text and add 1 for the attendee themselves
        try:
            num_people = int(num_people_text[0]) + 1 if isinstance(num_people_text, str) else 1
        except (ValueError, IndexError):
            num_people = 1

        # Generate URL for the QR code
        url = f"http://localhost:8000/welcome.html?name={attendee_name.replace(' ', '%20')}&attendees=No. of Pax: {num_people}"
        
        # Generate QR code
        qr = qrcode.make(url)
        qr_image = BytesIO()
        qr.save(qr_image, format="PNG")
        qr_image.seek(0)
        
        # Insert data into the sheet
        ws.append([attendee_name, email, num_people])
        
        # Insert QR code image into the next row in the "QR Code" column
        img = Image(qr_image)
        img.width, img.height = 100, 100  # Resize as needed
        ws.add_image(img, f"D{ws.max_row}")

    # Save the workbook locally
    wb.save("attendees_with_qr_codes.xlsx")
    print("Excel file with QR codes saved as 'attendees_with_qr_codes.xlsx'")

# Fetch data from Google Sheets, generate QR codes, and save locally
sheet_data = get_sheet_data()
generate_qr_excel(sheet_data)