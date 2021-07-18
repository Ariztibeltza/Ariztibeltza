import os

message_stream = os.popen('docker ps') 
message_stream.read()