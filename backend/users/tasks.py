from django.core import management

from django-react import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
