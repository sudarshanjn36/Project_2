import pandas as pd
import csv
from data_entry import get_amount,get_date,get_category,get_description
from datetime import datetime

class CSV:

    CSV_FILE='finance_date.csv'
    COLUMNS=['date','amount','category','description']

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description): 
        new_entry={                         # This dictionary allows you to keep data and then store ot into csv.
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csv_file:   #Here 'a' is used for append mode, data is added at the end rather than replacing the stored data
            writer = csv.DictWriter(csv_file,fieldnames= cls.COLUMNS)
            writer.writerow(new_entry)
        print('Entry added successfully')

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of Transaction (dd-mm-yyyy) or press 'Enter' for Today's Date")
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

add()