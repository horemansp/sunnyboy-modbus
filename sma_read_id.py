from pyModbusTCP.client import ModbusClient
c= ModbusClient(host="192.168.0.237",uit_id="3", port=502,debug=False)
c.open()
collected = c.read_holding_registers(42109,4)
print("Device ID=",collected[3])

c.close()
