import os
import sys

import MeMo.plugins as plugins
import MeMo.plugins.utilities as u
from {{ cookiecutter.plugin_name }}.views import MyPublicView, MyPrivateView


class {{ cookiecutter.plugin_name }}(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfig)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IDatabase)

    # IRoutes

    def before_mapping(self, config):
        # We don't add any routes before the host application
        return []

    def after_mapping(self, config):
        # Routes added after the MeMo routes
        custom_map = [
            u.add_route(
                "plugin_mypublicview", "/mypublicview", MyPublicView, "public.jinja2"
            ),
            u.add_route(
                "plugin_myprivateview",
                "/user/{userid}/myprivateview",
                MyPrivateView,
                "private.jinja2",
            ),
        ]
        return custom_map

    # IConfig

    def update_config(self, config):
        # Add the templates of the plugin to the config
        u.add_templates_directory(config, "templates")

    # ITranslation

    def get_translation_directory(self):
        module = sys.modules["{{ cookiecutter.plugin_name }}"]
        return os.path.join(os.path.dirname(module.__file__), "locale")

    def get_translation_domain(self):
        return "{{ cookiecutter.plugin_name }}"

    # IDatabase

    def update_orm(self, config):
        config.include("{{ cookiecutter.plugin_name }}.orm")

    def update_extendable_tables(self, tables_allowed):
        tables_allowed.append("{{ cookiecutter.plugin_name }}_example")
        return tables_allowed

    def update_extendable_modules(self, modules_allowed):
        modules_allowed.append("{{ cookiecutter.plugin_name }}.orm.{{ cookiecutter.plugin_name }}")
        return modules_allowed
