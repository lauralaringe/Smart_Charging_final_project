import blynklib
import pandas as pd
import time
import datetime
import re
import serial

# import functions from other files
from Red_Electrica_Data import get_price_data
from RE_Data import get_irradiance_wind_data
BLYNK_AUTH = 'SQhg7qdEsDMY3RyzwQzKvrWiJJmtoeGz'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

mess = "{},{}"

split = 0
# register handler for virtual pin V4 write event


@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    message = mess.format(pin, value)
    temp = re.findall(r'\d+', message)
    res = list(map(int, temp))
    total_time = res[1]
    print(total_time)

    while total_time > 0:

        print('Phone plugged for', total_time, " hours")
        price_df = get_price_data()
        irradiance_df, wind_df = get_irradiance_wind_data()

        current_hour = datetime.datetime.now().hour
        end_hour = current_hour + total_time -1

        price_to_check = price_df[current_hour:end_hour]

        irradiance_to_check = irradiance_df[current_hour:end_hour]
        wind_to_check = wind_df[current_hour:end_hour]
        total_df = pd.DataFrame()
        total_df['to_maximize'] = irradiance_to_check["G(h)"] + wind_to_check["WS10m"] - price_to_check[1]

        # Get the 2 maximum
        maximum2 = total_df['to_maximize'].nlargest(2)

        arduino = serial.Serial('COM4', 9600)
        current = arduino.readline().decode("utf-8")  # read from serial port
        if current < 0.295 or (time.time() - start_time >= 3600):
            arduino.write('L'.encode())
            print('Switch OFF')

        current_hour = datetime.datetime.now().hour
        if current_hour == maximum2.index[0] or current_hour == maximum2.index[1]:
            start_time = time.time()
            arduino.write('H'.encode())
            print('Switch ON')
            time.sleep(60)  # wait 1 minute

            # check current if current 0 stop charging
            current = arduino.readline().decode("utf-8")
            if current < 0.295 or (time.time() - start_time >= 3600):
                arduino.write('L'.encode())
                print('Switch OFF')


while True:
    total_time = 0
    blynk.run()
