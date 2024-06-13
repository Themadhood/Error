__Program__     = "Error.Upload"    
__Programer__   = "Themadhood Pequot"
__Date__        = "3/12/2024"
__Version__     = "0.0.2"
__Update__      = "documentation"
__Info__        = "Upload errors to google sheet"

#imports
import gspread,requests
from oauth2client.service_account import ServiceAccountCredentials
try:
    from .Log import *
except:
    from Log import *

VersionLst += [f"{__Program__}: {__Version__}"]


def TestInternet():
    try:
        requests.get('https://www.google.com/').status_code
        return True
    except:
        return False




#url of google workbook with error sheet
settings = {"URL":"",

#credentals
            "Credentals":{}}

_FP = os.path.dirname(os.path.abspath(__file__))
if settings["Credentals"] == {}:
    settings["Credentals"] = f'{_FP}/Credentals.json'



global UploadThredActive
UploadThredActive = False
_upload_records = [] #list of errors to wright


def UploadError(Record,sheet,DT=True):
    """record = [Py file,Version,Class,Def,Mesege,Error Return]"""
    if DT:
        #get date & Time
        now = DateTime()
        #add date & time to beginig of record
        Record.insert(0,now[1])
        Record.insert(0,now[0])
    
    _upload_records.append((Record,sheet))

    #run in Back Ground if not alredy running
    global UploadThredActive
    if not UploadThredActive:
        UploadThredActive = True
        thread = Thread(target=_Upload_Error)
        thread.start()
    

def _Upload_Error():

    #if internet acsses
    if TestInternet():
        GSE = _GetSavedErrors()
        if GSE != None:
            while GSE > []:
                _upload_records.append(GSE.pop())

        #run while there are still errors to uplode
        while _upload_records > []:
            error = _upload_records.pop(0)
            if len(error[0]) < 8:
                error[0].append("")
            _UploadError(error[0],error[1])

    #if no acsses     
    else:
        _SaveErrors(Record,sheet)
    
    global UploadThredActive
    UploadThredActive = False



def _UploadError(Record,sheet):
    try:
        #Login
        try:
            gc = gspread.service_account(filename=settings["Credentals"])
        except:
            gc = gspread.service_account_from_dict(settings["Credentals"])
        #open work book
        WorkBook = gc.open_by_url(settings["URL"])
        #opens Mob Sheet
        Sheeet = WorkBook.worksheet(sheet)
        #gets all records
        try:
            Records = Sheeet.get_all_records()
        except:
            Records = []
        for i in range(len(Records)):
            #cheks for same error
            if Records[i]["Mesege"] == Record[-2]:
                #Updates error count
                Sheeet.update(f'G{i+2}', f"{Records[i]['Error Count']+1}")
                #Updates date
                Sheeet.update(f'A{i+2}', f"{Record[0]}")
                #Logout
                gc.session.close()
                return
        
        Record.insert(-2,1)
        Record[-1] = str(Record[-1])
        #insert new row
        Sheeet.insert_row(Record, 2)
        #Logout
        gc.session.close()
    except Exception as e:
        gc.session.close()
        time.sleep(15)
        _UploadError(Record,sheet)



def _GetSavedErrors():
    if os.path.exists(_FP+"/_Error.py"):
        with io.open(_FP+"/_Error.py", 'a', encoding='utf-8') as error:
            error.write("]")
            error.close()
        try:
            from . import _Error
        except:
            import _Error
                
        records = _Error.records
        
        os.remove(_FP+"/_Error.py")

        return records



def _SaveErrors(Record,sheet):
    #if file dosent exist make it
    if not os.path.exists(_FP+"/_Error.py"):
        with io.open(_FP+"/_Error.py", 'w', encoding='utf-8') as error:
            error.write("records = [")
            error.close()
    #if file exist apend on to it
    else:
        with io.open(_FP+"/_Error.py", 'a', encoding='utf-8') as error:
            error.write(",\n")
            error.close()
    #Add record to error py
    with io.open(_FP+"/_Error.py", 'a', encoding='utf-8') as error:
        error.write(f"('{sheet}',{Record})")
        error.close()

        
     

if __name__ == "__main__":#error check
    VershonRecordsLog(pyName=__Program__,msg=VersionLst)
    UploadError([__Program__,__version__,"","","test",0],"Test")




    

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







    
