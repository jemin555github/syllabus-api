import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import random
from src.utils.response_utils import Response
import os

# Google Sheet Setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('GOOGLE_CRED_FILE'), scope)
client = gspread.authorize(creds)

# Your Sheet Title
SHEET_NAME = os.getenv('SHEET_NAME')
# Make sure this exists in your Google Drive
sheet = client.open(SHEET_NAME).sheet1

class GoogleSheetService:

    @staticmethod
    def generate_user_id(country: str, state: str, age: int) -> str:
        country_codes = {
            "India": "91",
            "USA": "01",
            "UK": "44",
            "Canada": "02",
            "Australia": "03"
        }

        state_codes = {
            "Andhra Pradesh": "28",
            "Arunachal Pradesh": "12",
            "Assam": "18",
            "Bihar": "10",
            "Chhattisgarh": "22",
            "Goa": "30",
            "Gujarat": "24",
            "Haryana": "06",
            "Himachal Pradesh": "02",
            "Jharkhand": "20",
            "Karnataka": "29",
            "Kerala": "32",
            "Madhya Pradesh": "23",
            "Maharashtra": "27",
            "Manipur": "14",
            "Meghalaya": "17",
            "Mizoram": "15",
            "Nagaland": "13",
            "Odisha": "21",
            "Punjab": "03",
            "Rajasthan": "08",
            "Sikkim": "11",
            "Tamil Nadu": "33",
            "Telangana": "36",
            "Tripura": "16",
            "Uttar Pradesh": "09",
            "Uttarakhand": "05",
            "West Bengal": "19",
            # Union Territories
            "Andaman and Nicobar Islands": "35",
            "Chandigarh": "04",
            "Dadra and Nagar Haveli and Daman and Diu": "26",
            "Delhi": "07",
            "Jammu and Kashmir": "01",
            "Ladakh": "37",
            "Lakshadweep": "31",
            "Puducherry": "34"
        }

        if age <= 12:
            age_group = "01"
        elif 13 <= age <= 19:
            age_group = "02"
        else:
            age_group = "03"

        cc = country_codes.get(country, "00")
        sc = state_codes.get(state, "00")
        random_part = f"{random.randint(0, 9999):04d}"

        return f"{cc}{sc}{age_group}{random_part}"

    @staticmethod
    def save_user_to_sheet(user):
        user_dict = user.dict()
        user_id = GoogleSheetService.generate_user_id(user.country, user.state, user.age)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Header row (1st row)
        header = [
            "First Name", "Last Name", "Email", "Age", "State", "Country",
            "Phone Number", "Language", "Password", "Role", "Grade", "Unique ID", "Created At"
        ]
        if sheet.row_values(1) != header:
            sheet.insert_row(header, index=1)

        # Data row
        row = [
            user.first_name, user.last_name, user.email, user.age,
            user.state, user.country, user.phone,
            user.language, user.password, user.role or "user",
            user.grade, user.unique_id[:10], created_at
        ]
        sheet.append_row(row)

        return Response(
            data={"User ID": user_id, "Email": user.email, "Created At": created_at},
            message="User saved to Google Sheet successfully.",
            success=True,
            status_code=200
        ).send_success_response()
