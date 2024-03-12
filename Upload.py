#program:       Upload
#purpose:       
#progamer:      Themadhood Pequot 3/12/2024

#imports
import gspread,requests
from oauth2client.service_account import ServiceAccountCredentials
try:
    from .Log import *
except:
    from Log import *


def TestInternet():
    try:
        requests.get('https://www.google.com/').status_code
        return True
    except:
        return False



_FP = os.path.dirname(os.path.abspath(__file__))
_URL = "https://docs.google.com/spreadsheets/d/1D9sFEHfsM1UfDFXicpPkyFZiWNK7bjf6t9EVzCYWePI/edit?usp=sharing"
_Credentals = {"type": "service_account",
               "project_id": "errors-387223",
               "private_key_id": "491dea1366644636c196c275a627661eda3fd9f3",
               "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC3UGHF2YUT1CFT\nGfiUSyYnD1xXDEjdy6ZBphcIoFqLvqmJEKCMYX2pMDLts0++bRX0MrWsGKe+5BIc\naRUg3Rh2FkQny9c3uYc3LpXLme2yQ7Wj8saEL/kAswI3lSEXCsIU5AOoWpjF6r7y\n/J4r9G8CjEtM6+ge10ihR8QOn3xeX3YyKdN4vUy4Z94bLYbWNxT5+8VS9iUMg2VX\nh58pcLIzOTfeVYSX+rq3bkOMKR/rLfp9eMfIbGNwbGGOEnmjFUeyBI13PuOtYyx1\nRcFOcsEmh/rYy93IF+sAkC3G+RbtF62ZHCMXYzVtSqcp6qWaPR3N5VNtKbWPM8k0\nRt5eYdnRAgMBAAECggEACdv5lz1fz0FE9dIPNOQeEiKdDPw+2MmCyJP/GAZeWlbj\nyci+dtBpRJnQWmkfDksSD8VQsLfugTmFaRhkg9UKY1MHIUQRECjjBy5y7W1666Ah\nR0cn4s0M+Zr3IP/NBN8N8VdSZEoTnoz1rk5UkEEEPbUHmYR0YoDCEfUQ/BebNfzZ\nZJrGlK2uxLltqOParZBbT6GzmyJIkrZdaNQawbklofCTW0l13KaRHft2Tpdff0mJ\n5RpgRpAjDIKavX4ncs2G0p5CJzVbVwEsgPtOPAkzaLzZ8MkeTzIOrOzjvESl4OFb\nnEbGBMeZdHtE4V00tO+ZS5Et/5+lMAU+cVSg5qDroQKBgQDr6GRYKLgNSUhmVyyG\nJRe3a/CS/YscaoltUiaNChADIw9a6+HJtJOOLiUf5HKV2O5GjjIHzTNFam5tdvpP\nRHo74eiuRxvBoT8l/YiTJ5HFO8R1nhQKGL+3YsHpALR+AEmiofwp9//jLSBkE8vC\napxBsVqBfRck1sgKcXX0LN6Z4QKBgQDG7UNM/QPLZ22fu7krL2k1vxpfSej5SAIt\nD8u1rygCF+NIkauhD5yElu8a31HC99wNmg4Tv5673XaqampaVZoBsYkicH1MEE6H\nuaPYOxnyT9ogZe6WBhAdNkLAk1iXV+MAT6A/v9woPju2PfSTlaYCOX7Tv+aRBFvA\nY8SjMvSd8QKBgAzsMAL8SAjCSOsCP3ghtAjiKs2CggpOc7S/WUlEkdf6Ja8vWLD5\n6VNSh8oVc4lt1q+avnba8MIOsHnimJebAq8hEuPpFUYoFRN5re+RrVSGj555yFM9\nQ9NB36lp1nlIfsAf63ZJFYVWRX3176V4vZKDqpeJSKlF8rNPv8xeYNtBAoGANJJv\nvuD/J7pl1lkeTrNw8qtWpOg7keXd7VrHU3S+9g6qGnulCCPAEapx9oAec5Bdr5qP\nLdjucmfM/Kyy/rywvtHUlC12b6u/lU8SZgr4iHliBD3sF+nySEYWzh4iw5yOeX6R\ns0dZP6lyzm8BPB/Ih736LqwAm0KznNzBEwBcdYECgYBXFKd2GjtyUAmh/ht3MjzA\n/t6G4RggTLYacF9sXQHYSy1RP2kbwHzzyt46nT8PpV4Xx+drTd0sCI/YqKHyT2Os\nNUH1eXQVNJ5kCBwSIX+5tnyeL3kFIC3WOGBl4zIsYN4+vEAY/+58dxdbPbfASzzb\nsq4bN0RPiJkLA0l2t9c9Yg==\n-----END PRIVATE KEY-----\n",
              "client_email": "error-137@errors-387223.iam.gserviceaccount.com",
               "client_id": "116299256214128577731",
               "auth_uri": "https://accounts.google.com/o/oauth2/auth",
               "token_uri": "https://oauth2.googleapis.com/token",
               "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
               "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/error-137%40errors-387223.iam.gserviceaccount.com",
               "universe_domain": "googleapis.com"}



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
            gc = gspread.service_account(filename=f'{_FP}/Credentals.json')
        except:
            gc = gspread.service_account_from_dict(_Credentals)
        #open work book
        WorkBook = gc.open_by_url(_URL)
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
    UploadError(["Error.__init__","0.0.1","","","test",0],"Test")




    

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







    
