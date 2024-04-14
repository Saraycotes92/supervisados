import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar datos
df = pd.read_csv('data.csv')
X = df[['hora', 'pasajeros', 'duracion']]
y = df['incidencias']

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Crear y entrenar el modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, '/Users/cristhianbonilla/Documents/ia/model.pkl')
