from django.db import models

class Feedback(models.Model):
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback {self.id}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.ManyToManyField(Feedback, related_name="tags")

    def __str__(self):
        return self.name

