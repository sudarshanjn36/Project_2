from datetime import datetime

def get_date(prompt,allow_default=False):
    date_str = input(prompt)
    date_format='%d-%m-%Y'
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)  #strftime is string format time
    
    try:
        valid_date = datetime.strftime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Please enter valid date in dd-mm-yyyy format')
        return get_date(prompt,allow_default)

def get_amount():
    try:
        amount=float(input())
        if amount<=0:
            raise ValueError("Amount must be greater than 0")
    except ValueError as e:
        print(e)
        return get_amount()
    pass