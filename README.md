#### online-order

```
➜  online-order git:(master) conda info --envs
# conda environments:
#
base                  *  /Users/shaytac/miniconda2
myenv                    /Users/shaytac/miniconda2/envs/myenv
py27                     /Users/shaytac/miniconda2/envs/py27
sci                      /Users/shaytac/miniconda2/envs/sci
                         /Volumes/Data/Users/shaytac/anaconda2/envs/sci

```
#### Create env if not there
```
conda create --name online-order python=3
```

#### To activate env 
```

```

#### To deactivate env 
```
source deactivate online-order
```

#### To run the server 
```
(online-order) ➜  app git:(master) ✗ pwd
/Users/shaytac/online-order/app
(online-order) ➜  app git:(master) ✗ python manage.py runserver
```

#### To create a superuser first initiate the migration so auth tables are created than issue `createsuperuser` command.
````
(online-order) ➜  app git:(multitenant) ✗ python manage.py migrate       
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
(online-order) ➜  app git:(multitenant) ✗ python manage.py makemigrations
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
No changes detected
(online-order) ➜  app git:(multitenant) ✗ python manage.py createsuperuser
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
Username (leave blank to use 'shaytac'): shaytac
Email address: shaytac@gmail.com
Password: 
Password (again): 
This password is entirely numeric.
Password: 
Password (again): 
This password is entirely numeric.
Password: 
Password (again): 
Superuser created successfully.
(online-order) ➜  app git:(multitenant) ✗
````

#### After creating the models you need to issue `makemigrations` than issue `migrate` command.

````
(online-order) ➜  app git:(pizza) ✗ python manage.py makemigrations
Migrations for 'order':
  order/migrations/0001_initial.py
    - Create model Flavor
    - Create model Size
    - Create model Topping
````




```
(online-order) ➜  app git:(multitenant) ✗ python manage.py makemigrations app      
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
Migrations for 'app':
  app/migrations/0001_initial.py
    - Create model Client

```
# !Never use migrate as it would sync all your apps to public! #

````
(online-order) ➜  app git:(multitenant) ✗ python manage.py migrate 
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
CommandError: migrate has been disabled, for database 'default'. Use migrate_schemas instead. Please read the documentation if you don't know why you shouldn't call migrate directly!
(online-order) ➜  app git:(multitenant) ✗ python manage.py migrate_schemas 
/Users/shaytac/miniconda2/envs/online-order/lib/python3.6/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
[standard:public] === Running migrate for schema public
[standard:public] Operations to perform:
[standard:public]   Apply all migrations: admin, app, auth, contenttypes, sessions
[standard:public] Running migrations:
[standard:public]   No migrations to apply.
(online-order) ➜  app git:(multitenant) ✗ 
````

#### To create a new tenant use `python manage.py shell` 
````
>>> tenant=Client(domain_url='localhost', schema_name='public', name='shaytac inc', paid_until='2016-12-5',on_trial=False)
>>> tenant.save()
````