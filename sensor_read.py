import Adafruit_DHT

# Define o tipo do sensor DHT (DHT11 ou DHT22)
sensor = Adafruit_DHT.DHT11

# Define o pino GPIO ao qual o sensor está conectado
pin = 4  # Você pode ajustar o número do pino conforme a sua configuração

# Tenta ler os dados do sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Verifica se a leitura foi bem-sucedida
if humidity is not None and temperature is not None:
    print("Temperatura: {0:0.1f}°C".format(temperature))
    print("Umidade: {0:0.1f}%".format(humidity))
else:
    print("Falha ao ler dados do sensor. Verifique a conexão e tente novamente.")
