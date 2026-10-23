{% if cookiecutter.plugin_hasCeleryTasks|lower == 'y' -%}
import time

from MeMo.config.celery_app import celeryApp
from MeMo.config.celery_class import celeryTask


@celeryApp.task(bind=True, base=celeryTask, soft_time_limit=7200, time_limit=7200)
def plugin_task(self):
    # Just to test that such sleep is handled by celery and does not hang MeMo
    time.sleep(30)
    print("Plugin task finished")
{%- endif %}
