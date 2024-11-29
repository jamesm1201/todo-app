from django.db import models
from django.contrib.auth.models import User

#Note model contains fields for the todo note
#created_at automatically records the datetime it was made
#Foreign key links to user model, related name allows you to find all a user's related notes
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title

