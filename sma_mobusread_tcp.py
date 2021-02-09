from pyModbusTCP.client import ModbusClient
c= ModbusClient(host="192.168.0.237",port=502,debug=True)
c.open()
collected = c.read_input_registers(30513,4)
print("registers content=",collected)

c.close()

