from django.db import models
from django.conf import settings  # to reference the custom User model

class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # links to your custom User model
        on_delete=models.CASCADE,
        related_name="blogs"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title