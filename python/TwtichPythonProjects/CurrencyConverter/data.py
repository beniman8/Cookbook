# learn how to use the API 
from decouple import config 
import requests 
from pathlib import Path
import json
from datetime import datetime

YOUR_APIKEY=config("YOUR_APIKEY")

API= f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={YOUR_APIKEY}"


current_directory = Path(__file__).parent
file_path = current_directory / "currency.json"


def update_data_from_api():
    '''This helps us get data from the api and save it to our local environment'''
    
    response = requests.get(API)
    data_file={}
    


    if response.status_code == 200:
        #update the local date
        data_file['local_date']=datetime.now().isoformat()
        
        with open(file_path,'w',encoding='utf-8') as file:
            #created our data file
            data = response.json() 
            data_file.update(data)
            json.dump(data_file,file,indent=4)   
        


    else:
        print("YOU FAILED BRO")
    
    
    

def get_available_currencies():
    ''' return list of all currencies available from your api'''
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            #created our data file
            data = json.load(file)
    except:
        update_data_from_api()


    return list(data['rates'].keys())


def get_info():
    ''' get all the data from the data file'''

    with open(file_path,'r',encoding='utf-8') as file:
        #created our data file
        data = json.load(file)
        
    return data



def get_value_of_currency(currency:str):
    ''' return currency value you want'''
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            #created our data file
            data = json.load(file)
    except:
        update_data_from_api()


    return data['rates'][currency]


def get_update_date_text():
    ''' return the date of api database update'''

    with open(file_path,'r',encoding='utf-8') as file:
        #created our data file
        data = json.load(file)



    return data['local_date'][0:10]  









