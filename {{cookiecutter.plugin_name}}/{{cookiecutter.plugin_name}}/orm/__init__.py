from sqlalchemy.orm import configure_mappers

from MeMo.models.schema import initialize_schema
from {{ cookiecutter.plugin_name }}.orm.{{ cookiecutter.plugin_name }} import ExampleTable  # noqa: F401

configure_mappers()


def includeme(config):
    initialize_schema()
