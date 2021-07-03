from django.db import models


class ListItems(models.Model):
    items = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.items

