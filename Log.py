#program:       Log
#purpose:       
#progamer:      Themadhood Pequot 3/12/2024

#imports
import datetime,time,os,io,shutil
from threading import Thread
try:
    from .TimeDefs import *
except:
    from TimeDefs import *




global LogThredActive
LogThredActive = False
_Write_Log = [] #list of logs to wright
        


def Log(msg,path,DT=True):
    dt = ""
    if DT:
        #get date & Time
        now = DateTime()
        #add date & time to beginig of record
        dt = f"({now[0]} {now[1]}): "
    
    _Write_Log.append((msg,path,dt))

    #run in Back Ground if not alredy running
    global LogThredActive
    if not LogThredActive:
        LogThredActive = True
        thread = Thread(target=_ALog)
        thread.start()




def _ALog():
    #repeet till list of logs to right is empty
    while _Write_Log > []:
        log = _Write_Log.pop(0)
        msg = log[0]
        path = log[1]

        #Makes sure date and time is placed after new lines
        newlines = 1
        if msg[:newlines] == "\n":
            while msg[newlines] == "\n":
                newlines += 1
            msg = msg[:newlines]+log[2]+msg[newlines:]
        else:
            msg = log[2]+msg

        #cheke file path for Log
        try:
            if not os.path.isfile(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
        except:
            pass

        #wright to Log File
        with io.open(path, 'a', encoding='utf-8') as log:
            log.write(msg)
            log.write("\n")
            log.close()

    
    global LogThredActive
    LogThredActive = False


#renames file
def Rename(path,name,new):
    os.rename(f"{path}/{name}",f"{path}/{new}")


#Moves a log
def LogMove(source, filename, destination, newname = None):
    if newname != None:
        Rename(source,filename,newname)
        filename = newname

    try:
        if not os.path.isfile(f"{destination}/"):
            os.makedirs(os.path.dirname(f"{destination}/"), exist_ok=True)
    except:
        pass
        
    shutil.move(f"{source}/{filename}", destination)



def LogDateCheck(filepath,filename):
    #get current date
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    Ldate = date.split("-")

    #chek if exists
    try:
        if not os.path.isfile(f"{filepath}/{filename}"):
            os.makedirs(os.path.dirname(f"{filepath}/{filename}"),
                        exist_ok=True)
            _Write_Log.append((date,f"{filepath}/{filename}",""))
            _ALog()
    except:
        pass

    #get log date
    fin = open(f"{filepath}/{filename}")
    logdate = fin.readline()
    fin.close()
    logdate = logdate.removesuffix("\n")
    Llogdate = logdate.split("-")

    #Cheke Date And move if year or Month dont Match
    for d in range(2,-1,-1):
        if Ldate[d] != Llogdate[d]:
            LogMove(filepath, filename, f"{filepath}/Logs",
                    f"{filename.removesuffix('.txt')} {logdate}.txt")
            _ALog(date,f"{filepath}/{filename}",False)
            break



        

if __name__ == "__main__":
    _FP = os.path.dirname(os.path.abspath(__file__))
    #log tests
    LogDateCheck(_FP,"Test.txt")
    Log("\n\n\n\n\ntt","Test.txt")




    

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







    
