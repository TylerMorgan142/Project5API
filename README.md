# Testing

All apps have been manually tested and are all functional

    Comments can be successfully created

    A specific users followed profiles and number of followed profiles can be viewed successfully

    All likes are visible and show the all the releveant information related to the likes

    The Album list can be viewed and shows all the releveant information related to the albums

    Each albums detail can be viewed as well

    The Review list can be viewed and shows all the releveant information related to the Review

    Each reviews detail can be viewed as well

    The Posts list can be viewed and shows all relevant information related to the Post

    Each posts detail can be viewed as well

    The Profiles list can be viewd and shows all relevant information related to the profile

    Each profile detail can be viewed as well

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
