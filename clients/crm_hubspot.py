import json
import logging

import requests
from fastapi import HTTPException, status

from settings import Settings

setting_var = Settings

api_key = setting_var.API_KEY_HUBSPOT
hubspot_contact_url = setting_var.HUBSPOT_CONTACT_URL
hubspot_vip_url = setting_var.HUBSPOT_VIP_URL
hubspot_email_url = setting_var.HUBSPOT_EMAIL_URL
hubspot_profile = setting_var.HUBSPOT_PROFILE
hubspot_token = setting_var.HUBSPOT_ACCESS_TOKEN
hubspot_url_v3 = setting_var.HUBSPOT_URL_V3

headers = {
    "content-type": "application/json",
    "authorization": "Bearer %s" % hubspot_token,
}


def get_single_hunty_by_email(email: str) -> object:
    """
    It takes an email address as a string, and returns a dictionary of the Hubspot contact's information

    :param email: str = the email of the user you want to get
    :type email: str
    :return: A dictionary of the user's information
    """

    try:
        payload = {"propertyMode": "value_only"}

        url = f"{hubspot_email_url}/{email}/{hubspot_profile}"

        user_hubspot = requests.get(url=url, params=payload, headers=headers)

        return user_hubspot.json

    except Exception as error:
        logging.error(f"get_single_hunty_by_email Hubspot error {error}")
        raise HTTPException(
            status_code=user_hubspot.status_code,
            detail=f"post_single_hunty Hubspot error : {user_hubspot.json()}",
        )


def get_single_hunty_by_id(id: int):
    """
    It takes an ID, and returns a dictionary of the Hubspot contact's information

    :param id: the HubSpot ID of the contact you want to retrieve
    :type id: int
    :return: A dictionary of the user's information
    """

    try:
        url = f"{hubspot_url_v3}objects/contacts/{id}"

        params = {
            "properties": [
                ""
            ]
        }

        user_hubspot = requests.get(url=url, params=params, headers=headers)
        user_hubspot.raise_for_status()
        return user_hubspot.json()
    except Exception as error:
        logging.info(f"get_single_hunty_by_id Hubspot error {error}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"get_single_hunty_by_id Hubspot error : {error}",
        )


def create_user_hubspot(data):
    """
    It takes a dictionary of data, converts it to JSON, and sends it to the Hubspot API

    :param data: This is the data that you want to send to HubSpot
    :return: The response data is being returned.
    """

    try:
        url = f"{hubspot_url_v3}objects/contacts"

        properties = {"properties": data}

        response = requests.post(url=url, data=json.dumps(properties), headers=headers)
        response_data = response.json()

        response.raise_for_status()

        return response_data

    except Exception as error:
        logging.info(f"error creating user in hubspot {error}")
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail=f"error creating user in hubspot {error}",
        )


def update_user_hubspot(data, hubspot_id):
    """
    It takes a dictionary of data and a hubspot_id, and updates the contact in Hubspot with the given hubspot_id with the
    data in the dictionary

    :param data: This is the data that you want to update in HubSpot
    :param hubspot_id: The HubSpot ID of the contact you want to update
    :return: The response is a JSON object with the following fields:
    """

    try:
        url = f"{hubspot_url_v3}objects/contacts/{hubspot_id}"
        properties = {"properties": data}
        response = requests.patch(url=url, data=json.dumps(properties), headers=headers)
        response_data = response.json()

        response.raise_for_status()

        return response_data
    except Exception as error:
        logging.info(f"error update user in hubspot {error}")
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail=f"error update user in hubspot {error}",
        )


def delete_user_hubspot(hubspot_id):
    """
    It deletes a user from Hubspot.

    :param hubspot_id: The HubSpot ID of the contact you want to delete
    :return: The response is a string with the status code of the request.
    """
    try:
        url = f"{hubspot_url_v3}objects/contacts/{hubspot_id}"

        response = requests.delete(url=url, headers=headers)

        return f"delete user in hubspot_id:{hubspot_id}, status:{response.status_code}"

    except Exception as error:
        logging.info(f"error delete user in hubspot {error}")
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail=f"error delete user in hubspot {error}",
        )
