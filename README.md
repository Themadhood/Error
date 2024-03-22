# Error
A Group of defs to upload Errors to a google Sheet


Befor use you need to set the url and Credentals
this can eather be done after import or by doing the folowing
    + make folder in your lib folder called THEMADHOOD
    + in the THEMADHOOD folder make a .py file called URLsCredentals 
    + in the URLsCredentals.py file make and set ErrorURL,ErrorCredentals variables

Included
+ dict settings
    - "URL" #set url to google sheets work book
    - "Credentals" #set as path to a .json or #set as a dict of the contets of .json
  
+ def SecsToTime
    - takes a int or float
    - returns a string "hours : minutes : Seconds"
      
+ def LenTime
    - takes a int or float
    - determins time elapsed from input time
    - returns a string "hours : minutes : Seconds"
      
+ def DateTime
    - returns ("month / day / year","hours : minutes : Seconds")
      
+ def Log
    - Input
        * messge
        * path to file
        * date and time :bool = True
    - wrights to spesified file in background of program
      
+ def Rename
    - Input
        * File Path
        * Name and extention of file
        * New Name and extention of file
    - renames .txt file
      
+ def LogMove
    - Input
        * source path
        * filename and extention
        * destination path
        * newname and extention = None
    - moves a file
      
+ def LogDateCheck
    - Input
        * source path
        * filename and extention
    - if date dosent match then moves to a log file and makes new
      
+ def TestInternet
    - tests internet
    - returns True if conection is made
      
+ def UploadError
    - Input
        * record = [Py file, Version, Class, Def, Mesege, Error Return]
        * Sheet name
        * Date and Time : bool = True
    - uploads to spesified Sheet name in background of program























