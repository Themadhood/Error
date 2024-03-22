#program:       __init__
#purpose:       
#progamer:      Themadhood Pequot 3/12/2024

try:
    from .PrintErrorCount import *
except:
    from PrintErrorCount import *

#alows me to set the URL & Credentals without puting them in all my sorce codes
try:
    from THEMADHOOD.URLsCredentals import ErrorURL,ErrorCredentals
    settings["Credentals"] = ErrorCredentals
    settings["URL"] = ErrorURL
except:
    pass




    
