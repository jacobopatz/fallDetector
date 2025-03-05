from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.TextField()  # Stores the message text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation

    def __str__(self):
        return self.content[:50]  # Return first 50 characters for display