from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_user = models.ForeignKey(User, null=True, blank=True, related_name="child_users", on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
