#### Video Tutorial for this project
https://youtu.be/SQ4A7Q6_md8
<br><br>

#### Packages

Django                5.2.4<br>
django-allauth        65.9.0<br>
django-browser-reload 1.18.0<br>
django-cleanup        9.0.0<br>
django-htmx           1.23.2<br>
pillow                11.3.0<br>

<br><br>


#### Getting the files
Download zip file<br> 
or <br>
git clone command (need git to be installed) and remove git folder afterwards
```
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git
```
<br><br><br>

## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv venv
(Powershell:) .\venv\Scripts\Activate.ps1
```
```
(or Command Prompt:) venv\Scripts\activate 
(or Git Bash:) source venv/Scripts/activate
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```


