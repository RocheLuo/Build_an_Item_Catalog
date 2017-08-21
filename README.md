# Build_an_Item_Catalog
Build_an_Item_Catalog is the 4th project for Full Stack Web Developer course.

## Enviorment

### Python
In order to run the program, you should have the environment for **Python 3**.
You can install python3.7 by downloading files from [Python.org](https://www.python.org/getit/) 

### Module-flask
The python program import flask module to build up the whole app. In order to run the program properly, you should install **flask** at first

You can install **flask** with the code ```pip3 install flask```

### Module-sqlalchemy
The python program import sqlalchemy module to connect and manipulate the database. In order to run the program properly, you should install **sqlalchemy** at first

You can install **sqlalchemy** with the code ```pip3 install sqlalchemy```

### Module-oauth2client
The python program import oauth2client module to help using google's OAuth . In order to run the program properly, you should install **oauth2client** at first

You can install **oauth2client** with the code ```pip3 install oauth2client```

### Data - item.db
The data used in this project is already in the respository ,named **item.db**. You can also add the origianl data by running code ```python3 lotsofitem.py```

### Localhost - port =5000
The project will run on **localhost:5000** . If the 5000 port have been used, you can change the port in ```project.py``` in the end of the code.

## How to use
### Run The Program
1. **Make sure you have item.db and database_setup.py in the same file with projcet.py**
2. **Make sure you have download templates file and static file, which insure the web can be displayed correctly**
3. Then use the comand ```python3 projcet.py```, it will start the localhost of 5000. and you can visit the website by visiting **http://localhost:5000/**. if the 5000 port have been used, you can change the port in "project.py" in the end of the code.

### API
You can get the data by visiting **http://localhost:5000/catalog/JSON**

### Add/Delete/Edit data
You can add/delete/edit the data once you have login by google's OAuth conncetion.

## Document

### project.py
This file can start the app and localhost.

### database_setup.py
This file setup the item.db. But you do not need to run it once you have **item.db** in your file.

### lotsofitems.py
This program can fill in the database with some data. You will not need to run it unless you have deleted **item.db**.

### templates file
In the file ,there are the basic html templates for the app.

### static file
In the file ,there are css file and favicon for the app. The favicon I used is udacity's.

