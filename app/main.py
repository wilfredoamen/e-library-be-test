#main application logic 
#first time steps: 1. clone repo, 2. on command prompt pip install -r requirements.txt
#importing the necessary nequirement
from fastapi import FastAPI
from .setup_main import configure_cors, create_db_and_tables
# example from .routers import user_management, Use the assign space below to import your router
#fola : use 10

#josh: use the below

#juilet: use the below

#nelson: use the below

#precious: use the below

#do not write below, discuss with team lead misecellonus spaces for any other deemed importation to main file






#WARNING: DO NOT EDIT THE EMPTY SPACE BELOW: future logging configuration space for custom middleware if necessary








#calling an instance of fast api
app = FastAPI(
    title="E-Library API",
    description="API for managing an electronic library system.",
    version="1.0.0"
)

#definiing the cors function
configure_cors(app)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# NB: PLEASE INCLUDE YOUR ROUTER IN YOUR NAME FIELD BELOW
# example app.include_router(user_management1.router)

#FOLA: YOU ARE NUMBER 1(REMEMBER TO ADD 1 TO ANY FILE YOU CREATE TO AVOID NAME CONFLICT e.g user_management1.py): USE the lines below




#JOSH:YOU ARE NUMBER 2(REMEMBER TO ADD 2 TO ANY FILE YOU CREATE TO AVOID NAME CONFLICT e.g user_management2.py): USE the lines below




#JULIET: YOU ARE NUMBER 3(REMEMBER TO ADD 3 TO ANY FILE YOU CREATE TO AVOID NAME CONFLICT e.g user_management3.py): USE the lines below



#NELSON: YOU ARE NUMBER 4(REMEMBER TO ADD 4 TO ANY FILE YOU CREATE TO AVOID NAME CONFLICT e.g user_management4.py): USE the lines below




#PRECIOUS: YOU ARE NUMBER 5(REMEMBER TO ADD 5 TO ANY FILE YOU CREATE TO AVOID NAME CONFLICT e.g user_management5.py): USE the lines below




#WARNING: PLEASE ASIDE FROM THE NUMBER ASSIGN VIA MAIN FILE TO YOU, PLEASE DO WRITE ON THE MAIN FILE
#PLEASE DO NOT EDIT THE DATABASE SETUP FILE, FOR ANY NEW UPDATE DISCUSS WITH YOUR TEAM AND TEAM LEAD
#FUTURE CUSTOM MIDDLEWARE: DISCUSS WITH YOUR TEAM LEAD FOR ANY CUSTOMER MIDDLEWARE THAT NEED TO COME IN





