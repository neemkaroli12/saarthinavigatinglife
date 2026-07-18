from django.db import models

# Create your models here.
class Feedback(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    services = models.TextField(blank=True)
    other_service = models.CharField(max_length=200, blank=True)

    satisfaction = models.CharField(max_length=50, blank=True)
    liked = models.TextField(blank=True)
    other_liked = models.CharField(max_length=200, blank=True)

    heard = models.CharField(max_length=50, blank=True)
    wellbeing = models.CharField(max_length=50, blank=True)
    recommend = models.CharField(max_length=50, blank=True)

    review = models.TextField()
    suggestions = models.TextField(blank=True)

    publish_permission = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name