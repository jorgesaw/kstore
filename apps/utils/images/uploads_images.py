
def custom_upload_to(instance, filename):
    """Custom upload image.
    
    Delete image for user.
    """

    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles_images/' + filename
