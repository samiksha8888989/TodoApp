from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=False)
    completed = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return "{}".format(self.title)
