from django.apps import AppConfig


class OrderManagementModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_management_module'

    def ready(self):
        import order_management_module.signal
