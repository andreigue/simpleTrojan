import socket
import os

# device's IP address
SERVER_HOST = "0.0.0.0" # private IP address
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server TCP socket
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

def singleFileDownload():
    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    fileName, fileSize = received.split(SEPARATOR)
    # remove absolute path if there is
    fileName = os.path.basename(fileName)
    # convert to integer
    fileSize = int(fileSize)
    
    if fileSize == 0:
        return
    with open(fileName, "wb") as f:
        totalRead = 0
        while (totalRead/fileSize) < 1:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                print("Done transferring "+fileName)    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            totalRead += len(bytes_read)
            print("Total Read = " + str(totalRead) + " bytes")
            print("Percent Complete = " + str((totalRead/fileSize) * 100) + " %")
           
# read and write files separately           
while True:
    singleFileDownload()

# close the client socket
client_socket.close()
print("closing client socket from server side")
# close the server socket
s.close()