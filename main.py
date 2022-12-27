import pandas as pd
import glob #Finds all the pathnames matching a specified pattern
from fpdf import FPDF
from pathlib import Path 

filepaths = glob.glob("invoices/*.xlsx") #Returns a list with every file that ends with .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1') #Load dataframes
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0] 
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice #{invoice_nr}")
    pdf.output(f'PDFs/{filename}.pdf')
