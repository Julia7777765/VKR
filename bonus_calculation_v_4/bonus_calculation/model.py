from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import pandas as pd

df = pd.read_csv('employee_bonus_data.csv')

X = df.drop('Премия', axis=1)
y = df['Премия']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return y_pred, mae, mse, r2

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    "SVR": SVR(),
    "XGBoost": XGBRegressor(random_state=42)
}

rf_params = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
rf_grid = GridSearchCV(RandomForestRegressor(random_state=42), rf_params, cv=3, scoring='r2')
models["Random Forest (Tuned)"] = rf_grid

gb_params = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5]
}
gb_grid = GridSearchCV(GradientBoostingRegressor(random_state=42), gb_params, cv=3, scoring='r2')
models["Gradient Boosting (Tuned)"] = gb_grid

# Оценка моделей
results = {}
for name, model in models.items():
    print(f"Обучение модели: {name}")
    y_pred, mae, mse, r2 = evaluate_model(model, X_train, X_test, y_train, y_test)
    results[name] = {"MAE": mae, "MSE": mse, "R²": r2, "Predictions": y_pred}
    print(f"  MAE: {mae:.2f}")
    print(f"  MSE: {mse:.2f}")
    print(f"  R²: {r2:.2f}")
    print()

best_model = max(results, key=lambda x: results[x]['R²'])
print(f"Лучшая модель: {best_model} с R² = {results[best_model]['R²']:.2f}")

print("\nПримеры предсказаний и реальных значений для лучшей модели:")
best_predictions = results[best_model]['Predictions']
for i in range(10):
    print(f"Реальное значение: {y_test.iloc[i]}, Предсказанное значение: {best_predictions[i]:.2f}")

best_model_name = max(results, key=lambda x: results[x]['R²'])
best_model = models[best_model_name]  # Получаем объект лучшей модели
joblib.dump(best_model, 'best_model.pkl')  # Сохраняем модель в файл
print(f"Лучшая модель '{best_model_name}' сохранена как 'best_model.pkl'.")


loaded_model = joblib.load('best_model.pkl')

new_data = pd.DataFrame({
    'Оценка выполненной работы руководителем': [8.5, 7.0],
    'Факт выполнения плана (%)': [95, 80],
    'Количество часов работы': [200, 180],
    'Число продаж страхований авто': [12, 5],
    'Число продаж страхований имущества': [8, 3],
    'Число дней больничного': [2, 4],
    'Число дней отпуска': [5, 7]
})

predictions = loaded_model.predict(new_data)
print("\nПредсказанные премии для новых данных:")
for i, pred in enumerate(predictions):
    print(f"Сотрудник {i + 1}: {pred:.2f} руб.")