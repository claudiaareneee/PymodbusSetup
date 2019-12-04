from pymodbus.client.sync import ModbusTcpClient

port = 500
ip = '169.254.161.3'
# logfile = open(r'portlog.txt','a')

def scanPort(port):
    client = ModbusTcpClient(ip, port=port)
    portConnected = client.connect()
    print( "port: " + str(port) + " connected = " + str(portConnected))
    # logfile.write("\nport: " + str(port) + " = " + str(portConnected))
    if (portConnected):
        try:
            # result = client.read_coils(1,1)
            # print (" Valid YAY " + result.bits[0])
            # logfile.write(" Valid YAY " + result.bits[0])

            error = client.write_coil(1, True)
            if error:
                print (" Valid YAY but? " + str(error))
                # logfile.write(" Valid YAY but? " + str(error))
            else:
                print (" you dope head it actually worked")
                # logfile.write(" Valid YAY ")
        except Exception as e:
            print (" but Invalid -- " + str(e))
            # logfile.write(" but Invalid -- " + str(e))
    return

def writePort(port, writeCoil, writeVal):
    client = ModbusTcpClient(ip, port=port)
    portConnected = client.connect()
    response = client.write_coil(writeCoil, writeVal)
    return response

def readPort(port, readCoil):
    client = ModbusTcpClient(ip, port=port)
    portConnected = client.connect()
    result = client.read_coils(readCoil,1)
    print(result.bits[0])
    

scanPort(510)
readPort(510, 1)
writePort(510, 1, 0)
readPort(510, 1)
readPort(510, 2)
writePort(510, 2, 1)
readPort(510, 2)

