<div align="center" class="row">
  <img src="https://dummyimage.com/300x300/ff8000/0011ff&text=HMS" width="200"/>
</div>
<h3 align="center">Backend App for Hostel Management System</h3>
<br>


### Technologies used

* Flask
* MSSQL

### Steps to run the application

1. `cd hostel_management_system`
   
2. `pip3 install -r requirements.txt` (only for the first time)

3. Do `python make_table.py` (only for the first time)

4. DO `python app.py`

3. Add or Edit the routes and functions in the file run_model.py

### Testing the API

1. Locally, eg: http://localhost:3434/status
2. Test the API with POSTMAN. 

Example for GET boarderS : 

* Set the URL TO `http://localhost:3435/api/get_all_boarders` to get all the boarders (DO GET).
* Set the URL TO `http://localhost:3435/api/get_boarder/` to get a boarder for an email (DO POST).


Example input for ADD BOARDERS (POST):
* Set the URL TO `http://localhost:3435/api/add_boarders`

INPUT:
```json
    {
    "name":"Subhasish Goswami",
    "image":"https://asdasdasd/asdasd.png",
    "email":"asdasdasd@gmail.com",
    "phone":"100123123",
    "gtoken":"123981239127317237"
    }
```

Example input for UPDATE boarderS :
* Set the URL TO `http://localhost:3435/run_model/update_boarders` to Update Single Record 

INPUT:
```json
    {   
        "api_key":"Enter API key for successfull operation",
        "email":"asdasdasd@gmail.com",
        "name": "Upam Sarmah"
    }
```
Example input for DELETE boarderS :
* Set the URL TO `http://localhost:3435/run_model/delete_boarders` to Delete boarder Record

INPUT:
```json
    {

        "api_key":"Enter API key for successfull operation",
        "email":"asdasdasd@gmail.com"
    
    }
```

<hr>

### Authors

##### [Adittya Dey](https://github.com/adiXcodr) 
