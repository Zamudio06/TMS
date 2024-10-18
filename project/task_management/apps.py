from django.apps import AppConfig


class TaskManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.task_management'

    def ready(self):
        import project.task_management.signals