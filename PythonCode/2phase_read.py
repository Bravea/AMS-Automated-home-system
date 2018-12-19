import serial
import binascii
import crcmod
import base64
import time
import datetime
#import socket


start = False
result = ""


ser = serial.Serial(
 port='/dev/ttyUSB0',
 baudrate = 2400,
 parity=serial.PARITY_EVEN,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)


def info(data):
    datalength = int(data[3:5],16)
    start1 =6;
    start2 =8;
    list = []
    for i in range(datalength):
     dataTekst=binascii.unhexlify(data[start1:start2])
     start1 = start1+3
     start2 = start2+3
     list.append(dataTekst)  
    tekst = ''.join(list) 
    return tekst


def output(data,type):
  s1 = str (data[3:5])
  s2 = str (data[6:8])
  s3 = str (data[9:11])
  s4 = str (data[12:14])
  value = s1+s2+s3+s4
  endValue =str(int(value,16))
  if type==1:
   
   return (endValue[:-1] + "," +endValue[-1:])

  if type==2:
   return endValue


def date(data):
    yearFirst  = str(data[6:8])
    yearSecond = str(data[9:11])
    year       = yearFirst+yearSecond
    year       = str(int(year,16))
    month      = str(int( data[12:14],16))
    day        = str(int( data[15:17],16))
    dayofweek  = str(int( data[18:20],16))
    hour       = str(int( data[21:23],16))
    minute     = str(int( data[24:26],16))
    second     = str(int( data[27:29],16))
    timestamp  = year+"-"+month+"-"+day+" "+hour+":"+minute+":"+second
    return timestamp

def logg(log):
    logfile = open("datalog2fas19April.txt", "a")
    logfile.write(log)
    logfile.close



def filewrite(responce):
    logfile = open("templog2fas19April.txt", "a")
    logfile.write(responce)
    logfile.close


