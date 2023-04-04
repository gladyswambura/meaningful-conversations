# meaningful-conversations

Meaningful Conversations is a social networking web application that allows people from around the globe to create and join rooms to talk about various topics that matter. This project is built using Django-Python.

## AUTHOR 
**Gladys Wambura**

## DESCRIPTION
- Meaningful Conversations is a web application that allows people to create rooms and have conversations with others around the world on topics that matter.
- Users can sign up and log in to the web application.
- Users can create rooms with different topics and descriptions.
- Users can join and leave different rooms.
- Users can view and comment on conversations in different rooms.
- Users can search for rooms based on topics.
- Users can view the number of people who have joined a room.

- ![image](https://user-images.githubusercontent.com/97955649/229700729-888f58d4-0151-4c6c-b8e6-26d77f67221f.png)


## FEATURES && USER STORY 
As a user of Meaningful Conversations, you will be able to:
- Sign up and log in to the web application.
- Create rooms with different topics and descriptions.
- Join and leave different rooms.
- View and comment on conversations in different rooms.

# **SETUP/INSTALLATION.**

# Prerequisites
-python3.6
-virtual environment
-pip

*** To view the app.Visit -> [meaningful-conversations](https://github.com/gladyswambura/meaningful-conversations)

1. Clone this repo: git clone https://github.com/gladyswambura/meaningful-conversations
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create Postgres database conversations using the command below.


       CREATE DATABASE conversations; 
       **if you opt to use your own database name, replace awwards your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       python3 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


# Technologies Used

* Python 3.6
* Django
* Postgresql
* Bootstrap4


## Known Bugs  
* There are no known bugs currently && pull requests are allowed.
  

  ## Contact Information   
If you have any question or contributions, please email me at [gladyswahito7@gmail.com]  


## live link 
https://gladysneighborhood.herokuapp.com/

## License
This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.
