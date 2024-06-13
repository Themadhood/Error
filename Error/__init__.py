__Program__     = "Error.__init__"    
__Programer__   = "Themadhood Pequot"
__Date__        = "3/12/2024"
__Version__     = "0.0.2"
__Update__      = "documentation"
__Info__        = ""

try:
    from .PrintErrorCount import *
except:
    from PrintErrorCount import *

VersionLst += [f"{__Program__}: {__Version__}"]

#allows me to set the URL & Credentals without puting them in all my sorce codes
try:
    from THEMADHOOD.URLsCredentals import ErrorURL,ErrorCredentals
    settings["Credentals"] = ErrorCredentals
    settings["URL"] = ErrorURL
except:
    pass


if __name__ == "__main__":
    VershonRecordsLog(pyName=__Program__,msg=VersionLst)








    

    
