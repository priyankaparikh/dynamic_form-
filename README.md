![](dynamic_form.gif)

to run this program clone the repository and in a python 3 environment or shell

```pip install -r requirements.txt```

Do this from the root repository 

```python server.py```

Improvements : 

1) we could hook this up to a nosql db because this a dynamic form with the fields changing often. With a sql db we may have to keep adding new columns which may mean having to replicate tables (creating and dropping often)
2) Data would be in a separate file.