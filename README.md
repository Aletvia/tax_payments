tax_payments
# APY tax payments
API Rest which implements a tax payment service provider.

## Installation
Requerimientos:
- Entorno virtual (venv)
- Python 3.7, pip

### Entorno de Desarrollo

This environment let ​make changes in the API. Follow the next steps:

1. Create virtual environment (_venv_)
```shell script 
virtualenv venv
```
2. Activate virtual environment
```shell script
source venv/bin/activate
```
3. Packages install
```shell script
(venv) pip install -r PATH/requirements.txt
```

With these steps we generate access to the libraries necessary for the development of the project.

1. It is necessary to carry out the corresponding migrations, execute the following command in the terminal within the same folder:
```shell script
python src/manage.py makemigrations
python src/manage.py migrate
```
2. To run the API tests, run the following command in the terminal within the same folder:
```shell script
src/manage.py test src
```
3. If everything is fine, you can see the API response in OK



**Endpoints available:**

- List of all payables, filtered by payment status or service type.
GET: http://127.0.0.1:8000/api/v1/payables/filtered_by/filter/

- List of total amounts and transactions per day filtered by a period of time.
GET: http://127.0.0.1:8000/api/v1/transactions/start_date/end_date/

- Create a new payable.
POST: http://127.0.0.1:8000/api/v1/payables/

- Create a new transaction.
POST: http://127.0.0.1:8000/api/v1/transactions/

