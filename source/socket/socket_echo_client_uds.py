#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Client half of echo example
"""
#end_pymotw_header

import socket
import sys

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './uds_socket'
print('connecting to %s' % server_address)
try:
    sock.connect(server_address)
except socket.error, msg:
    print(msg)
    sys.exit(1)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending "%s"' % message)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
