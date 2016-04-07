#! /usr/bin/python2.7

import json
import subprocess
import argparse

def get_uptime():
    uptime = ''

    try:
        output = subprocess.check_output(["uptime"])
    except subprocess.CalledProcessError as e:
        print (e.output)
    else:
        uptime = output.split()[2][0:-1]

    return {'uptime': uptime}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', required=False)
    args = parser.parse_args()
    
    json_string = json.dumps(get_uptime())

    if args.o:
        with open(args.o,'w') as outfile:
            outfile.write(json_string + '\n')
    else:
        print json_string
