__Program__     = "Error.PrintErrorCount"    
__Programer__   = "Themadhood Pequot"
__Date__        = "3/12/2024"
__Version__     = "0.0.2"
__Update__      = "documentation"
__Info__        = "fetches and counts errors from a google sheet then \
prints resalts"

#imports
try:
    from .Upload import *
except:
    from Upload import *

VersionLst += [f"{__Program__}: {__Version__}"]

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

def _returnErrorCount(errorlist):
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

def PrintErrorCount():

    RC_DCT = dict()
    #Login
    try:
        gc = gspread.service_account(filename=settings["Credentals"])
    except:
        gc = gspread.service_account_from_dict(settings["Credentals"])
    #open work book
    WorkBook = gc.open_by_url(settings["URL"])
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
            total = _returnErrorCount(RC_DCT[i])
            print(f"Total: {total}\tDifrent: {len(RC_DCT[i])}\t{i} Errors")

if __name__ == "__main__":
    VersionRecordsLog(pyName=__Program__,msg=VersionLst)
    #settings["URL"] = 
    #settings["Credentals"] = 

    
    PrintErrorCount()

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




