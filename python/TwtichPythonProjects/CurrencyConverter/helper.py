from data import get_info

#CALCULATE THE VALUE OF THE CURRENCY YOU WANT AND RETURN VALUE


def change_base_rate(new_base,new_currency):
    
    ''' this function helps us change the base rate if it is not USD'''
    new_base_rate = float(new_base)
    new_currency_rate = float(new_currency)
    
    return new_currency_rate/new_base_rate 

