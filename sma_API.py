from sma_sunnyboy import *
import urllib3
urllib3.disable_warnings()
client = WebConnect("192.168.0.237", Right.USER, "Soloya2019", True)
client.auth()
pow_current = client.get_value(Key.pow_current)
print("real time power=",pow_current)
client.logout()