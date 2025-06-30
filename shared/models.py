from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model — abhi same as default, future me extend kar sakte hain
class User(AbstractUser):
    # Future me extra fields add karne ke liye ready hai for best practices
    pass
