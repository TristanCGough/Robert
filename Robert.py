# importing all the required modules
import pdfplumber
from os import listdir,rename,remove

from pyparsing import And

# SETTINGS
test = False


# creating list of files
files = listdir('PDF')
if test == True:
    listlength = 1
else:
    listlength = len(files)
# Read PDFs


for file in range(listlength):
    INV = "INV"
    ORDER = ""
    with pdfplumber.open(f"PDF/{files[file]}") as pdf:
        first_page = pdf.pages[0].extract_text()
        position = first_page.find("Order Number: ") + 14
        if first_page.find("TAX INVOICE") != -1:
            for d in range(6):
                ORDER = ORDER + first_page[position + d]
            position = first_page.find("Invoice Number: ") + 16
            for d in range(5):
                if first_page[position + d] != "\n":
                    INV = INV + first_page[position + d]
            new_file = f"{ORDER}-{INV}.pdf"
            status = True
        else:
            status=False
    recheck = f"{new_file}" in listdir('PDF')
    if recheck == True:
        print("name taken")
        #feel free to delete duplicate files
        #remove(f"PDF/{files[file]}")
    elif status == True:
        rename(f"PDF/{files[file]}",f"PDF/{ORDER}-{INV}.pdf")
        print(f"Renamed {files[file]} to {ORDER}-{INV}.pdf")

    if test == True:
        print(files[file])
        print(INV)
        print(ORDER)
