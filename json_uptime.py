#! /usr/bin/python2.7

import json
import subprocess
import argparse

def get_uptime():
    info = {}

    try:
        output = subprocess.check_output(["uptime"])
    except subprocess.CalledProcessError as e:
        print (e.output)
    else:
        output_list = output.split(',',3)
        info['timestamp'] = output_list[0].split()[0]
        days_running = output_list[0].split()[2]
        hours_running = output_list[1].strip()
        info['uptime'] = days_running + ' days, and ' + hours_running + ' hours'
        info['current_users'] = output_list[2].split()[0]
        load_average = output_list[3].split()
        info['load_average_1min'] = load_average[2].strip(',')
        info['load_average_5min'] = load_average[3].strip(',')
        info['load_average_15min'] = load_average[4]

    return info

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
