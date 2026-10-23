{{ cookiecutter.plugin_description }}
==============

Getting Started
---------------

- Activate the MeMo environment.
```
$ source /path/to/memo_env/bin/activate
```

- Change directory into your newly created plugin.
```
$ cd {{ cookiecutter.plugin_name }}
```

- Build the plugin
```
$ python setup.py develop
```

- Alembic configuration for extra tables
```
$ mv alembic.example.ini alembic.ini
```
- Edit alembic.ini and replace sqlalchemy.url with the one in the MeMo ini file
```
$ alembic revision --autogenerate -m "Initial version"
$ alembic upgrade head
```

- Add the plugin to the MeMo list of plugins by editing the following line in development.ini or production.ini
```
    #MeMo.plugins = examplePlugin
    MeMo.plugins = {{ cookiecutter.plugin_name }}
```
{%- if cookiecutter.plugin_hasCeleryTasks|lower == "y" %}

- Restart the MeMo Celery worker so it loads the tasks in `celerytasks.py`
{%- endif %}

- Run MeMo again

Example routes
--------------

- Public: `/mypublicview`
- Private (login required): `/user/{userid}/myprivateview`
