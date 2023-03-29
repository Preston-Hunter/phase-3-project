from classes.base import Base
from sqlalchemy import create_engine
from classes.activity import Activity
from classes.user import User
from classes.user_activity_history import UserActivityHistory
from sqlalchemy.orm import Session, sessionmaker

in_prog = True
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(engine)
session = Session()
Activity(name="hiking").addToDB(engine)
while(in_prog):

    print("Hello message")
    
    
    user_input = input("enter something: ")
    if user_input == "y":
        
        session.query(Activity).first().deleteFromDB(session)    
        #Activity(name = "hiking :)").addToDB(engine)
        print("the func")

