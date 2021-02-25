from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeployASGI.settings')

app = Celery('celery')

app.config_from_object('Apps.Controlador.celery_config')
