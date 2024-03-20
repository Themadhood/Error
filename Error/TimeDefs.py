#program:       TimeDefs
#purpose:       
#progamer:      Themadhood Pequot 3/12/2024

#imports
import datetime,time


def SecsToTime(sec):
    """takes a int or float and formats as hour : minute : Seconds"""
    return time.strftime('%H:%M:%S', time.gmtime(sec))

def LenTime(start):
    """takes a int or float and and tells time pased as hour : minute : Seconds"""
    return SecsToTime(time.time()-start)

def DateTime():
    """returns date and time"""
    now = datetime.datetime.now()
    #formats
    HMS = datetime.datetime.strftime(now, '%H:%M:%S')
    MDY = datetime.datetime.strftime(now, '%m/%d/%Y')
    
    return MDY,HMS






        

if __name__ == "__main__":
    startTime = time.time()

    time.sleep(5) #wait 5 seconds

    runTime = LenTime(startTime)

    print("TotalRunTime",runTime)












    
