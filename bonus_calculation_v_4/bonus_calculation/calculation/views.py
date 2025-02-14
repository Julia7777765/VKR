import joblib
import pandas as pd
from django.shortcuts import render, redirect
from .forms import CalculationForm
from .models import Calculation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


loaded_model = joblib.load('best_model.pkl')

def redirect_to_login(request):
    return redirect('/login/')

def custom_logout(request):
    logout(request)
    return redirect('/login/')

@login_required
def calculate_bonus(request):
    year = request.GET.get('year', 2023)
    quarter = request.GET.get('quarter', '1 квартал')

    calculation = Calculation.objects.filter(year=year, quarter=quarter).first()

    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.year = year
            instance.quarter = quarter

            new_data = pd.DataFrame({
                'Оценка выполненной работы руководителем': [instance.manager_evaluation],
                'Факт выполнения плана (%)': [instance.plan_completion],
                'Число продаж страхований авто': [instance.car_insurance_sales],
                'Число продаж страхований имущества': [instance.property_insurance_sales],
                'Число дней больничного': [instance.sick_days],
                'Число дней отпуска': [instance.vacation_days]
            })

            instance.premium = loaded_model.predict(new_data)[0]
            instance.save()
            return redirect(f'/calculate/?year={year}&quarter={quarter}')
        else:
            print("Форма не валидна:", form.errors)
    else:
        if calculation:
            form = CalculationForm(instance=calculation)
        else:
            form = CalculationForm(initial={'year': year, 'quarter': quarter})

    calculations = Calculation.objects.all()
    return render(request, 'calculation/calculate.html', {
        'form': form,
        'calculations': calculations,
        'selected_year': int(year),
        'selected_quarter': quarter,
        'calculation': calculation
    })