a.	Instructions for running your project

    Run python seed.py, then run python main.py. Make sure you are in appropriate python environment (pipenv shell). 

b.	An overview about what your project is about

    My project allows for the keeping track of different users and different activities. Each user has their id, name, city, address, fave_type, age, and each activity has their id, name, duration, family_friendly, activity_type, city, address. 

    A join table also exists which keeps track of the activities a user has done.

    In admin mode, full CRUD can be done from CLI, with guidance on what to type for each CRUD operation and simplified typing for admin (dont type raw SQL).

    In user mode, we have more user oriented operations that can give info about user and their activities, as well as allowing users to get suggestions on new activities to do, or building a list of activities to do in a city, or seeing the most common kind of activity in a city.

    Options on what to do are either selected numerically or by entering key word. Info on what prompt does what are given on start up and entering a different mode, and can be requested again by typing help or the corresponding number, depending on where you are in program. 

c.	Instructions for using your project
Upon entering the project, you will have choice of admin mode, user mode, or quitting.

    - Admin
    Full CRUD. Start by choosing what CRUD operation, then what table. Then enter the appropriate info according to the prompt given

    - User

    To start you will be asked if you are a new or returning user. New user is not implemented but would allow for creation of User entry to table
    Returning user takes a user id, and then logs you in. Currently there is no password support, but there is a placeholer function as of the moment
    Once logged in, All options are displayed on starting and can be redisplayed with help command. 

    Some interactions here include changing their favorite activity type, or getting suggested new activities. Options are selected numerically, with the 
    starting prompt and help command telling you what number corresponds to what command. 

    Quitting from Admin mode or User mode will bring you back to the mode selection, and quitting here exits program