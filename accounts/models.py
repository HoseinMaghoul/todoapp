from django.db import models
from django.contrib.auth.models import User 



class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)


    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    upload_at = models.DateField(auto_now_add=True, null=True)
    role = models.IntegerField(null=True, default=1)


    def __str__(self):
        return f'{self.user.username}'