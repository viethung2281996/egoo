from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'export_data_user_task': {
        'task': 'user.tasks.exportUserDataTask',
        # Every minute
        'schedule': timedelta(seconds=3600*12),
    }
}