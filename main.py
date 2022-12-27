import pandas as pd
import glob #Finds all the pathnames matching a specified pattern 

filepaths = glob.glob("invoices/*.xlsx") #Returns a list with every file that ends with .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1') #Load dataframes
    print(df)
