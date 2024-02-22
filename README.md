# Testing

## Manual Testing

### Comments

    An admin is able to delete comments

    If a logged in user enters the /comments url, the comment list renders all comments as an array of objects

    A logged in user is able to create comments and the array is updated

    A logged in user can enter the url for a speicific comment using the comments id,
    If they own the comment they can update and delete the comment

    If a user updates the comments data, the change is saved in the database

### Profiles

    An admin is able to delete profiles
    
    A user is able to create a profile

    If a logged in user enters the /profiles url, the profile list renders all profiles as an array of objects

    A logged in user can enter the url for a specific profile using the profiles id,
    If they own the profile they can update and delete it

    If a user updates a profiles data, the change is saved in the database



 ### Posts

    An admin is able to delete posts
        
    A logged in user is able to create a post

    If a logged in user enters the /posts url, the posts list renders all posts as an array of objects

    A logged in user can enter the url for a specific post using the posts id,
    If the user owns the posts they can update and delete it

    If a user updates a posts data, the change is saved in the database

### Likes

    A logged in user is able to like a post

    If a logged in user enters the /likes url, the like list renders all comments as an array of objects
    
    A logged in user can enter the url for a specific like by using the likes id

    If a user likes a post the like is saved in the database


### Followers

    A logged in user is able to follow other users

    If a logged in user enters the /followers url, the follower list renders all follower data as an array of objects

    A logged in user can enter the url for a specific follower by using the follower id

    If a user follows another user it is saved in the database

### Albums

    An admin is able to create,update and delete albums

    If a logged in user enters the /albums url, the album list renders all albums as an array of objects

    A logged in user can enter url for a specific album by using the albums id

    If an album is created, updated or deleted the it is saved in the database

### Reviews

    An admin is able to delete reviews

    A logged in user is able to create a review

    If a logged in user enters the /reviews url, the reviews list renders all reviews as an array of objects

    A logged in user can enter the url for a specific review using the reviews id,
    If the user owns the review they can update and delete it

    If a user updates a reviews data, the change is saved in the database

    
# Deployment

This project was deployed to Heroku at [this location](https://metalhub-api-7e3be8a93e64.herokuapp.com/)

The steps for deployment are as follows:

1 Sign up for Heroku

2 Go to the dashboard and create a new app

3 Give the app a name and assign it a region, then click "create app".

4 Navigate to the settings tab of the app and click "Reveal Config Vars"
        
        The app requires the following Config Vars

        CLIENT_ORIGIN
        CLIENT_ORIGIN_DEV
        CLOUDINARY_URL
        DATABASE_URL
        DISABLE_COLLECTSTATIC
        HEROKU_POSTGRESQL_MAROON_URL
        SECRET_KEY


5 In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database

     pip3 install dj_database_url==0.5.0 psycopg2


6 Create a variable in Env.py that is assigned a value of a database URL, this projects database is hosted on ElephantSQL

        os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"

7 In the settings.py file add the following code
     
    if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
    else:
         DATABASES = {
             'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
         }


8 Navigate to the "Deploy" tab and select Github as the deployment method.

9 Choose the repository to be deployed, you can also choose to enable automatic deployment.

10 At the bottom of the Deployment page click "Deploy Branch"

11 Once the app is deployed, click the "Open app" button in the Heroku dashboard to view the live application.
