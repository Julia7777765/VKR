# Generated by Django 5.1.5 on 2025-01-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Calculation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(default=2023, verbose_name="Год")),
                (
                    "quarter",
                    models.CharField(
                        default="1 квартал", max_length=20, verbose_name="Квартал"
                    ),
                ),
                (
                    "car_insurance_sales",
                    models.IntegerField(
                        default=0, verbose_name="Число продаж страхований авто"
                    ),
                ),
                (
                    "property_insurance_sales",
                    models.IntegerField(
                        default=0, verbose_name="Число продаж страхований имущества"
                    ),
                ),
                (
                    "manager_evaluation",
                    models.IntegerField(
                        default=0,
                        verbose_name="Оценка выполненной работы руководителем",
                    ),
                ),
                (
                    "plan_completion",
                    models.IntegerField(verbose_name="Факт выполнения плана"),
                ),
                (
                    "sick_days",
                    models.IntegerField(
                        default=0, verbose_name="Число дней больничного"
                    ),
                ),
                (
                    "vacation_days",
                    models.IntegerField(default=0, verbose_name="Отпуск (дни)"),
                ),
                (
                    "premium",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Премия",
                    ),
                ),
            ],
        ),
    ]
