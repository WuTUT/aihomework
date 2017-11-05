#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: recv.py
socket service
"""


import socket
import threading
import time
import sys
import os
import struct
from imgsr import recieve_img
from imgsr import send_img
from utils import object_detection_tutorial as odt
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print 'Waiting connection...'

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr):
    print 'Accept new connection from {0}'.format(addr)
    #conn.settimeout(500)
    conn.send('Hi, Welcome to the server!')

    while 1:
        filepath =recieve_img(conn)
        print filepath
        afterdect_name=odt.detect(filepath)
        print (afterdect_name)
        send_img(conn, afterdect_name)
        
        #conn.close()
        #break


if __name__ == '__main__':
    socket_service()
