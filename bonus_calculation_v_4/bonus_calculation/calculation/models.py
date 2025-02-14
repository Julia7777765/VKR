from django.db import models

class Calculation(models.Model):
    year = models.IntegerField(verbose_name="Год", default=2023)
    quarter = models.CharField(verbose_name="Квартал", max_length=20, default="1 квартал")
    car_insurance_sales = models.IntegerField(verbose_name="Число продаж страхований авто", default=0)
    property_insurance_sales = models.IntegerField(verbose_name="Число продаж страхований имущества", default=0)
    manager_evaluation = models.IntegerField(verbose_name="Оценка выполненной работы руководителем", default=0)
    plan_completion = models.IntegerField(verbose_name="Факт выполнения плана")
    sick_days = models.IntegerField(verbose_name="Число дней больничного", default=0)
    vacation_days = models.IntegerField(verbose_name="Отпуск (дни)", default=0)
    premium = models.DecimalField(verbose_name="Премия", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Расчет премии за {self.quarter} {self.year}"