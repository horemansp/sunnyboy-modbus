import struct
from pyModbusTCP.client import ModbusClient
c= ModbusClient(host="192.168.0.237",unit_id="3",port=502,debug=False)
c.open()

collected = c.read_holding_registers(42109,4)
print("Device ID=",collected[3])

#collected = c.read_input_registers(30775,2)

collected = c.read_input_registers(30529,2)
collected_merged = struct.pack('>HH',collected[0],collected[1])
print("modbus registers (30529) total energy produced Wh=",collected)
print("Produced energy in Wh=",struct.unpack('>I', collected_merged)[0])
#unpack always returns a tuple, even if there is only one element, hence the [0] to select the first element


#s = struct.pack('HH',collected[0], collected[1])
#print(s)

#collected = c.read_input_registers(30517,4)
#print("total energy produced today =",collected)
#collected = c.read_input_registers(30775,2) #confirmed
#print("Real time power =",collected) 

c.close()

