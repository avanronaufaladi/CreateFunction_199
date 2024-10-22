def konversuhu(temperature, value):
    if value == 'c':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'c'
    else:
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'f'

celsius_temperature = 30
temperaturesuhu, target_value = konversuhu(celsius_temperature, 'f')
print(f"{celsius_temperature}°c dikonversi ke fahrenheit adalah
    {temperaturesuhu}°{target_value}" )
            
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversuhu(fahrenheit_temperature, 'c')
print(f"{fahrenheit_temperature}°f dikonversi ke celcius adalah {temperaturesuhu}°{target_value}")
              
              
