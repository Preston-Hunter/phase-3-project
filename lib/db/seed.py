from classes.base import Base
from classes.user import User
from classes.activity import Activity
from classes.user_activity_history import UserActivityHistory
from sqlalchemy import *
from sqlalchemy.orm import *


engine = create_engine('sqlite:///students.db')
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name = "Preston Hunter")
activity1 = Activity(name = "hike")
uah1 = UserActivityHistory()
everything = [user1]
session.add_all(everything)
session.commit()

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()