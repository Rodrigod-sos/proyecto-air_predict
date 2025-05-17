Air-Benzene-Predictor
Predicción de la concentración de benceno en el aire a partir de variables ambientales – Trabajo Final Módulo 9

Este proyecto consiste en el desarrollo de un modelo de aprendizaje automático capaz de predecir la concentración de benceno (µg/m³) en el aire utilizando variables ambientales medidas por sensores en tiempo real.

Descripción del modelo
El modelo fue entrenado utilizando un conjunto de datos que contiene registros históricos de calidad del aire, temperatura y sensores químicos. Estos datos permiten estimar de forma precisa el nivel de benceno, un contaminante perjudicial para la salud humana.

A través de un análisis de correlación, se seleccionaron las 6 variables independientes más relevantes para el modelo:

Humedad absoluta (humedad_abs)

Temperatura ambiente (temperatura)

Humedad relativa (humedad_rel)

Sensor 1: Estaño - CO (sensor_1)

Sensor 4: NO₂ (sensor_4)

Sensor 2: Titania - NMHC (sensor_2)

Estas variables permiten al modelo generar una predicción de la concentración de benceno en el aire.
