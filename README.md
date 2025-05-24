Here's project with UI auto-tests using Playwright.

1. Make sure virtual environment are created and activated:
   - [ ]    `Project python -m venv .venv`
   - [ ]    `.venv\Scripts\activate`
   
   Result: (.venv) should appear at the beginning of work directory

2. Add interpreter to .venv if needed
   - [ ]   interpreter added (see Hint) 

3. Install all needed dependencies for Playwrigh
   - [ ]    `playwright install`



### HINTS:
1. Steps for adding Interpreter to the Project virtual Environment:
    1. Open PyCharm and go to project settings: File > Settings (или Ctrl + Alt + S).
    2. Choose the Project section: > Project Interpreter.
    3. Click on the gear icon and select Add....
    4. Select in opened window "Existing environment" and specify the path to your environment (usually: your_project_name\venv\Scripts\python.exe for Windows).
    5. Add the interpreter and apply the changes.
2. Make sure the virtual environment is created and activated:
File -> Settings -> Project(Name og project) -> Python Interpreter:
Python 3.9 is installed to venv to the root of the Project

3. If tests fail check the following:

- Versions of requirements are compatible: pay attention to selenium version and webdriver-manager
(on the moment of writing this Readme.md the following versions are working correctly:
selenium == 4.11.2 webdriver-manager==4.0.1)
- Clear cache: __pycash folder in Project folder
- Delete the broken driver file (new ones will be created):
C:\Users<smth_like_user>.wdm\gw0\drivers\chromedriver\win64\128.0.6613.137\chromedriver-win32
If project doesn't run after these steps contact to Dev / PM LEAD
