# MeMo Plugins Template

A Cookiecutter (project template) for creating MeMo plugins.

Requirements
------------

* Python 3.10
* MeMo installed in development mode (`python setup.py develop`)
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Usage
-----

1. Activate the MeMo environment and generate a MeMo plugin project, following the prompts from the command
    ```sh
    $ cookiecutter https://github.com/BrandonMrBot/memo-cookiecutter-plugin.git
    ```

2. Follow the instructions printed at the end of the generation (also available in the README of the generated plugin).

What the template provides
--------------------------

* `plugin.py`: plugin class implementing `IRoutes`, `IConfig`, `ITranslation` and `IDatabase`.
* `views.py`: one public view (`/mypublicview`) and one private view (`/user/{userid}/myprivateview`).
* `templates/`: Jinja2 templates extending `public/page.jinja2` and `private/page.jinja2`.
* `orm/`: example SQLAlchemy table registered in MeMo's ORM.
* `alembic/`: migrations for the plugin tables, using its own version table.
* `celerytasks.py`: optional Celery tasks (registered under the `memo.tasks` entry point).
* `locale/`, `static/`, `resources/`: how-to guides for translations, static files and JS/CSS resources.
