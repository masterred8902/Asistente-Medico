from machine import Pin
import time

# Configuración del sensor PIR y el LED
pir_sensor = Pin(14, Pin.IN)  # El PIR está conectado al pin 14
led = Pin(2, Pin.OUT)

while True:
    if pir_sensor.value():  # Si el sensor detecta movimiento
        print("Movimiento detectado!")
        led.value(1)  # Enciende el LED
    else:
        print("No se detecto movimiento")
        led.value(0)  # Apaga el LED
    time.sleep(0.1)  # Pequeño retraso para evitar lecturas erróneas
