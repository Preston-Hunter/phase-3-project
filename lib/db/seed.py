from classes.base import Base
from classes.user import User
from classes.activity import Activity
from classes.user_activity_history import UserActivityHistory
from sqlalchemy import *
from sqlalchemy.orm import *
## fake data stuff
#users


engine = create_engine('sqlite:///students.db')
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name = "Nicholas Hunter", address = "My parents house", city = "Issaquah", fave_type = "Hike", age = 18)
user2 = User(name = "Dylan", address = "the ballpark", city = "Denver", fave_type = "Restaurant", age = 25)
user3 = User(name = "Bindi", address = "Gage's floor", city = "Denver", fave_type = "Hike", age = 4)
user4 = User(name = "Mike", address = "It would be weird if I knew", city = "Denver", fave_type = "Cornhole", age = 25)
user5 = User(name = "Bigfoot", address = "Abondoned Mine", city = "Golden", fave_type = "Hike", age = 1000)
user6 = User(name = "Jonah", address = "Again weird", city = "Denver", fave_type = "Cornhole", age = 0)
user7 = User(name = "David", address = "the gas station", city = "Denver", fave_type = "Drug deals", age = 25)

activity1 = Activity(name = "Mayhem Gulch", duration = 2, family_friendly = 1, address = "Mayhem Gulch Juniper Loop Trail", city = "Golden", activity_type = "Hike")
activity2 = Activity(name = "Centennial Cone", duration = 5, family_friendly = 1, address = "Centennial Cone Trailhead", city = "Golden", activity_type = "Hike")
activity3 = Activity(name = "Cherry Cricket", duration = 2, family_friendly = 1, address = "right next door :)", city = "Denver", activity_type = "Restaurant")
activity4 = Activity(name = "Moon Gate asian Grill", duration = 0, family_friendly = 0, address = "745 Quebec St", city = "Denver", activity_type = "Restaurant")
activity5 = Activity(name = "Viewhouse", duration = 2, family_friendly = 1, address = "2015 Market Street", city = "Denver", activity_type = "Cornhole")
activity6 = Activity(name = "Post CodeChallenge Drinks", duration = 1, family_friendly = 0, address = "Probably cherry cricket", city = "Denver", activity_type = "Restaurant")
activity7 = Activity(name = "That shady gas station near me", duration = 0, family_friendly = 0, address = "Who knows", city = "Denver", activity_type = "Drug deals")
activity8 = Activity(name = "Squawk Mountain", duration = 4, family_friendly = 1, address = "Squawk Mountain", city = "Issaquah", activity_type = "Hike")
activity9 = Activity(name = "Issaquah Pho", duration = 2, family_friendly = 1, address = "1025 NW Gilman Blvd", city = "Issaquah", activity_type = "Restaurant")
activity10 = Activity(name = "That skate park next to my old school", duration = 5, family_friendly = 0, address = "Next to the highschool", city = "Issaquah", activity_type = "Drug deals")

uah = UserActivityHistory(user_id = 1, activity_id = 4)
uah1 = UserActivityHistory(user_id = 1,activity_id = 9)
uah2 = UserActivityHistory(user_id = 1,activity_id = 10)

uah3 = UserActivityHistory(user_id = 2,activity_id = 3)
uah4 = UserActivityHistory(user_id = 2,activity_id = 5)
uah5 = UserActivityHistory(user_id = 2,activity_id = 6)
uah6 = UserActivityHistory(user_id = 2,activity_id = 1)

uah7 = UserActivityHistory(user_id = 3,activity_id = 1)
uah8 = UserActivityHistory(user_id = 3,activity_id = 6)

uah9 = UserActivityHistory(user_id = 4,activity_id = 5)
uah10 = UserActivityHistory(user_id = 4,activity_id = 3)
uah11 = UserActivityHistory(user_id = 4,activity_id = 6)

uah12 = UserActivityHistory(user_id = 5,activity_id = 1)
uah13 = UserActivityHistory(user_id = 5,activity_id = 2)
uah14 = UserActivityHistory(user_id = 5,activity_id = 7)

uah15 = UserActivityHistory(user_id = 6,activity_id = 3)
uah16 = UserActivityHistory(user_id = 6,activity_id = 5)
uah17 = UserActivityHistory(user_id = 6,activity_id = 6)

uah18 = UserActivityHistory(user_id = 7,activity_id = 7)
uah19 = UserActivityHistory(user_id = 7,activity_id = 3)







everything = [user1, user2, user3, user4, user5, user6, user7, activity1, activity2, 
              activity3, activity4, activity5,activity6, activity7, 
              activity8, activity9, activity10, uah, uah1, uah2, uah3, uah4, uah5, 
              uah6, uah7, uah8, uah9, uah10, uah11, uah12, uah13, uah14, uah15, uah16, uah17,uah18, uah19]

session.add_all(everything)
session.commit()
print(uah5.id)

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()