def list(resultat):
    tid = resultat[51:92]
    tid2 =  time.time()
    st = datetime.datetime.fromtimestamp(tid2).strftime('%Y-%m-%d %H:%M:%S')  
    listLength = resultat[93:98]

    print "ListeID: " + listLength
    element = int((listLength[3:]),16)    
    print "tid(AMS): " + date(tid)
    print "tid(nettverk): " + st
   
    
    if element == 1:
     actPower = resultat[99:113]
     print "aktiv effekt: " + output(actPower,2) + " W"
     #clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #clientsocket.connect(('192.168.38.101',25000))
     #clientsocket.send("aktiv effekt: " + actPower)
     logg("Liste ID: 1 "+"\r"+ "tid: "+ date(tid) + "\r"+ "aktiv effekt:" + output(actPower,2)+" W"+ "\r\r")    
    
    	
    if element == 9: 
     obilList = resultat[99:125]
     meterID = resultat[126:179]
     meterType = resultat[180:209]
     aPower1 = resultat[210:224]
     aPower2 = resultat[225:239]
     rPower1 = resultat[240:254]
     rPower2 = resultat[255:269]
     iCurrent1 = resultat[270:284]
     uPhase1   = resultat[285:299]
          
   
     
     print "Liste 2 "
     print "Meterid: "+  info(meterID)
     print "obilist: "+info(obilList)
     print "Metertype: " + info(meterType)
     print "Active power1: "+ output(aPower1,2) + " W"
     print "Active power2: "+output(aPower2,2) + " W"  
     print "Reactive power1: "+output(rPower1,2)+ " VAr"
     print "Reactiv power2: "+output( rPower2,2)+" Var "
     print "Current1: "+ output(iCurrent1,2)+ " mA"
     print "Voltage phase1-2: "+output(uPhase1,1) +" Volt"

     #clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #clientsocket.connect(('192.168.38.101',25000))
     #clientsocket.send("Liste ID: 2 "+ "@"+ "tid: "+date(tid) + "@"+"tid(Nettverk): "+ st+" Meterid: "+info(meterID)+"@"+"obilist: "+ info(obilList)+"@"+"Metertype: " +info(meterType)+ "@"+ "aktiv effekt(inn): " + output(aPower1,2)+ " W"+"@"+ "Active effekt(ut): "+output(aPower2,2)
     #+ " W"+ "@" + "Reaktiv effekt(inn): "+output(rPower1,2)+ " VAr" +"@" +"Reaktiv effekt(ut): "+output(rPower2,2)+ " VAr" +"@"+  "Current1: "+ output(iCurrent1,2)+ " mA" + "@" +
     #"Voltage phase1-2: "+output(uPhase1,1) +" Volt" +  "@")

     logg("Liste ID: 2 "+"\r"+ "tid: "+date(tid) + "\r"+"tid(Nettverk): "+ st+  "\r"+"Meterid: "+info(meterID)+"\r"+"obilist: "+ info(obilList)+"\r"+"Metertype: " +info(meterType)+ "\r"+ "aktiv effekt(inn): " + output(aPower1,2)+ " W"+"\r"+ "Active effekt(ut): "+output(aPower2,2)
     + " W"+ "\r" + "Reaktiv effekt(inn): "+output(rPower1,2)+ " VAr" +"\r" +"Reaktiv effekt(ut): "+output(rPower2,2)+ " VAr" +"\r"+  "Current1: "+ output(iCurrent1,2)+ " mA" + "\r" 
     +"Voltage phase1-2: "+output(uPhase1,1) +" Volt" +  "\r\r")


     
       
    if element == 14:
     obilList = resultat[99:125]
     meterID = resultat[126:179]
     meterType = resultat[180:209]
     aPower1 = resultat[210:224]
     aPower2 = resultat[225:239]
     rPower1 = resultat[240:254]
     rPower2 = resultat[255:269]
     iCurrent1 = resultat[270:284]
     uPhase1   = resultat[285:299]
     clockmeter = resultat[300:341]
     importact = resultat[342:356]
     exportact = resultat[357:371]
     importreact = resultat[372:386]
     exportreact = resultat[387:401]
     
      
     
     print "Liste 3 "
     print "Meterid: "+info( meterID)
     print "obilist: "+ info( obilList)
     print "Metertype: " +  info(meterType)
     print "Active power1: "+ output(aPower1,2)
     print "Active power2: "+output(aPower2,2)
     print "Reactive power1: "+output(rPower1,2)
     print "Reactive power2: "+ output(rPower2,2)
     print "Current: "+ output(iCurrent1,2)
     print "Voltage phase1/2: "+ output(uPhase1,1)
     print "Clock and date in meter: "
     print  "kumulativ importert aktiv effekt paa 1 time: "
     print  "kumulativ eksportert aktiv effekt paa 1 time: "
     print  "kumulativ importert reaktiv effekt paa 1 time: "
     print  "kumulativ eksportert reaktiv effekt paa 1 time: "

     logg("Liste ID: 3 " + "\r"+ "tid: "+date(tid) + "\r"+"tid(Nettverk): "+ st+  "\r"+"Meterid: "+info(meterID)+"\r"+"obilist: "+ info(obilList)+"\r"+"Metertype: " +info(meterType)+ "\r"+ "aktiv effekt(inn): " + output(aPower1,2)+ " W"+"\r"+ "Active effekt(ut): "+output(aPower2,2)
     + " W"+ "\r" + "Reaktiv effekt(inn): "+output(rPower1,2)+ " VAr" +"\r" +"Reaktiv effekt(ut): "+output(rPower2,2)+ " VAr" +"\r"+  "Current1: "+ output(iCurrent1,2)+ " mA" + "\r" +
     "Voltage phase1-2: "+output(uPhase1,1) +" Volt" + "\r" + "tid: "+ date(clockmeter) +  "\r" + "akkumulert aktiv effekt(inn): "+output(importact,2)+ " W" + 
     "\r" + "akkumulert aktiv effekt(ut): "+output(exportact,2)+ " W" + "\r" + "akkumulert reaktiv effekt(inn): "+output(importreact,2)+ " VAr" +
     "\r" + "akkumulert reaktiv effekt(ut): "+output(exportreact,2)+ " VAr" + "\r\r")    
   


while True:
    tidnett =  time.time()
    stnett  = datetime.datetime.fromtimestamp(tidnett).strftime('%Y-%m-%d %H:%M:%S')
    response = ser.readline()
    if start == False:
     result = ''
     
    for i in range(len(response)):
     if start==False:
      startresult = binascii.hexlify(response[i]) + " "
 
     if startresult=="7e ":
      start = True
      startresult = ""

     
     if start==True :

      result = result + binascii.hexlify(response[i]) + " "
     
     if result[:5] == "7e 7e":
      result= result[3:]

    
    if (result[-4:]) == " 7e " and start==True  :
     filewrite(stnett+": " +  result+"\r")
     length = len(result)
     list(result)
     start = False
      
   
