#### Getting the files
<ol>
<li>Download zip file</li>
<br>
<li>Create a new folder to extract the project zip file into it</li>
<br>
<li>Extract the project files into the crated folder.</li>
<br>
##### For Example folder was created on Desktop with name "project" then extract files to "project" folder
<br><br>
## Setup
#### - Change Working Directory to "project" folder
Open Command Prompt and execute following commands:
```
cd <project_folder_path>
```

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
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```
##### While creating superuser i.e. executing last step, remember the USER_EMAIL AND PASSWORD, because the superuser acts as admin to the Django app and can be used to monitior application data by using below URL after running application (will be seen in next step):
###### # URL
```
http://localhost:8000/admin
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


