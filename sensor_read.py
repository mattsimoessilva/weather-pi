import Adafruit_DHT
import time
import matplotlib.pyplot as plt
import pandas as pd

# Define o tipo do sensor DHT (DHT11 ou DHT22)
sensor = Adafruit_DHT.DHT11

# Define o pino GPIO ao qual o sensor está conectado
pin = 4  # Você pode ajustar o número do pino conforme a sua configuração

# Create empty lists to store temperature and humidity data
temperature_data = []
humidity_data = []
time_data = []

# Collect data for a certain amount of time
start_time = time.time()
collect_time = 60*10  # Collect data for 10 minutes

while time.time() - start_time < collect_time:
    # Tenta ler os dados do sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Verifica se a leitura foi bem-sucedida
    if humidity is not None and temperature is not None:
        print("Temperatura: {0:0.1f}°C".format(temperature))
        print("Umidade: {0:0.1f}%".format(humidity))
        
        # Add the data to the lists
        temperature_data.append(temperature)
        humidity_data.append(humidity)
        time_data.append(time.time() - start_time)
    else:
        print("Falha ao ler dados do sensor. Verifique a conexão e tente novamente.")
    
    # Wait before collecting the next set of data
    time.sleep(60)  # Wait for 60 seconds

# Convert the lists to pandas Series for easier data manipulation
temperature_series = pd.Series(temperature_data, index=time_data)
humidity_series = pd.Series(humidity_data, index=time_data)

# Calculate the moving average with a window size of 10
temperature_moving_avg = temperature_series.rolling(window=10).mean()
humidity_moving_avg = humidity_series.rolling(window=10).mean()

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(temperature_moving_avg, label='Temperature (°C)')
plt.plot(humidity_moving_avg, label='Humidity (%)')
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Time (seconds)')
plt.legend()
plt.show()
