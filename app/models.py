from django.db import models

# Create your models here.



class BootcampRegistration(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=200)
    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email} - {self.role}"
