import qrcode
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from io import BytesIO
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from urllib.parse import quote_plus
from pathlib import Path

# Configuration
SERVICE_ACCOUNT_FILE = 'credentials/service_account.json'
SPREADSHEET_ID = 'your_spreadsheet_id_here'
RANGE_NAME = 'Form Responses 1!B:D'
QR_BASE_URL = 'http://localhost:8000/welcome.html'
OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = OUTPUT_DIR / f"attendees_with_qr_codes_{timestamp}.xlsx"

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# Fetch data from Google Sheets
def get_sheet_data():
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    df = pd.DataFrame(values[1:], columns=values[0])  # Skip the header row
    print(f"Columns in Google Sheet: {df.columns.tolist()}")
    return df

# Generate Excel file with QR codes
def generate_qr_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendees with QR Codes"
    headers = ["Name", "Email", "Number of People", "QR Code"]
    ws.append(headers)

    for _, row in data.iterrows():
        try:
            attendee_name = row["What's your name?"]
            email = row["Email Address"]
            num_people_text = row["How many people are you bringing? "]
            num_people = int(num_people_text[0]) + 1 if isinstance(num_people_text, str) else 1
        except Exception as e:
            print(f"Error processing row: {row}, Error: {e}")
            continue

        url = f"{QR_BASE_URL}?name={quote_plus(attendee_name)}&attendees=No. of Pax: {num_people}"
        try:
            qr = qrcode.make(url)
            qr_image = BytesIO()
            qr.save(qr_image, format="PNG")
            qr_image.seek(0)
            ws.append([attendee_name, email, num_people])
            img = Image(qr_image)
            img.width, img.height = 100, 100
            ws.add_image(img, f"D{ws.max_row}")
        except Exception as e:
            print(f"Failed to generate QR for {attendee_name}: {e}")

    wb.save(OUTPUT_FILE)
    print(f"Excel file with QR codes saved as '{OUTPUT_FILE}'")

# Execute the process
sheet_data = get_sheet_data()
generate_qr_excel(sheet_data)
