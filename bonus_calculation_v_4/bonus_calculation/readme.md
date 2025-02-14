# Создаём виртуальное окружение  
    python -m venv venv

# Запускаем виртуальное окружение 
Для Windows:  

    .\venv\Scripts\activate.bat

cd C:\Users\Юлия\bonus_calculation_v_4\bonus_calculation


# Устанавливаем зависимости  

    pip install -r requirements.txt  

# Делаем миграции  

    python manage.py makemigrations  
    python manage.py migrate  

# Добавляем пользователя в систему 

    python manage.py createsuperuser

Далее переходим по ссылку:  

    http://localhost:8000/

    http://localhost:8000/admin  

Вносим пользователя в разделе users

# Запускаем сервис  

    python manage.py runserver