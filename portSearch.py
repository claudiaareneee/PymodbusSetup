from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Defaults

Defaults.Timeout = 10

port = 500
ip = '169.254.161.3'
client = ModbusTcpClient(ip)
logfile = open(r'portlog.txt','a')

def scanPort(port):
    client = ModbusTcpClient(ip, port=port, timeout=10)
    # client.port = port
    portConnected = client.connect()
    print( "port: " + str(port) + " connected = " + str(portConnected))
    # logfile.write(str(client) + "\n")
    logfile.write("\nport: " + str(port) + " = " + str(portConnected))
    if (portConnected):
        try:
            # result = client.read_coils(1,1)
            # print (" Valid YAY " + result.bits[0])
            # logfile.write(" Valid YAY " + result.bits[0])

            error = client.write_coil(1, True)
            if error:
                print (" Valid YAY but? " + str(error))
                logfile.write(" Valid YAY but? " + str(error))
            else:
                print (" you dope head it actually worked")
                logfile.write(" Valid YAY ")

            error = None
            
            ip
        except Exception as e:
            # print (" but Invalid -- " + str(e))
            logfile.write(" but Invalid -- " + str(e))
            e = None
    portConnected = None
    return

while (port <= 8888):
    scanPort(port)
    port += 1
    
logfile.close()
