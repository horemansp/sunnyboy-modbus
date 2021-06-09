# DSRM T211, sunnyboy5-modbus, Victron battery controller-modbus

Collects:
- Real time power & dialy energy from a T211 digital smart meter (Belgian) over a serial cable with a RPI4
- Real time power produced & daily energy by a PV system with a Sunnyboy 5 converter over ModbusTCP (ModbusTCP must be enabled)
- Real time power consumed or delivered & battery charge status from a Victron battery converter system over ModbusTCP
Calculates
- real time power from or to grid
- real time home consumption (excluding battery)
Stores:
- Data in mySQL database via a web-API call

