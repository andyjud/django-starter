#### Video Tutorial to build this project
https://youtu.be/SQ4A7Q6_md8
<br><br>


#### Getting the files
Download zip file<br> 
or with<br>
git clone (and remove git folder afterwards)
```
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git
```
<br><br><br>


## Setup

#### Install Dependencies with uv (Recommended)
uv: https://docs.astral.sh/uv/ 
pip install uv

##### Install dependencies
uv sync

##### Migrate to database
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py createsuperuser


#### Install Dependencies with pip
###### # Mac
```
python3 -m venv .venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv .venv
(Powershell:) .\venv\Scripts\Activate.ps1
```

<br>

#### - Install dependencies
```
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

<br>


#### - Run application
```
python manage.py runserver
http://localhost:8000
```




