# Puzzled Escape Room

- [Puzzled Escape Room](#puzzled-escape-room)
  - [Introduction](#introduction)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Features To Be Implemented](#features-to-be-implemented)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks \& Liabraries](#frameworks--liabraries)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Cloning the Repository](#cloning-the-repository)
    - [Creating an Application and Postgres Database on Heroku](#creating-an-application-and-postgres-database-on-heroku)
    - [Configuring Cloudinary for hosting the application's images](#configuring-cloudinary-for-hosting-the-applications-images)
    - [Linking the Heroku application to the GitHub repository](#linking-the-heroku-application-to-the-github-repository)
    - [Executing the final deployment steps](#executing-the-final-deployment-steps)
  - [Credits](#credits)

## Introduction

## User Stories

## Features

## Features To Be Implemented

## Technologies

### Languages

- [HTML5](<https://en.wikipedia.org/wiki/HTML5>)
- [CSS3](<https://en.wikipedia.org/wiki/CSS>)
- [Python](<https://www.python.org/>)

### Frameworks & Liabraries

- [Google Fonts](https://fonts.google.com/) was used for Ubuntu and Edu SA Beginner
- [Font Awesome](<https://fontawesome.com/>) was used for icons
- [Codeanywhere](<https://codeanywhere.com/>) was utilized for version control, enabling commits to Git and subsequent pushes to GitHub.
- [GitHub](<https://github.com/>) project code is stored in a repository after being pushed from Git. Moreover, GitHub served as a platform for the agile development process in this project, specifically through the implementation of User Stories via GitHub Issues
- [Heroku](<https://id.heroku.com/login>) project was deployed using this platform
- [Django](<https://www.djangoproject.com/>) platform served as the framework that facilitated the swift and secure development of the application
- [Bootstrap](<https://getbootstrap.com/>) tool was utilized to construct responsive web pages
- [Gunicorn](<https://gunicorn.org/>) software acted as the web server, enabling Django to run on Heroku
- [ElephantSQL](<https://www.elephantsql.com/>) served as the database for this project
- [dj_database_url](<https://pypi.org/project/dj-database-url/>) library facilitated the connection between database URLs and the PostgreSQL database
- [psycopg2](<https://pypi.org/project/psycopg2/>) database adapter was utilized to enable the connection to the PostgreSQL database
- [Cloudinary](<https://cloudinary.com/>) service was employed for storing the images utilized by the application
- [Django allauth](<https://django-allauth.readthedocs.io/en/latest/index.html>) platform was utilized for account registration and user authentication

## Testing

## Deployment

Outlined below are the comprehensive instructions for cloning this project repository, along with the guidelines to configure and deploy the application. A condensed version of the deployment process is made available by the Code Institute: CI Cheat Sheet and within the walkthrough project.

1. [Cloning the Repository](#Cloning the Repository)
2. [Creating an Application and Postgres Database on Heroku](#Creating an Application and Postgres Database on Heroku)
3. [Configuring Cloudinary for hosting the application's images](#Configuring Cloudinary for hosting the application's images)
4. [Linking the Heroku application to the GitHub repository](#Linking the Heroku application to the GitHub repository)
5. [Executing the final deployment steps](#Executing the final deployment steps)

### Cloning the Repository

- Visit the repository [Puzzled Escape Room](https://github.com/Ellusive89/puzzled-escape-room) on GitHub
- To the right of the screen, click on the "Code" button. Switch to the HTTPs section and copy the provided link.
- Launch a GitBash terminal and navigate to the directory where you intend to create the clone.
- On the command line, enter ```git clone```, paste the previously copied URL, and press the Enter key to initiate the cloning process.
- After cloning, install the necessary packages for the application by typing ```pip install -r requirements.txt```
- If you are developing and running the application locally, set ```DEBUG=True``` in the **settings.py** file.
- Any changes made to the local clone can be committed back to the repository with these commands:
  - ```git add [filenames]``` ,or use ```git add .``` to add all changed files
  - ```git commit -m "a descriptive message about changes"```
  - ```git push```
Note: Any changes pushed to the main branch will reflect on the live project after re-deployment from Heroku.

### Creating an Application and Postgres Database on Heroku

- Visit [Heroku](https://www.heroku.com/) and log in, or create a new account if necessary
- From the Heroku dashboard, click the **Create new app** button. If you have a new account, an icon will be displayed on the screen to **Create an app**, or find this option under the **New** dropdown menu at the top right of the screen
- On the **Create New App** page, provide a unique name for the application, select a region, and click **Create app**
- On the **Application Configuration** page for your new app, click on the **Resources** tab
- In the **Add-ons** search bar, type **Postgres** and select **Heroku Postgres** from the dropdown list. Then, click the **Submit Order Form** button in the pop-up dialog
- Go back to **Settings** on the **Application Configuration** page and click on the **Reveal Config Vars** button. Ensure the ```DATABASE_URL``` has been set up automatically
- Add a new Config Var named ```DISABLE_COLLECTSTATIC``` and set its value to 1
- Create another Config Var named ```SECRET_KEY``` and assign it a value. This can be any random string of letters, digits, and symbols
- Update the **settings.py** file to use the ```DATABASE_URL``` and ```SECRET_KEY``` environment variable values
- In Gitpod, within the project terminal window, initialize the data model in the Postgres database by running the command: ```python3 manage.py migrate```
- Make sure the project's **requirements.txt** file is updated with all necessary supporting files. Enter the command: ```pip3 freeze --local > requirements.txt```
- Commit and push any local changes to GitHub
- To run the application on localhost, add ```SECRET_KEY``` and ```DATABASE_URL``` along with their respective values to the **env.py** file

### Configuring Cloudinary for hosting the application's images

- Visit [Cloudinary](https://cloudinary.com/) and log in, or create an account if necessary. During account creation, provide your name, email, and a password. For **primary interest**, select **Programmable Media for image and video API**. After clicking **Create Account**, you'll receive an email to verify your account, which will redirect you to the dashboard
- From the dashboard, click on the **Copy to clipboard** link to copy the **API Environment variable** value
- Log into [Heroku[(<https://www.heroku.com/>) and navigate to the **Application Configuration** page for your application. Click on **Settings** and then click on the **Reveal Config Vars** button
- Add a new Config Var named ```CLOUDINARY_URL```. Paste the value copied from the Cloudinary dashboard, but remember to remove the ```CLOUDINARY_URL=``` prefix from the string
- To enable the application to run on localhost, add the ```CLOUDINARY_URL``` environment variable and its value to your **env.py** file

### Linking the Heroku application to the GitHub repository

- Visit the **Application Configuration** page for your application on Heroku and click on the **Deploy** tab
- Choose **GitHub** as your Deployment Method. If requested, confirm the connection to GitHub. Enter the name of your GitHub repository and click **Connect**. This will link the Heroku app with the code in your GitHub repository
- Scroll down to the **Automatic deploys** section. Here, you can opt to either **Enable Automatic Deploys**, which will deploy every time changes are pushed to GitHub, or use the **Manual Deploy** option. For this project, select **Manual Deploy**
- You can now run the application directly from the **Application Configuration** page by clicking on the **Open App** button

### Executing the final deployment steps

- In the **settings.py** file, set the ```DEBUG``` flag to ```False```
- Make sure that **requirements.txt** is up-to-date. You can use the command ```pip3 freeze --local > requirements.txt``` to achieve this
- Push your files to GitHub
- In the **Heroku Config Vars** for the application, delete the ```DISABLE_COLLECTSTATIC``` environment variable
- Visit the **Heroku dashboard** and navigate to the **Deploy** tab for your application. Click **Deploy Branch** to initiate the deployment

After completing these steps, the application will be live. You can access the deployed application at this link: [Puzzled Escape Room](https://github.com/Ellusive89/puzzled-escape-room)

## Credits
