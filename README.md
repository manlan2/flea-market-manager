# Flea Market App

Code to implement a online flea market management app as part of [Udacity's](https://www.udacity.com) Full Stack Web Developer Nanodegree.

[Project Guide](https://docs.google.com/document/d/1jFjlq_f-hJoAZP8dYuo5H3xY62kGyziQmiv9EPIA7tM/pub?embedded=true)

## Table of Contents
* [Files](#files)
* [How To Run](#how-to-run)
* [Loading Test Data](#loading-test-data)
* [Python Code Testing](#python-code-testing)
* [JSON API](#json-api)
* [Turning Off Debug Mode](#turning-off-debug-mode)

## Files

* **db_model.py** - This file contains the database model with three tables.

* **application.py** - This file is the main program used to create the flea market app.

* **templates/** - This directory contains the HTML templates used to render the app.

* **static/** - This directory contains contains a CSS file.

* **main.css** - This is the CSS file used to tweak the look of the app.

* **test_data.sql** - This file contains test data used to develop the app.


[Back to Top](#flea-market-app)


## How To Run

The code for this project can be run inside the Udacity Vagrant VM.  Additional steps are required to run the app in a stand alone environment.

### Udacity Vagrant VM

Follow the guide found [here](https://www.udacity.com/wiki/ud197/install-vagrant) to install and run the VM.

### Installation
* Download the ZIP by clicking on the link on the right side of this page.
* Extract the archive and copy the files to a directory inside the vagrant directory.
* Open your terminal application if you haven't already and navigate to the directory you copied the files to.
* Start the app with ```python application.py```

**OR**

* Clone the repository inside the vagrant directory.

 ```
 git clone https://github.com/larrytooley/Udacity-FSND2015-P3.git fleamarket
 ```

* Move to the directory containing **application.py**.

 ```
 cd Udacity-FSND2015-P3/
 ```

* And start the app.

  ```
    python application.py
  ```

[Back to Top](#flea-market-app)

## Loading Test Data

To create and test the database, you will need to edit **test_data.sql** and run the following commands in **SQLite**:

* In order to modify the exist booths and items, you will need to change line 9 in **test_data.sql** to include your name and the email associated with the Google account you intend to log in with or you can delete the line all together and the first account to login will control the existing data.

```
INSERT INTO user (name, email, picture) VALUES ("Your Name", "you@somegmail.com", "");
 ```

* Start the SQLite command line tool, **sqlite3**.

```
vagrant fleamarket $ sqlite3 fleamarket.db

SQLite version 3.8.4.1 2014-03-11 15:27:36
Enter ".help" for usage hints.
sqlite>
```

* Import the **test_data.sql** file containing the test data set.

```
sqlite> .read test_data.sql
```

* Exit **SQLite**.

```
sqlite> .exit
```

[Back to Top](#flea-market-app)

## Python Code Testing

As stated in the project specification, you should be able to add, change, and delete existing items and booths as long as you are logged in and the owner of the booth. The owner of the existing booths and items is the user with the id of 1 in the user table.  This is can be set prior to loading the test data by editing line 9 of the **test_data.sql** file.

* Test access to existing items and booths without logging in.
  * On the main page you should not see a green "Create a Booth button".

  * You should not see any buttons on the individual booth or item pages to add, edit, or delete booths or items.

  * Any attempt to access CRUD functionality for any items or booths directly through urls should be routed to the login page.

* Test access logged in as a user without access to the existing items and tables.
  * A green "Create a Booth" button should be visible on the main page.

  * You should not see any buttons on the individual booth or item pages to add, edit, or delete booths or items.

  * Any attempt to access CRUD functionality for any items or booths directly through urls should result in a JavaScript dialog box warning that you do not have rights to those items.

  * You should be able to create a new booth and add, edit, or delete items from that booth.

  * New items should appear at the top of the "Newest Items" list on the main page.

* Test functionality as the owner of the existing items and booths.
  * You should be able to add, edit, or delete items from your existing booths.

  * Any attempt to access CRUD functionality for any items or booths directly through urls should result in a JavaScript dialog box warning that you do not have rights to those items.

* Test for code injection attacks.
  * Test for HTML injection in text inputs. Should result in raw HTML appearing in the updated or created item. I tested this by changing the name of an item to ```<h1>Bad!</h1>```.

  * Test for JavaScript injection into form elements. Should result in raw JavaScript appearing in the updated or created item. I tested this by changing the description of an items to ```<script>alert('Bad!');</script>```.

  * Test for SQL injection into form elements. Should result in raw SQL appearing in the updated or created item. I tested this by changing the description of an items to ```Robert'); DROP TABLE items;--```.

[Back to Top](#flea-market-app)

## JSON API

JSON can be retrieved at the following endpoints:
* ```localhost:8000/items/json```
* ```localhost:8000/booth/booth_id/json```
* ```localhost:8000/booth/booth_id/item_id/json```

[Back to Top](#flea-market-app)

## Turning Off Debug Mode

Prior to deploying the app in a production environment, be sure to turn off the debug mode.

* Go to line 485 the **application.py** file.
* Delete ```debug='True', ```.
* Unless otherwise desired, remove ```, port=8000``` as well.

[Back to Top](#flea-market-app)
