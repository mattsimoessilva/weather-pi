# WeatherPI

WeatherPI is a Python project that reads temperature and humidity data from a DHT11 sensor connected to a Raspberry Pi. This project provides a simple way to monitor and record environmental data, making it ideal for weather monitoring or home automation applications.

## Features

- Reads temperature and humidity data from a DHT11 sensor.
- Provides accurate and up-to-date information for your weather monitoring needs.
- Easily configurable for different GPIO pins and sensor types.
- Lightweight and easy to use.

## Prerequisites

Before using WeatherPI, ensure you have the following:

- A Raspberry Pi (or similar single-board computer).
- A DHT11 sensor connected to your Raspberry Pi.
- Python 3.x installed on your Raspberry Pi.

## Installation

1. Clone the repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/yourusername/weather-pi.git

2. Navigate to the project-directory:

   cd weather-pi

3. Install the required dependencies:

   pip install -r requirements.txt

## Usage

1. Run the `sensor_read.py` script to read temperature and humidity data:

   python sensor_read.py

2. View the real-time temperature and humidity information displayed in the terminal

## Configuration

- You can configure the GPIO pin and sensor type by modifying the variables in the `sensor_read.py` script.

  ```python
  # Define the type of the sensor (DHT11 or DHT22)
  sensor = Adafruit_DHT.DHT11

  # Define the GPIO pin to which the sensor is connected
  pin = 4  # You can adjust the pin number according to your setup

## Contributing

Contributions are welcome! If you find any issues or would like to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the license file for details.

## Acknowledgments

- The WeatherPI project is inspired by a passion for weather monitoring and Raspberry Pi tinkering.
  
- We appreciate the open-source community for their valuable contributions and resources.
