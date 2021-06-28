from django.db import models

class Order(models.Model):

    order = models.JSONField()

    def __str__(self):
        return self.error
