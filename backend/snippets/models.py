from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    winner = models.TextField()
    class Meta:
        ordering = ['created']
