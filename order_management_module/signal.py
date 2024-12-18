from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ImageItemOrder
import os

@receiver(post_delete, sender=ImageItemOrder)
def delete_image_file(sender, instance, **kwargs):
    """
    Señal que se ejecuta después de eliminar un ImageItemOrder.
    Elimina el archivo físico asociado si existe.
    """
    if instance.image and os.path.isfile(instance.image.path):
        try:
            os.remove(instance.image.path)  # Eliminar el archivo
        except Exception as e:
            print(f"Error eliminando el archivo {instance.image.path}: {e}")