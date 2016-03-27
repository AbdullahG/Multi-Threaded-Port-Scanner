import _thread as thread,time,socket
from threading import Lock
import traceback


lock = Lock()

end = 65535
total_count = 0
server = "example.com"
openPorts = []

def scanport(name,num):
    global total_count
    global end
    global openPorts
    while total_count < end:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            lock.acquire()
            port = total_count
            total_count+=1
            lock.release()
            s.connect((server,port))
            print(server+": Port",str(port),"is open *")
            lock.acquire()
            openPorts.append(port)
            lock.release()
            s.close()
        except:
            pass

def startThreads(num):
    threads = []
    for i in range(num):
        try:
            threads.append(thread.start_new_thread(scanport,("Thread",i)))
        except:
            traceback.print_exc()
            print("unable to start thread",i)
    print("Total Thread Number:",len(threads))


start_time = str(time.ctime())

startThreads(5000)
while total_count < end:
    pass

print("Started in:",start_time,"End:",str(time.ctime()))
print("open port number:",len(openPorts))
for i in openPorts:
    print(i,end=",")
