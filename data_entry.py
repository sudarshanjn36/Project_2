from datetime import datetime

date_format='%d-%m-%Y'
CATEGORIES={
    "I":'Income',
    "E":'Expense'
}

def get_date(prompt,allow_default=False):
    date_str = input(prompt)
 
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)  #strftime is string format time
    
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Please enter valid date in dd-mm-yyyy format')
        return get_date(prompt,allow_default)

def get_amount():
    try:
        amount = float(input("Enter the Amount"))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category 'I' for income OR 'E' for Expense. ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid category I for Income E for Expense")
        return get_category()

def get_description():
    description = input('Enter the description')
    return description