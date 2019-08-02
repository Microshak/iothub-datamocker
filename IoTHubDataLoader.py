from D2CMsgSender import IoTDataMsgSender
import time 
from BuildData import BuildData
connectionString = 'HostName=iothub-k3s3b.azure-devices.net;DeviceId=NewMikesDevice;SharedAccessKey=BY5HdQTm5fKaJF0RhkMZq6N6iMqfFyrd/yq87onJTMo='
connectionString2 = 'HostName=iothub-k3s3b.azure-devices.net;DeviceId=MikesNewDevice2;SharedAccessKey=Kwnl/JM88Xs70FPI341MK3iDRCohI5lxl3xO8zdztLE='
MessagesToSend = 1000000


if __name__ == '__main__':  
    
   
    buildData = BuildData()
    template = buildData.loadTemplate("template.json")
    IoTHubMsgSender = IoTDataMsgSender(connectionString)
    m1 = IoTDataMsgSender(connectionString)
    m2 = IoTDataMsgSender(connectionString2)
    x = 0
    while(x < MessagesToSend):
        x = x+1
        if x % 2 == 0:
            IoTHubMsgSender = m2
        else:
            IoTHubMsgSender = m1

        message = buildData.getDistribution(template)
        sasToken =  IoTHubMsgSender.buildIoTHubSasToken()
        print(IoTHubMsgSender.sendD2CMsg(message,sasToken))
        print(message)
        time.sleep(.2)




