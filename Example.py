
import Error

Error.settings["URL"] = "https://docs.google.com/spreadsheets/some jumle of leters and numbers"
Error.settings["Credentals"] = 'F:/Error_Credentals.json'
               

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














