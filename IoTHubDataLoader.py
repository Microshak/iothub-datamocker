from D2CMsgSender import IoTDataMsgSender
import time 
from BuildData import BuildData
connectionString = 'HostName=iothub-yhb5s.azure-devices.net;DeviceId=mikesdevice;SharedAccessKey=t0RiwgNTjND4MUoJYEm4toqXc4GaXSzcNZlR8IkmFTY='
MessagesToSend = 10000


if __name__ == '__main__':  
    
    IoTHubMsgSender = IoTDataMsgSender(connectionString)
    buildData = BuildData()
    template = buildData.loadTemplate("template.json")
    x = 0
    while(x < MessagesToSend):
        x = x+1
        message = buildData.getDistribution(template)
        sasToken =  IoTHubMsgSender.buildIoTHubSasToken()
        print(IoTHubMsgSender.sendD2CMsg(message,sasToken))
        print(message)
        time.sleep(1)




