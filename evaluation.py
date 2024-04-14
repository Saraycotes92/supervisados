# evaluation.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def load_data():
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv('data.csv')
    X = df[['hora', 'pasajeros', 'duracion']]
    y = df['incidencias']
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def load_model(path='model.pkl'):
    # Cargar el modelo entrenado desde un archivo
    try:
        return joblib.load(path)
    except FileNotFoundError:
        print(f"Error: El archivo {path} no fue encontrado.")
        exit()

def evaluate_model(model, X_test, y_test):
    # Realizar predicciones con el modelo
    predictions = model.predict(X_test)

    # Calcular e imprimir el reporte de clasificación y la matriz de confusión
    print("Reporte de Clasificación:")
    print(classification_report(y_test, predictions))
    
    print("Matriz de Confusión:")
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Matriz de Confusión')
    plt.ylabel('Actual')
    plt.xlabel('Predicción')
    plt.show()

    # Calcular y mostrar la precisión
    accuracy = accuracy_score(y_test, predictions)
    print(f"Precisión del Modelo: {accuracy:.2f}")

def main():
    # Cargar los datos y el modelo
    X_train, X_test, y_train, y_test = load_data()
    model = load_model()

    # Evaluar el modelo
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
