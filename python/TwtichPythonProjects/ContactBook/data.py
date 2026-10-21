"""Json  file to save contacts  save edit delete

example:

{
    "contacts":[
            {
                'user_id':1,
                'first_name':'name',
                'last_name':'last_name',
                'phone_number':'45658466455656',
                'email':'one@hotmail.com',
                'address':'201 James St N ',
                'instagram':'@instagram'
            },
            ]

}


"""



from pathlib import Path

import json

current_directory = Path(__file__).parent
file_path = current_directory / "contacts.json"


def generate_user_id():
    """Generate the user Id from the amount of data in our list"""

    # Read the data to get the user Id
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return len(data["contacts"])
    except:
        return 0


def get_current_data():
    """get current data"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except:
        # we found No File or Data
        return None


def save_data(
    first_name: str,
    last_name: None | str,
    phone_number: None | str,
    email: None | str,
    address: None | str,
    instagram: None | str,
):
    """Write data into our database"""

    user_id = generate_user_id()

    data = get_current_data()

    if get_current_data() is None:
        data = {
            "contacts": [
                {
                    "user_id": user_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "email": email,
                    "address": address,
                    "instagram": instagram,
                }
            ],
        }

    else:

        data["contacts"].append(
            {
                "user_id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
                "instagram": instagram,
            }
        )

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return
    except:
        return f"We were not able to write in your database"


def edit_data(user_id: int, value_name: str, value: str):
    """Edit single data from our database

    user_id:
        the user id you want to edit

    value_name:
        the value you want to edit such as email

    value:
        the actual value you will be adding the database

    """

    data = get_current_data()

    for info in data["contacts"]:
        # search data by user id and update it

        if info["user_id"] == user_id:
            info[value_name] = value

    # save the data
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return
    except:
        return f"We were not able to write in your database"


def delete_data(user_id):
    """delete data from our database

        user_id:
            Enter the user id of the data you want deleted
    
    """

    data = get_current_data()

    # return the list of data where the user_id is not equal to want deleted
    contacts = [
        contact for contact in data["contacts"] if contact.get("user_id") != user_id
    ]

    # update the new contact list
    data["contacts"] = contacts

    # save the data with the new contact list
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return
    except:
        return f"We were not able to write in your database"


def edit_all_data(user_id: int, first_name,last_name,phone_number,email,address,instagram):
    """Edit single data from our database

    user_id:
        the user id you want to edit

    value_name:
        the value you want to edit such as email

    value:
        the actual value you will be adding the database

    """

    data = get_current_data()

    for info in data["contacts"]:
        # search data by user id and update it

        if info["user_id"] == user_id:
            info['first_name'] = first_name
            info['last_name'] = last_name
            info['phone_number'] = phone_number
            info['email'] = email
            info['address'] = address
            info['instagram'] = instagram
            
            
    # save the data
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return
    except:
        return f"We were not able to write in your database"