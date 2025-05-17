from air_predictor import ContaminacionPredictor

# Crear instancia del predictor
predictor = ContaminacionPredictor()

# Solicitar al usuario los 6 datos necesarios
humedad_abs = float(input("Ingrese la humedad absoluta (g/m³): "))
temperatura = float(input("Ingrese la temperatura (°C): "))
humedad_rel = float(input("Ingrese la humedad relativa (%): "))
sensor_1 = float(input("Ingrese el valor del sensor 1 (estaño CO): "))
sensor_4 = float(input("Ingrese el valor del sensor 4 (NO2): "))
sensor_2 = float(input("Ingrese el valor del sensor 2 (titania NMHC): "))

# Realizar predicción
prediccion = predictor.predict(humedad_abs, temperatura, humedad_rel, sensor_1, sensor_4, sensor_2)

# Mostrar resultado
print(f"La concentración de benceno predicha es: {prediccion:.4f} µg/m³")