#program:       __init__
#purpose:       
#progamer:      Themadhood Pequot 3/12/2024

try:
    from .PrintErrorCount import *
except:
    from PrintErrorCount import *


try:
    from Themadhood.URLsCredentals import ErrorURL,ErrorCredentals
    settings["Credentals"] = ErrorCredentals
    settings["URL"] = ErrorURL
except:
    pass




    
