#### Video Tutorial to build this project
https://youtu.be/SQ4A7Q6_md8
<br><br>


#### Getting the files
Download zip file<br> 
or with<br>
git clone command
```
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git
```
<br><br>


## Setup with UV (Recommended)


##### Install UV
uv: https://docs.astral.sh/uv/ 
```
pip install uv
```

##### Install dependencies
```
uv sync
```

##### Migrate to database
```
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py createsuperuser
```

##### Run application
```
uv run manage.py runserver
http://localhost:8000
```

<br><br>


## Setup with with pip

##### Create Virtual Environment on Mac
```
python3 -m venv .venv
source .venv/bin/activate
```

##### Create Virtual Environment on Windows
```
python3 -m venv .venv
.\venv\Scripts\Activate.ps1
```

##### Install dependencies
```
pip install -r requirements.txt
```

##### Migrate to database
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

##### Run application
```
python manage.py runserver
http://localhost:8000
```