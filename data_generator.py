# data_generator.py

import pandas as pd

def generate_data():
    data = {
        'hora': [7, 9, 13, 18, 21, 10, 15, 20, 22, 6, 8, 12, 17, 19, 23, 14, 16, 11, 5, 4],
        'pasajeros': [50, 200, 150, 300, 100, 180, 160, 220, 140, 190, 210, 50, 120, 260, 110, 130, 250, 170, 80, 60],
        'duracion': [30, 45, 40, 60, 35, 55, 50, 65, 25, 45, 50, 20, 35, 55, 40, 45, 60, 25, 30, 15],
        'incidencias': [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

if __name__ == "__main__":
    generate_data()
