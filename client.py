import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # send 4096 bytes each time step
HOST_IP = "192.168.1.101"
PORT = 5001

s = socket.socket()

def openConnection():
    print("Opening Connection")
    s.connect((HOST_IP, PORT))

def closeConnection():
    print("Closing Connection")
    s.close()

def sendFile(fileAbsPath):
    fileSize = os.path.getsize(fileAbsPath)
    # send file info
    s.send(f"{fileAbsPath}{SEPARATOR}{fileSize}".encode())
    # send file data
    with open(fileAbsPath, "rb") as f:
        totalRead = 0
        while True:
            bytesRead = f.read(BUFFER_SIZE)
            if not bytesRead:
                # file transmitting is done
                print("File Transferred")
                break
            # we use sendall to assure transimission in busy networks
            totalRead += bytesRead
            print("Total Read = " + totalRead + " bytes")
            print("Percent Complete = " + (totalRead/fileSize) * 100 + " %")
            s.sendall(bytesRead)
