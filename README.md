#### Video Tutorial to build this project
https://youtu.be/SQ4A7Q6_md8
<br><br>

#### BE AWARE: UPDATES FROM THE OLDER VERSION
- Now uses the CustomUser Model instead of Django's default User<br>
- In models get the User with "from django.conf import settings" and "author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)"
- In views get the User with "from django.contrib.auth import get_user_model" and "User = get_user_model()"
- No more Profile table, all users properties are now in the Users table, that means instead of {{ message.author.profile.name }} use {{ message.author.name }}, no more profile needed
  
- send_confirmation instead of send_email_confirmation (remove the = in the email verification link sent to the terminal)<br>
- Project Title was moved to the settings.py file _core > settings.py > PROJECT_TITLE
- Option to use UV for Dependency Management<br>
<br><br>


#### Getting the files
Download zip file<br> 
or<br>
run git clone command in empty folder
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

##### Activate Virtual Environment (Mac)
```
source .venv/bin/activate
```

##### Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

##### Run application
```
python manage.py runserver
```
http://localhost:8000

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
pip install --upgrade pip
```

##### Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

##### Run application
```
python manage.py runserver
```
http://localhost:8000
