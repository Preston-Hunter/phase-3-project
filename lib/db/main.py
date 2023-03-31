from classes.base import Base
from sqlalchemy import create_engine, text, func, desc
from classes.activity import Activity
from classes.user import User
from classes.user_activity_history import UserActivityHistory
from sqlalchemy.orm import Session, sessionmaker
import shlex
import random
from collections import Counter

def main():
    in_prog = True
    engine = create_engine('sqlite:///students.db')
    Session = sessionmaker(engine)
    session = Session()
    response = ""
    print("Welcome!")
    mode = "friendly"
    while(in_prog):
        print("Choose your option by typing the appropriate word that is contained in square brackets")
        mode = input("Choose mode [admin] or [user], or [quit]: ")
        if mode == "admin":
            in_admin = True
            displayTechnicalOptions()
            while in_admin:
                user_input = input("What would you like to do: ")
                if user_input == "help":
                    displayTechnicalOptions()
                elif user_input == "create":
                    user_input = input("Type the corresponding number for the Data entry you would like to create. \n\
                                    User (1), Activity (2), UserActivity(3). Type 4 to restart: ")
                    if user_input == "1":
                        print("Enter data for the user entry in this order")
                        user_field_list = input("Name age address city favorite_activity_type: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        User(name = user_field_list[0],city = user_field_list[3],address = user_field_list[2], fave_type = user_field_list[4],age = int(user_field_list[1])).addToDB(engine)
                    elif user_input == "2":
                        print("Enter data for the activity entry in this order")
                        user_field_list = input("name address city duration family_friendly(a value of 0 or 1) : \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        
                        Activity(name = user_field_list[0],address = user_field_list[1], city = user_field_list[2], duration = int(user_field_list[3]), family_friendly = int(user_field_list[4]), activity_type = user_field_list[5]).addToDB(engine)
                    elif user_input == "3":
                        print("Enter data for the activity entry in this order: \n")
                        user_field_list = input("user_id activity_id")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        UserActivityHistory(user_id = int(user_field_list[0]), activity_id = int(user_field_list[1])).addToDB(engine)
                    elif user_input == "4":
                        print("back to start")
                elif user_input == "delete":
                    user_input = input("Type the corresponding number for the Data entry type you would like to delete: \n\
                                    User (1), Activity (2), UserActivity(3). Type 4 to restart: ")
                    if user_input == "1":
                        user_input = input("Enter User id of entry you would like to delete")
                        to_delete_list = session.query(User).filter(User.id == int(user_input))
                        if to_delete_list.first() != None:
                            to_delete_list.first().deleteFromDB(session)
                            print("Delete success")
                        else:
                            print("Entry with that ID does not exist")
                    elif user_input == "2":
                        user_input = input("Enter id of Activity entry you would like to delete")
                        to_delete_list = session.query(Activity).filter(Activity.id == int(user_input))
                        if to_delete_list.first() != None:
                            to_delete_list.first().deleteFromDB(session)
                            print("Delete success")
                        else:
                            print("Entry with that ID does not exist")
                    elif user_input == "3":
                        user_input = input("Enter id of UserActivity you would like to delete")
                        to_delete_list = session.query(UserActivityHistory).filter(UserActivityHistory.id == int(user_input))
                        if to_delete_list.first() != None:
                            to_delete_list.first().deleteFromDB(session)
                            print("Delete success")
                        else:
                            print("Entry with that ID does not exist")
                    else:
                        print("back to start")

                elif user_input == "update":
                    user_input = input("Type the corresponding number for the Data entry type you would like to update: \n\
                    User (1), Activity (2), UserActivity(3). Type 4 to restart: ")
                    if user_input == "1":
                        print("Enter data for the updated user entry in this order")
                        user_field_list = input("CurrentId new_name new_age new_address new_city new_favorite_activity_type: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        updateUser(session, int(user_field_list[0]), user_field_list[1], user_field_list[5], int(user_field_list[2]), user_field_list[4], user_field_list[3] )
                    elif user_input == "2":
                        print("Enter data for the updated activity entry in this order")
                        user_field_list = input("CurrentId, new_name, new_address, new_city, new_duration, new_family_friendly, new_activity_type: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        updateActivity(session, user_field_list[0], user_field_list[1], user_field_list[4], user_field_list[5], user_field_list[6], user_field_list[3], user_field_list[2])
                    elif user_input == "3":
                        print("Enter data for the updated UserActivity entry in this order")
                        user_field_list = input("CurrentId, user_id, activity_id : \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        updateUserActivity(session, user_field_list[0], user_field_list[1], user_field_list[2])
                    else:
                        print("back to start")
                elif user_input == "read":
                    user_input = input("Type the corresponding number for the Data entry type you would like to Filter/Read. Use single quotes around string entries: \n\
                    User (1), Activity (2), UserActivity(3). Type 4 to restart: ")
                    if user_input == "1":
                        print("Enter data for the filtered users list in this order")
                        user_field_list = input("CurrentId name age address new_city favorite_activity_type: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        user_field_list = Noneify(user_field_list)
                        filtered_list = filteredUsers(engine, session, user_field_list[0], user_field_list[1], user_field_list[5], user_field_list[2], user_field_list[4], user_field_list[3])
                        [print(u) for u in filtered_list]

                    elif user_input == "2":
                        print("Enter data for the filtered Activities list in this order")
                        user_field_list = input("CurrentId, name, address, city, duration, family_friendly, activity_type: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        user_field_list = Noneify(user_field_list)
                        filtered_list = filteredActivity(engine, session, user_field_list[0], user_field_list[1], user_field_list[4], user_field_list[5], user_field_list[6], user_field_list[3], user_field_list[2])
                        [print(u) for u in filtered_list]
                    
                    elif user_input == "3":
                        print("Enter data for the filtered UserActivities list in this order")
                        user_field_list = input("CurrentId, user_id, activity_id: \n")
                        user_field_list = shlex.split(user_field_list, posix=False)
                        user_field_list = Noneify(user_field_list)
                        filtered_list = filteredUserActivity(engine, session, user_field_list[0], user_field_list[1], user_field_list[2])
                        [print(u) for u in filtered_list]
                    else:
                        print("back to start")

                elif user_input == "advanced":
                    print("WIP")
                
                elif user_input == "exit":
                    in_admin = False
            
        # todo delete and join tables?
        elif mode == "user":
            in_friendly = True
            while in_friendly:
                print("\ntype the keyword in brackets or refer to it numerically by its order, starting with 1")
                user_input = input("[new] or [returning] user, or [quit] user mode?: ")
                if user_input == "1" or user_input == "new":
                    print("WIP\n")
                    pass
                elif user_input == "2" or user_input == "returning":
                    auth = False
                    cont = True
                    current_user = ""
                    while not auth and cont:
                        user_input = input("Whats your user id? (type a non numerical to quit): ")

                        try:
                            user_input = int(user_input)
                            if len(filteredUsers(engine, session, int(user_input), None, None, None, None, None)) != 0:
                                print("Valid user info.")
                                auth = passwordProtection(user_input) 
                                current_user = filteredUsers(engine, session, int(user_input), None, None, None, None, None)[0]
                            else:
                                print("Invalid username. Try again")
                        except:
                            print("Non numerical entered")
                            cont = False
                    if auth:
                        logged_in = True
                        displayOptions()
                        while(logged_in):

                            user_input = input("Enter your choice: ")

                            # View my activity history
                            if user_input == "1":
                                print(myActivities(current_user))
                                print("")
                            # View activities in my area
                            elif user_input == "2":
                                [print(a) for a in filteredActivity(engine, session, None, None, None, None, None, f"'{current_user.city}'", None)]
                                print("")

                            # Activities of specific type and area
                            elif user_input == "3":
                                city = input("city name: ")
                                a_type = input("type of activity: ")
                                [print(a) for a in filteredActivity(engine, session, None, None, None, None, f"'{a_type}'", f"'{city}'", None)]
                                print("")
                            
                            # set your favorite activity type
                            elif user_input == "4":
                                fave = input("Enter your favorite activity type: ")
                                updateUser(session, current_user.id, None, fave, None, None, None)
                                print("")
                            #get fave acts
                            elif user_input == "5":
                                [print(act) for act in getActivitiesByType(session, current_user.fave_type)]
                                print("")
                            
                            # New activity suggestion
                            elif user_input == "6":
                                my_act_ids = [act.activity_id for act in myActivities(current_user)]

                                print(random.choices(queryToList(session.query(Activity).filter(Activity.id.notin_(my_act_ids)))))
                                print("")

                            # #1 activity type in city
                            elif user_input == "7":
                                user_input = input("enter the city: ")
                                all_act_in_city = filteredActivity(engine, session, None, None, None, None, None, f"'{user_input}'", None)
                                all_act_in_city = [act.activity_type for act in all_act_in_city]
                                c = Counter(all_act_in_city)
                                print(c.most_common(1)[0][0], ": ",c.most_common(1)[0][1], " occurences")
                                print("")

                            # itinerary builder
                            elif user_input == "8":
                                user_input = input("destination city: ")
                                all_act_in_city = filteredActivity(engine, session, None, None, None, None, None, f"'{user_input}'", None)
                                desired_acts = input("desired activities (space separated with quotes): ")
                                counts = input("desired count of each activity (space separated no quotes): ")

                                counts_list = shlex.split(counts, posix=False)
                                desired_acts_list = shlex.split(desired_acts, posix=False)
                                itinerary = []
                                
                                for ind in range(0, len(desired_acts_list)):
                                    ls = filteredActivity(engine, session, None, None, None, None, desired_acts_list[ind], f"'{user_input}'", None)
                                    
                                    num_to_choose = int(counts_list[ind])
                                    if len(ls) < int(counts_list[ind]):
                                        num_to_choose = len(ls)
                                    chosen_list = random.choices(ls, k = num_to_choose)
                                    itinerary.extend(chosen_list)
                                
                                for ind in range(0, len(itinerary)):
                                    print(f"{ind+1}: ", itinerary[ind])
                                                                
                                print("")
                                pass
                            elif user_input == "help" or user_input == "9":
                                displayOptions()
                            else:
                                logged_in = False
                                print("back to user log in\n")
                elif user_input == "3" or user_input == "quit":
                    in_friendly = False
                    print("quitting user mode\n")
        
        elif mode == "quit":
            print("quitting....")
            in_prog = False
  

def getActivitiesByType(session, a_type):
    return session.query(Activity).filter(Activity.activity_type == a_type)

def myActivities(user):
    # session.query(Activity).filt
    return user.user_activities

# Easy human typeable filters

def filteredActivity(engine, session, id, name, duration, family, a_type, city, address):

    s = (f"SELECT * from activities WHERE {'' if (id == None) else 'activities.id = ' + str(id) + ' AND '}{'' if (name == None) else 'activities.name = ' + name +' AND '}"\
    f"{'' if (duration == None) else 'activities.duration = ' + str(duration) + ' AND '}{'' if (family == None) else 'activities.family_friendly = ' + family + ' AND '}"\
    f"{'' if (a_type == None) else 'activities.activity_type = ' + a_type + ' AND '}{'' if (city == None) else 'activities.city = '+ city +' AND '}"\
    f"{'' if (address == None) else 'activities.address = ' + address}")
    if s[-5:] == " AND ":
        s = s[:-5]
    if s[-6:] == "WHERE ":
        s = s[:-6]
    sql = text(s)
    # print("query:  ", s, "end query")
    
    
    
    with engine.connect() as conn:
        with conn.begin():   # Optional: start a transaction
            dic = conn.execute(sql).mappings().all()
    ind = []
    for entry in dic:
        ind.append(entry["id"])
    return [act for act in session.query(Activity).filter(Activity.id.in_(ind))]

def filteredUsers(engine, session, id, name, fav_act, age, city, address):

    s = (f"SELECT * from users WHERE {'' if (id == None) else 'users.id = ' + str(id) + ' AND '}{'' if (name == None) else 'users.name = ' +name +' AND '}"\
    f"{'' if (fav_act == None) else 'users.fave_type = ' + fav_act + ' AND '}{'' if (age == None) else 'users.age = ' + str(age) + ' AND '}"\
    f"{'' if (city == None) else 'users.city = '+ city +' AND '}{'' if (address == None) else 'users.address = ' + address}")
    if s[-5:] == " AND ":
        s = s[:-5]
    if s[-6:] == "WHERE ":
        s = s[:-6]
    sql = text(s)
    # print("query: ", s, "end query", sep ="")
    
    
    
    with engine.connect() as conn:
        with conn.begin():   # Optional: start a transaction
            dic = conn.execute(sql).mappings().all()
    ind = []
    for entry in dic:
        ind.append(entry["id"])
    return [u for u in session.query(User).filter(User.id.in_(ind))]


def filteredUserActivity(engine, session, id, user_id, activity_id):

    s = (f"SELECT * from users-activities WHERE {'' if (id == None) else 'users-activities.id = ' + id + ' AND '}{'' if (user_id == None) else 'users-activities.user_id = ' + user_id +' AND '}"\
    f"{'' if (activity_id == None) else 'users-activities.activity_id = ' + activity_id}")

    if s[-5:] == " AND ":
        s = s[:-5]
    if s[-6:] == "WHERE ":
        s = s[:-6]
    sql = text(s)
    # print("query:  ", s, "end query")
    
    
    
    with engine.connect() as conn:
        with conn.begin():   # Optional: start a transaction
            dic = conn.execute(sql).mappings().all()
    ind = []
    for entry in dic:
        ind.append(entry["id"])
    return [act for act in session.query(UserActivityHistory).filter(UserActivityHistory.id.in_(ind))]

def updateActivity(session, id, name, duration, family, a_type, city, address):    
    print("old: ",session.query(Activity).filter(Activity.id == id).first())

    session.query(Activity).filter(Activity.id == id).update({
        Activity.name: keepOrUpdateValue(Activity.name, name),
        Activity.duration: keepOrUpdateValue(Activity.duration, duration),
        Activity.family_friendly:keepOrUpdateValue(Activity.family_friendly, family),
        Activity.city: keepOrUpdateValue(Activity.city, city),
        Activity.address: keepOrUpdateValue(Activity.address, address),
        Activity.activity_type: keepOrUpdateValue(Activity.activity_type, a_type)
    })
    session.commit()
    print("updated: ", session.query(Activity).filter(Activity.id == id).first())
    print("")


def updateUser(session, id, name, fav_act, age, city, address):    
    print("old: ",session.query(User).filter(User.id == id).first())

    session.query(User).filter(User.id == id).update({
        User.name: keepOrUpdateValue(User.name, name),
        User.fave_type:keepOrUpdateValue(User.fave_type, fav_act),
        User.city: keepOrUpdateValue(User.city, city),
        User.address: keepOrUpdateValue(User.address, address),
        User.age: keepOrUpdateValue(User.age, age)
    })
    session.commit()
    print("updated: ",session.query(User).filter(User.id == id).first())
    print("")

def updateUserActivity(session, id, user_id, act_id):    
    print("old: ",session.query(UserActivityHistory).filter(UserActivityHistory.id == id).first())

    session.query(UserActivityHistory).filter(UserActivityHistory.id == id).update({
        UserActivityHistory.user_id:keepOrUpdateValue(UserActivityHistory.fave_type, user_id),
        UserActivityHistory.activity_id: keepOrUpdateValue(UserActivityHistory.city, act_id)
    })
    session.commit()
    print("updated: ",session.query(UserActivityHistory).filter(UserActivityHistory.id == id).first())
    print("")

def keepOrUpdateValue(original, new):
    if new == None:
        return original
    return new

def Noneify(ls):
    for ind in range(0, len(ls)):
        if ls[ind] == "$":
            ls[ind] = None
    return ls

def displayTechnicalOptions():
    print("the options")
    print("create, delete, update, read, help, exit")
def displayOptions():
    print("view my activities (1), activities in my area (2), activities of type in city (3), set favorite activity tyoe (4), \
          activities that are my favorite (5), new suggested activity (6), most common activity in city (7), itinerary builder (8), [help] (9), exit")

def passwordProtection(user):
    print("No password implementation at moment")
    return True
def queryToList(q):
    return [u for u in q]

main()
# specialSplit("hello and 'hey there' king")
# print(shlex.split("help     me 'dad dad'"))