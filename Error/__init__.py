_PYInfo = {"Program":    "Error.__init__",
           "Programer":  "Themadhood Pequot",
           "Date":       "3/12/2024",
           "Version":    "0.0.2",
           "Update":     "documentation",
           "Info":       ""}

try:
    from .PrintErrorCount import *
except:
    from PrintErrorCount import *

PYsInfo += {_PYInfo["Program"]:_PYInfo}
PYInfo = _PYInfo
del _PYInfo #delete extra data not needed

#allows me to set the URL & Credentals without puting them in all my sorce codes
try:
    from THEMADHOOD.URLsCredentals import ErrorURL,ErrorCredentals
    settings["Credentals"] = ErrorCredentals
    settings["URL"] = ErrorURL
except:
    pass




    
