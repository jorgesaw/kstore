# Python
from uuid import uuid4


def custom_upload_to(instance, filename):
    """Custom upload picture function.

    Delete the old image saved as an avatar and set filename as random string.    
    """
    
    old_instance = instance.__class__.objects.get(pk=instance.pk)
    old_instance.picture.delete()

    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    
    return 'users/pictures/' + filename
