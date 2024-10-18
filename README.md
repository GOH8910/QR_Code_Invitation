A Python-based project that generates QR codes for event attendees, processes RSVP data from an Excel file, and sends personalized invitations via email.

Table of Contents
  1.	Project Overview
  2.	Features
  3.	Requirements
  4.	Setup
     	(Google Sheets API Setup)
  5.	Usage
  6.	File Structure

Project Overview

This project was created to automate the process of handling party invitations. It reads attendee data from an Excel sheet, generates unique QR codes for each attendee, and sends these QR codes via email. The QR codes can be scanned upon arrival to log each guest’s entry.

Features

  1. QR Code Generation: Generates unique QR codes for each registered attendee.
  2. RSVP Data Handling: Processes RSVP responses from an Excel file or Google Sheets.
  3. Email Invitations: Sends QR codes via email using SMTP.
  4. Attendance Tracking: Displays attendee information upon QR code scanning.

Requirements

To run this project, you need the following software and libraries:

  1.Python 3.x
	2. Required Python packages:
  	•	qrcode
  	•	pandas
  	•	openpyxl
  	•	google-auth (for Google API authentication)
  	•	google-auth-oauthlib (for Google API authentication)
  	•	google-auth-httplib2
  	•	google-api-python-client
  	•	smtplib (for email sending)
   
Install them using pip:

  `pip install -r requirements.txt`

Setup
1. Clone the repository:
   
  `git clone https://github.com/yourusername/QR_Code_Invitation.git `
  `cd QR_Code_Invitation`
  3. Set up the virtual environment (optional but recommended):
      `python3 -m venv myenv`
       `source myenv/bin/activate  # On Windows: myenv\Scripts\activate`
  4. Install required packages
      `pip install -r requirements.txt`
  5. Prepare the Excel or Google Sheet: Ensure that your attendee data is stored in attendees_with_qr_codes.xlsx in the /data/ folder, or follow the Google Sheets setup below.
  6. Configure SMTP for email sending: Modify the email sending script to include your email credentials (use environment variables for security if needed).

Google Sheets API Setup

If you’re using the Google Sheets API to automatically pull data from a Google Sheet, follow these steps to set it up:

1. Enable the Google Sheets API

	1.	Go to the Google Cloud Console.
	2.	Create a new project or select an existing project.
	3.	In the left-hand menu, go to APIs & Services > Library.
	4.	Search for “Google Sheets API” and enable it.
	5.	Also, enable the Google Drive API if you need to access Google Sheets stored in your Drive.

2. Create Credentials for the API

	1.	Go to APIs & Services > Credentials in the Google Cloud Console.
	2.	Click on Create Credentials and choose Service Account.
	3.	Fill in the required details and click Create.
	4.	Under Key, click Add Key, then select JSON. This will download a .json file that contains your service account credentials.
	5.	Move the .json file to your project directory and rename it (if needed).

3. Share the Google Sheet with Your Service Account

	1.	Open your Google Sheet (the one you’re using to store RSVP data).
	2.	Click the Share button in the top right.
	3.	Enter the email address of your service account (found in the .json file), and give it “Editor” permissions.

Usage

1.	Run the QR code generation script:
    `python src/QRCode_Generator.py`
2.	Start the server to display the QR code on arrival (if needed):
    `python -m http.server`
3.	
