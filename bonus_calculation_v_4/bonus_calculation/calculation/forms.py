from django import forms
from .models import Calculation
from django.core.validators import MinValueValidator, MaxValueValidator

class CalculationForm(forms.ModelForm):
    manager_evaluation = forms.IntegerField(
        label="Оценка выполненной работы руководителем",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 10}),
    )
    plan_completion = forms.IntegerField(
        label="Факт выполнения плана",
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 100}),
    )
    car_insurance_sales = forms.IntegerField(
        label="Число продаж страхований авто",
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={'min': 0}),
    )
    property_insurance_sales = forms.IntegerField(
        label="Число продаж страхований имущества",
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={'min': 0}),
    )

    class Meta:
        model = Calculation
        fields = '__all__'
        labels = {
            'car_insurance_sales': 'Число продаж страхований авто',
            'property_insurance_sales': 'Число продаж страхований имущества',
            'manager_evaluation': 'Оценка выполненной работы руководителем',
            'plan_completion': 'Факт выполнения плана',
            'sick_days': 'Число дней больничного',
            'vacation_days': 'Отпуск (дни)',
            'premium': 'Премия',
        }