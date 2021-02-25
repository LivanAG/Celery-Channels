web: daphne DeployASGI.asgi:application --port $PORT --bind 0.0.0.0

worker: celery -A Apps.Controlador.tareas worker --loglevel=info

celery_beat: celery -A Apps.Controlador.celery beat --loglevel=info
