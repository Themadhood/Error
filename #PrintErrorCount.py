#program:       FetchStats
#purpose:       Fetches records
#progamer:      Madison Arndt 5/8/2023

_VERSION = "0.0.1"

#imports
from __init__ import _URL,gspread,ServiceAccountCredentials,time

def _GetAllFromSheet(workbook,SheetName,Retry=0):
    FailCount = 0
    while True:
        try:
            DataSet = workbook.worksheet(SheetName).get_all_records()
            break
        except IndexError:
            DataSet = []
            break
        except:
            FailCount += 1
            msg = f"Faild to load {workbook.title}.{SheetName} records \
{FailCount} times {Retry} Retry"
            if FailCount > 100 and Retry < 5:
                print(msg)
                time.sleep(30)
                while True:
                    try:
                        return _GetAllFromSheet(workbook,SheetName,Retry+1)
                    except:
                        Retry+=1
            else:
                DataSet = workbook.worksheet(SheetName).get_all_records()
    return DataSet

def returnErrorCount(errorlist):
    try:
        if "Error Count" in list(errorlist[0]):
            errors = 0
            for e in errorlist:
                errors += e["Error Count"]
            return errors
        else:
            return len(errorlist)
    except:
        return 0


RC_DCT = dict()
#Login
gc = gspread.service_account(filename="Personal.json")
#open work book
WorkBook = gc.open_by_url(_URL)
#get all sheets in work book
sheets = WorkBook.worksheets()
#get all recods from all the sheets
for Sheet in sheets:
    SheetName = Sheet.title
    print(f"getting: {SheetName} records")
    DataSet = _GetAllFromSheet(WorkBook,SheetName)
    RC_DCT.update({SheetName:DataSet})

gc.session.close()
print()
print()

lst = list(RC_DCT)
for i in lst:
    if i != "Blank" and i != "Test":
        total = returnErrorCount(RC_DCT[i])
        print(f"Total: {total}\tDifrent: {len(RC_DCT[i])}\t{i} Errors")


#index.title#name of sheet
"""
#change sheet
sheet = WorkBook.worksheet("Ornithischia")
#get all Records as list of dcts
dataSet1 = sheet.get_all_records()
#create Sheet
newsheet = gsheet.add_worksheet(title="New Worksheet", rows="100", cols="20")
#delete sheet
gsheet.del_worksheet(newsheet)
#get cell value
cval = wsheet.acell('A2').value
#update cell value
wsheet.update('A2', 'John')
#get all row valls
row_index = 2
values_row = wsheet.row_values(row_index)
#get all colum values
col_index = 3
values_column = wsheet.col_values(col_index)
#insert new row
student_data = ['Emily', 'Watson', 89]
new_row_index = 6
wsheet.insert_row(student_data, new_row_index)
"""




