from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):

    class Meta:
        verbose_name="Отдел"
        verbose_name_plural="Отделы"

    name = models.CharField(max_length=20)
    head = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Руководитель",
        null=True,
    )

    def __str__(self):
        return self.name
