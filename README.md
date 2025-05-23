# 🎟️ QR Code Party Invitation System

This Python-based project automates the invitation process for events. It reads RSVP data from an Excel file or Google Sheets, generates **unique QR codes** for each guest, and sends **personalised email invitations**. Upon arrival, guests can scan their QR codes for check-in, allowing for efficient attendance tracking.

---

## 📑 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
   - [Google Sheets API Setup](#google-sheets-api-setup)
5. [Usage](#usage)
6. [File Structure](#file-structure)
7. [Future Improvements](#future-improvements)
8. [License](#license)

---

## 📌 Project Overview

This project was created to simplify and automate the process of managing party invitations. It supports both **Excel** and **Google Sheets** as data sources, allowing organisers to:
- Import RSVP data
- Generate QR codes for each attendee
- Email those codes as invitations
- Use a basic frontend or server to scan and check in guests

---

## ✨ Features

- **QR Code Generation**: Creates unique QR codes for each registered guest.
- **RSVP Data Handling**: Imports data from Excel or Google Sheets.
- **Email Invitations**: Sends QR codes via email using SMTP.
- **Attendance Tracking**: Displays guest details when QR is scanned (optional feature).
- **Webcam Integration (JS)**: Uses `getUserMedia` for real-time QR code scanning.

---

## ⚙️ Requirements

- Python 3.x

### Python Packages
Install all dependencies with:
```bash
pip install -r requirements.txt
```

```
qrcode
pandas
openpyxl
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
```

---

## 🛠️ Setup

### Clone the Repository
```bash
git clone https://github.com/yourusername/QR_Code_Invitation.git
cd QR_Code_Invitation
```

### (Optional) Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Prepare the RSVP Data
- Store attendee info in `data/attendees_with_qr_codes.xlsx`
- Or use a Google Sheet and follow the [Google Sheets API Setup](#google-sheets-api-setup)

### Configure Email Sending
- Edit your SMTP credentials in `email_sender.py`
- Use environment variables or a `.env` file for secure storage

---

## 🔌 Google Sheets API Setup

If using Google Sheets for RSVP data:

1. **Enable APIs**  
   - Go to Google Cloud Console  
   - Enable: `Google Sheets API` and `Google Drive API`

2. **Create a Service Account**  
   - Create new credentials as a **Service Account**  
   - Download the `.json` key  
   - Place it in `credentials/` and rename it if necessary

3. **Share the Google Sheet**
   - Open your Sheet  
   - Click **Share**, and add the service account’s email with **Editor** permissions

---

## ▶️ Usage

1. **Generate QR Codes and Send Emails**
```bash
python src/QRCode_Generator.py
```

2. **(Optional) Serve Web Page for QR Check-In**
```bash
python -m http.server
```

> Add your HTML/CSS/JS scanner frontend in the root or `public/` directory.

---

## 📂 File Structure

```
QR_Code_Invitation/
├── data/
│   └── attendees_with_qr_codes.xlsx
├── src/
│   ├── QRCode_Generator.py         # Main script for QR + email
│   ├── email_sender.py             # Sends emails via SMTP
│   └── utils.py                    # Helper functions
├── credentials/
│   └── service_account.json
├── public/                         # (Optional) QR scanner page
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚧 Future Improvements

- Add web dashboard to track check-ins in real time
- Auto-email QR on form submission (Google Apps Script)
- Scan logs with timestamps for each guest
- Full event analytics (e.g., turnout rate, scan time)

---

## 📜 License

This project is licensed under the MIT License.
