from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import Users


@receiver(post_save, sender=Users)
def post_save_user(instance, created, **kwargs):
<<<<<<< HEAD
    try:
        image = Image.open(instance.avatar)
        if image.height != image.width:
            if image.height < image.width:
                x = (int(image.width) - int(image.height)) / 2
                y = 0
                h = image.height
                w = image.height
                
            elif image.height > image.width:
                y = (int(image.height) - int(image.width)) / 2
                x = 0
                h = image.width
                w = image.width
            
            cropped_image = image.crop((x, y, w, h))
            resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
            resized_image.save(instance.avatar.path)
    except Exception:
        instance.avatar = '/img/user.png'
        instance.save()
=======
    
    try:
        image = Image.open(instance.avatar)

        if image.height < image.width:
            x = (int(image.width) - int(image.height)) / 2
            y = 0
            h = image.height
            w = image.height
            
        elif image.height > image.width:
            y = (int(image.height) - int(image.width)) / 2
            x = 0
            h = image.width
            w = image.width
        
        cropped_image = image.crop((x, y, w, h))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(instance.avatar.path)
    
    except Exception:
        instance.avatar = '/img/user.png'
        instance.save()
    return instance
>>>>>>> 2e5a3836685d3337c6441aafa57cd2556cff4d20
