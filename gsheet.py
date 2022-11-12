from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
scopes = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("tj_test.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("TJ_Test_Sheet")  #open sheet
sheet = sheet.sheet1 #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1

def get_blank_row():
    row = 1
    while sheet.cell(row,1).value:
        row += 1
    return row


def append_to_sheet(reviewer, input_text, classification, annotation):
    row = get_blank_row()
    sheet.update_cell(row, 1, reviewer)
    sheet.update_cell(row, 2, input_text)
    sheet.update_cell(row, 3, classification)
    sheet.update_cell(row, 4, annotation)