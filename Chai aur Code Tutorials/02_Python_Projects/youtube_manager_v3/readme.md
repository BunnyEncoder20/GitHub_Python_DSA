# Python Project : Youtube Manager v3.0

--- 

## Description
- This version of the Youtube Manager runs in the terminal 
- Deals with all the `CRUD` operations
- Saves the data to a MongoDB database

### MongoDB

- yes mongoDB can be used with many other tech stacks other than MERN/MEAN for web development 
- after creating a new project, database and user, we can finally connect to our new MongoDB Project : Personal Projects : 01-PythonProjects-DB (details in .env file only)

<br>

- we can connect and interact with a mongoDB database using the pymongo library
- Installation : 
```
pip install pymongo
```
- we still have that problem of 3rd party packages that might cause error when other people try to run the same code. (Will discuss that in next video)

### `.env` variables handling in Python

- we do not want to send out credentials to github which is a public repo. 
- So such secrets are kept in a `.env` file in the project directory.
- In order to use those `env` vairables we will need the `python-dotenv` library
- Installation : 
```
pip install python-dotenv
```
- Usage example : 
```python 
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
print("Secret: ",os.getenv("secret_key"))
```