from fastapi import APIRouter
from src.api.v1.auth.schema import AddUser
from src.api.v1.excel_update.service import GoogleSheetService

sheet_router = APIRouter()

@sheet_router.post("/save-to-excel")
def signup_excel(user : AddUser):
    return GoogleSheetService.save_user_to_sheet(user)