# API Handling in Python

> *You can't call your well versed in any programming language unless and until you have mastered handling APIs in that language.*
>**- Hitesh Choudary sir** 

- we will be taking API responses from Hitesh sir & Team's own [freeAPI website](https://api.freeapi.app/#/%F0%9F%93%A2%20Public%20APIs/getUsers) which provides us with many free API responses.
- To understand what the responses are coming as we can use the json formatter websites like [JSON formatter](https://jsonformatter.org/) 
- Even firefox has it's own formatter just paste the api url in a new tab.

---

# Web requesting in Python 

- Python on it's own doesn't have web requests capabilities.
- Hence we will be using 3rd party package : [requests](https://pypi.org/project/requests/).
- installation 
```cmd
pip install requests
``
- Problem with 3rd party packages is that when another user will try to use your application, it will not run cause he might not have the necessary packages installed. (Will tackle this problem in the future...)
