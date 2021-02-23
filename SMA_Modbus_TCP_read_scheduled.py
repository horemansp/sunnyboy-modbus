import struct
from pyModbusTCP.client import ModbusClient
import requests
from datetime import datetime
import schedule
import time

savemye_url = 'http://192.168.1.230/savemye/api/store.php'
Modbus_Device_IP="192.168.0.237"
Modbus_Device_ID="3"
Modbus_Device_Port = 502
SMA_modbus_to_collect = [[30775,2,"W","Real time power (W) production"]]
SMA_modbus_to_collect_2 = [[30535,2,"Wh","Real-Time Energy (Wh) produced today"]]
SMA_modbus_to_collect_3 = [[30529,2,"Wh","Total energy (Wh) produced by system"]]

def store_url(sensor, description, value, metric, timestamp):
    try:
        url = savemye_url
        myobj = {'sensor' : sensor,'description': description, 'value':value, 'metric': metric, 'timestamp':timestamp}
        x = requests.post(url, data = myobj)
        print(x)
    except requests.RequestException as e:
        print(e)

def Collect_Modbus(Collect_Array):
    #todo: add try
    try:
        c= ModbusClient(host=Modbus_Device_IP,unit_id=Modbus_Device_ID,port=Modbus_Device_Port,debug=False)
        c.open()
        
        for x in range(len(Collect_Array)):
            collected_array = [0]
            collected_array.pop()
            collected = c.read_input_registers(Collect_Array[x][0],Collect_Array[x][1])
            collected_merged = struct.pack('>HH',collected[0],collected[1])
            collected_array.append(struct.unpack('>i', collected_merged)[0])
            #store_url format : (sensor, description, value, metric, timestamp)
            store_url("SMA",Collect_Array[x][3],collected_array,Collect_Array[x][2],datetime.now())
            print("SMA",Collect_Array[x][3],collected_array[0],Collect_Array[x][2],datetime.now())
        c.close()
    except:
        print("Could not read from modbus")
        
        
''' schedule examples
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
'''
    
schedule.every(15).seconds.do(Collect_Modbus, SMA_modbus_to_collect)
schedule.every(5).minutes.do(Collect_Modbus, SMA_modbus_to_collect_2)
schedule.every(1).hour.do(Collect_Modbus, SMA_modbus_to_collect_3)

while True:
    schedule.run_pending()
    time.sleep(1)

