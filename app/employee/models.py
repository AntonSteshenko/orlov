from tabnanny import verbose
from django.db import models

from department.models import Department

class Employee(models.Model):

    class Meta:
        verbose_name="Сотрудник"
        verbose_name_plural="Сотрудники"

    full_name = models.CharField(max_length=50, verbose_name="ФИО полностью")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Отдел",
    )

    def __str__(self):
        return self.full_name
