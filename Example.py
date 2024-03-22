
import Error

Error.settings["URL"] = "https://docs.google.com/spreadsheets/some jumle of leters and numbers"
Error.settings["Credentals"] = 'F:/Error_Credentals.json'
#or you can
"""
1: make folder in your python lib folder called THEMADHOOD
2: in the THEMADHOOD folder make a .py file called URLsCredentals
3: in the URLsCredentals.py file make and set ErrorURL,ErrorCredentals variables
"""

_FP = os.path.dirname(os.path.abspath(__file__))
#log tests
LogDateCheck(_FP,"Test.txt") #if dates dont match move Test.txt file
Log("\n\n\n\n\ntt","Test.txt")

try:
    startTime = Error.time.time()

    #some lines of code
    Error.time.sleep(3)

    
    Error.Log(f"program run time: {Error.LenTime(startTime)}","Log.txt")
except Exception as e:
    Error.UploadError(["Example.py",
                       "v0.0.1",
                       "class",
                       "def",
                       "custom error mesege",
                       e],
                      "sheet in work book")














