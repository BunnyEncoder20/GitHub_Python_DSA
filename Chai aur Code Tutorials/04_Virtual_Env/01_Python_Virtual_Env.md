# Python Virtual Environment 

--- 

- As we had seen earlier, certain 3rd party apps had to be installed when we were making python projects.
- It is **not** recommended to pip install packages directly into your base python installation 
- We should try to keep that to a minimum
- Instead we should create a **virtual environment** for projects and install all the required packages there.
- For any project, we can mention all the required packages needed to run the project in a `requirements.txt` file.
- The virtual environment keeps the packages separate from the base python installation and our base machine.
- Python Virtual Env comes with a base python installation and pip to install other packages.

<br>

>- Think of VM as a separate machine inside your machine (completed isolated from your base computer).

## 1. Creating a PVM from package `virtualenv`

- There are man ways to create a virtual environment of python. The most common (industry wise) is using the package `vitualenv`
- Documentation: [Link](https://virtualenv.pypa.io/en/latest/)
- Installation : 
```
pip install virtualenv
```
- This will create a new computer (folder) inside the dir with a basic python and pip installation


<br>

- To create a python virtual environment folder :
```
python -m venv env_name
```
- **OR**
```
python -m virtualenv env_name
```
- Where env_name is the name of your virtual environment 
- This will create a folder called `env_name` inside the current dir.
- Read Documentation : [Link](https://docs.python.org/3/library/venv.html)

---

## 2. Activating the Virtual Environment

- to activate the virtual environment **on windows:**
```
.\env_name\Scripts\activate
```
- If the `venv` activated correctly, you'll see that your terminal dir will have a `(.venv)` at the beginning of it.
```
(.venv) PS C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\04_Virtual_Env>
```
- to deactivate the virtual environment:
```
deactivate
```

--- 

## 3. Installing packages in PVM and generating `requirements.txt`

- You can install packages in the virtual environment using the pip command like normal :
```
pip install pymongo
```
- We can also install frameworks like Django: 
```
python -m pip install django
```
- We can develop our project in that folder and at the end, we can generate a `requirements.txt` which will list all the packages needed to run the project.
```
pip list > requirement.txt
```
- pip list gets us the list of all the installed packages and there versions. 
- That list will be stored into  `requirement.txt` file (outside the .env_name folder).
- The above command can also be used to update the requirement.txt list
- We can then **install** those packages using a single command
```
pip install -r requirements.txt
``` 
- You can also uninstall packages like normal : 
```
pip uninstall pymongo
```