from setuptools import setup

#from my_pip_package import __version__

setup(
    name='TPC_Error',
    version="1.0.0",#__version__,

    url='https://github.com/Themadhood/Error',
    author='Themadhood Pequot',
    author_email='themadhoodpequot@gmail.com',

    py_modules=['Error'],

    install_requires=[
        "gspread",#manipulates google sheets
        "oauth2client",#logs in to google
        "google-api-python-client",],
)
