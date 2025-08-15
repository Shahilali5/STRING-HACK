# TEAM SHAHIL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = os.environ.get("API_ID") or input("Enter your API_ID: ")
    API_HASH = os.environ.get("API_HASH") or input("Enter your API_HASH: ")
    TOKEN = os.environ.get("TOKEN") or input("Enter your Bot TOKEN: ")
    MONGO_URL = os.environ.get("MONGO_URL") or input("Enter your MongoDB URL: ")
    START_PIC = os.environ.get("START_PIC") or input("Enter your Start Pic URL: ")
    
    sudo_ids = os.environ.get("SUDOERS") or input("Enter your Admin IDs (comma-separated): ")
    SUDOERS = filters.user(sudo_ids.split(","))
