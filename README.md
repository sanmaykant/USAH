# Instructions
- cd into the repo.
```shell
cd USAH
```
- Create a python virtual environment and activate it.
```shell
python -m venv env
.\env\Scripts\Activate.ps1
```
- Install requirements.
```shell
pip install -r .\requirements.txt
```
- Add a `.env` file in the USAH folder in the following format.
```.env
DB_NAME=name
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
```
- Create super user
```shell
python manage.py createsuperuser
```
- Run server
```shell
python manage.py runserver
```
