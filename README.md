# Error
A Group of defs to upload Errors to a google Sheet


need to set google sheets Workbook url by setting ErrorURL variable

need to eather have a google .json named Credentals or set Credentals var with your Credentals

Included
+ SecsToTime
    - takes a int or float
    - returns a string "hours : minutes : Seconds"
      
+ LenTime
    - takes a int or float
    - determins time elapsed from input time
    - returns a string "hours : minutes : Seconds"
      
+ DateTime
    - returns ("month / day / year","hours : minutes : Seconds")
      
+ Log
    - Input
        * messge
        * path to file
        * date and time :bool = True
    - wrights to spesified file in background of program
      
+ Rename
    - Input
        * File Path
        * Name and extention of file
        * New Name and extention of file
    - renames .txt file
      
+ LogMove
    - Input
        * source path
        * filename and extention
        * destination path
        * newname and extention = None
    - moves a file
      
+ LogDateCheck
    - Input
        * source path
        * filename and extention
    - if date dosent match then moves to a log file and makes new
      
+ TestInternet
    - tests internet
    - returns True if conection is made
      
+ UploadError
    - Input
        * record = [Py file, Version, Class, Def, Mesege, Error Return]
        * Sheet name
        * Date and Time : bool = True
    - uploads to spesified Sheet name in background of program













