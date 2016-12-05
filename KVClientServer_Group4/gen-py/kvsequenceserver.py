'''
Group Number: 4

#kvserver.py;

TeamMembers:
Rahul Reddy (rra304)
Suraj Patel (skp392)
Jubin Soni  (jas1464)
Balaji Reddy(bbr234)
'''

import sys
sys.path.append('gen-py')
import socket
import threading
from thrift import Thrift
from kvSequencer import SequenceService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
host = socket.gethostname()

class kvsequence:
    currentsequence = 0
    result = currentsequence
    lock = threading.Lock()

    def getnextsequenceid(self):
        print("service request came")
        with self.lock:
            self.result = self.currentsequence
            self.currentsequence += 1
            print ("Curre ID which is being given now:%d - next: %d" % (self.result,self.currentsequence))
            return self.result


if __name__ == "__main__":
    try:
        handler = kvsequence()
        processor = SequenceService.Processor(handler)
        transport = TSocket.TServerSocket(port=10100)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        print("Starting Server: %s"%host)
        server.serve()
        print("Done.")

    except Exception as err:
        print("Error: %s" %str(err))
