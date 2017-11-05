#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: send.py
socket client
"""

import socket
import os
import sys
import struct
from imgsr import recieve_img
from imgsr import send_img
def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect_addr=raw_input('please input the ip you want to connect: ')
        s.connect((connect_addr, 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)

    print s.recv(1024)

    while 1:
        filepath = raw_input('please input file path: ')
        send_img(s, filepath)
        new_filename=recieve_img(s)        
        s.close()
        break


if __name__ == '__main__':
    socket_client()