# Project Management Dashboard 


*This project will test your ability to program with Python using the Django Framework.*

*As much as you can, make sure the code is neatly written, well commented and adequately optimised.*

## Create App
Create a Django project called project-dashboard: 
## I created the project as ProjectDashboard because Django no longer supports the names with hyphens.

Create an app called "dashboard".

## Create Models:
* Declare a `Team` model class with `name`, `title`, `description` and `image`. 
## I created a Team model with a many to many field with the built-in django User model and then created a UserImage model to store the user pictures.

* In the `dashboard` app, create a model class called `Project`.
* In the `Project` model, declare the following fields; `title`, `timestamp`, `activity-list`, `team`. (the team will be a `foreign` key to the `Team` model class).
## I created an Activity Model with a many to many relationship

* Create a superuser called `admin` and the project data from the static template provided. 

* ## username: admin
* ## password: pass1234

## Create Views:
* Create a `dash_board` view that will display the models dynamically on the template. 
* Display 6 main projects 
* Display 4 recent projects below the charts


## Submission:
* Push to a GitHub repository 
* Send the repo link to skills@instincthub.com
