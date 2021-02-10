from pyModbusTCP.client import ModbusClient
c= ModbusClient(host="192.168.0.237",unit_id="3",port=502,debug=False)
c.open()

collected = c.read_holding_registers(42109,4)
print("Device ID=",collected[3])

#collected = c.read_input_registers(30775,2)
collected = c.read_input_registers(30533,4)
print("total energy produced=",collected)
collected = c.read_input_registers(30517,4)
print("total energy produced today =",collected)
collected = c.read_input_registers(30775,2)
print("Real time power =",collected)

c.close()

