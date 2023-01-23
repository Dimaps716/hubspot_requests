import os

from dotenv import load_dotenv

load_dotenv()


# > The class `Settings` is a container for all the environment variables that are used in the Hubspot API
class Settings:

    API_KEY_HUBSPOT = os.getenv("API_KEY_HUBSPOT")
    HUBSPOT_URL = os.getenv("HUBSPOT_URL")
    HUBSPOT_URL_V3 = os.getenv("HUBSPOT_URL_V3")
    HUBSPOT_CONTACT_URL = f"{HUBSPOT_URL}contact"

    HUBSPOT_VIP_URL = f"{HUBSPOT_CONTACT_URL}/vid"
    HUBSPOT_EMAIL_URL = f"{HUBSPOT_CONTACT_URL}/email"
    HUBSPOT_PROFILE = "profile?"
    HUBSPOT_APP_ID = os.getenv("HUBSPOT_APP_ID")
    HUBSPOT_ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")
