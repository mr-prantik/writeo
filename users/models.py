from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#ceate your models here 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f"{self.user.username} profile" 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            op_size = (300, 300)
            image.thumbnail(op_size)
            image.save(self.image.path)