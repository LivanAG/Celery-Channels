import os

broker_url = os.environ.get('REDIS_URL')

imports = ['Apps.Controlador.tareas']

result_backend = os.environ.get('REDIS_URL')

timezone = 'UTC'

result_serializer = 'json'

beat_schedule = {

    'revision-every-5-seconds': {
        'task': 'Apps.Controlador.tareas.revision',
        'schedule': 1.0,
    },
}
