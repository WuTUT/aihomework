#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: .py
send and recieve img function
"""

import socket
import threading
import time
import sys
import os
import struct

def recieve_img(conn):
    fileinfo_size = struct.calcsize('128sl')
    buf = conn.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('128sl', buf)
        fn = filename.strip('\00')
        new_filename = os.path.join('./', fn)
        print 'file new name is {0}, filesize if {1}'.format(new_filename,
                                                                 filesize)

        recvd_size = 0  # 定义已接收文件的大小
        fp = open(new_filename, 'wb')
        print 'start receiving...'

        while not recvd_size == filesize:
            if filesize - recvd_size > 1024:
                data = conn.recv(1024)
                recvd_size += len(data)
            else:
                data = conn.recv(filesize - recvd_size)
                recvd_size = filesize
            fp.write(data)
        fp.close()
    print 'end receive...'
    return new_filename
def send_img(s,filepath):
    if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', os.path.basename(filepath),
                                os.stat(filepath).st_size)
            s.send(fhead)
            print 'client filepath: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print '{0} file send over...'.format(filepath)
                    break
                s.send(data)