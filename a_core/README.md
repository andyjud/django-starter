## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
pip install virtualenv 
virtualenv venv 
venv\Scripts\activate.bat 
```

<br>

#### - Install dependencies
```
pip install -r requiremenets.txt
```

#### - Get Secret Key
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

#### - Run application
```
python manage.py runserver
```
#### - Migrate to database
```
python manage.py migrate
```
#### - Start App
```
python manage.py startapp app_name
```


admin.site.register(Message)
admin.site.register(Conversation)
```

