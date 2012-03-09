# -*- coding: utf-8 *-*
import time, os, simplejson
def read(params):
    filename = 'data.txt';
    if 'timestamp' in params:
        last = params['timestapm']
    else:
        last = 0
    current = os.path.getmtime(filename)

    while current <= last:
        time.sleep(0.1)
        current = os.path.getmtime(filename)


    response = {}
    response['msg'] = open(filename).read()
    response['timestamp'] = current
    return simplejson.dumps(response)

def write(params):
    msg = params['msg']
    datafile = open('data.txt', 'a')
    datafile.write(msg)
    datafile.close()
    return ""
