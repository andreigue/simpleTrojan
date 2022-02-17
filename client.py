import socket
import os
import time

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step
HOST_IP = "0.tcp.ngrok.io" # public IP address of server 
PORT = 11065

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket established=======================================")
print(s)

def openConnection():
    print("Opening Connection")
    s.connect((HOST_IP, PORT))
    print("Connection established")

def closeConnection():
    print("Closing Connection from client side")
    s.close()

def sendFile(fileAbsPath):
    print("absolute path: " + fileAbsPath)
    fileSize = os.path.getsize(fileAbsPath)
    # send file info
    print(str(s) + "===================inside sendFile()")
    s.send(f"{fileAbsPath}{SEPARATOR}{fileSize}".encode())
    time.sleep(2)
    # send file data
    with open(fileAbsPath, "rb") as f:
        totalRead = 0
        while True:
            dataRead = f.read(BUFFER_SIZE)
            if not dataRead:
                # file transmitting is done
                print("File Transferred")
                break
            # we use sendall to assure transimission in busy networks
            # totalRead += len(dataRead)
            # print("Total Read = " + str(totalRead) + " bytes")
            # print("Percent Complete = " + str((totalRead/fileSize) * 100) + " %")
            s.sendall(dataRead)

# openConnection()
# # sendFile('C:\\Users\\Chris\\Desktop\\bank.txt')
# closeConnection()