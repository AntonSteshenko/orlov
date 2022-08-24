from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee

class Explane(models.Model):

    class Meta:
        verbose_name="Объяснительная"
        verbose_name_plural="Объяснительные"

    dt_orig = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время внесения записи",
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )

    date = models.DateField(
        verbose_name = "Дата отсутствия",
    )

    time_from = models.TimeField(
        null=True,
        blank=True,
        verbose_name="отсутствовал с"
    )

    time_to = models.TimeField(
        null=True,
        blank=True,
        verbose_name="отсутствовал до"
    )

    

    explane = models.TextField(
        max_length=1000,
        verbose_name="Объяснение"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, внесший запись"
    )

    def __str__(self):
        return str(self.id)
