from pymodbus.client.sync import ModbusTcpClient

port = 510 # I found this using a port scanner. It was the only port that would let me connect without giving me a "remote host forcibly closed" error
ip = "169.254.161.3" # I found this IP using the LogoSoft sofware and connecting to the plc

# Writes to an individual coil and returns response
def write_coil(coil, writeValue):
    client = ModbusTcpClient(ip, port=port)
    client.connect()
    result = client.write_coil(coil, writeValue)
    client.close()
    return result

# Reads an individual coil and returns response
def read_coil(coil):
    client = ModbusTcpClient(ip, port=port)
    client.connect()
    result = client.read_coils(coil,1)
    client.close()
    return result.bits[0]

# Wrties to a holding register, this will affect the values of coils
def write_register(register, value):
    client = ModbusTcpClient(ip, port=port)
    client.connect()
    result = client.write_register(register, value)
    client.close()
    return result

 # Reads holding register, values in here are set by values of coils, interestingly
def read_register(register):
    client = ModbusTcpClient(ip, port=port)
    client.connect()
    result = client.read_holding_registers(register)
    client.close()
    # return result.registers[0]
    return result
