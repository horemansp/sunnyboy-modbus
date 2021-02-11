import struct
from pyModbusTCP.client import ModbusClient
Modbus_Device_IP="192.168.0.237"
Modbus_Device_ID="3"
Modbus_Device_Port = 502
SMA_modbus_to_collect = [[30529,2,"Total energy (Wh) produced by system"],[30535,2,"Energy (Wh) produced today"],[30775,2,"Real time power (W) production"] ]

def Collect_Modbus(Device_IP, Device_ID, Device_Port, Collect_Array): 
    c= ModbusClient(host=Device_IP,unit_id=Device_ID,port=Device_Port,debug=False)
    c.open()
    collected_array = [0]
    collected_array.pop()
    for x in range(len(Collect_Array)):
        print(x)
        collected = c.read_input_registers(Collect_Array[x][0],Collect_Array[x][1])
        collected_merged = struct.pack('>HH',collected[0],collected[1])
        collected_array.append(struct.unpack('>I', collected_merged)[0])
        print(collected_array)
    c.close()
    return collected_array

print(Collect_Modbus(Modbus_Device_IP, Modbus_Device_ID,Modbus_Device_Port,SMA_modbus_to_collect))
