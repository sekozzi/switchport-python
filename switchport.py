#!/usr/bin/python
import os, re, sys, subprocess, shlex

versioncheck = sys.version_info[0]
interface = str(sys.argv[1])

def switchportV2(interface):    
    cmd = "tcpdump -nn -v -i {0} -s 1500 -c 1 'ether[20:2] == 0x2000'".format(interface)
    p1 = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(['egrep', 'Device-ID|Port-ID|VLAN'], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.stdout.close()    
    outs, err = p.communicate()
    outs = outs.split('\n')
    out = []
    for line in outs:
        out.append(line)

    #Switch bilgi alinip, parse edilir. // to get switch information and parse
    switch = str(out[0])
    switch = re.findall("[A-Za-z-]+[0-9]+[A-Z]+[0-9]+", switch)
    switch = switch[0]

    #Port bilgisi alinip, parse edilir. // to get port information and parse
    port = str(out[1])
    port = re.findall("[A-z-]+[0-9]+[[0-9]+[\W]+[0-9]+[\W]+[0-9]+", port)
    if len(port) == 0:
        port = str(out[1])
        port = re.findall("[A-z]+[0-9]+[\W]+[0-9]+", port)
    port = port[0]

    #Vlan bilgisi alininir, parse edilir. // to get vlan information and parse
    vlan = str(out[2])
    vlan = re.findall("[0-9]+", vlan)
    vlan = vlan[3]

    print('Switch: ' + switch)
    print('Port: ' + port)
    print('Vlan: ' + vlan)

def switchportV3(interface):
    cmd = "tcpdump -nn -v -i {0} -s 1500 -c 1 'ether[20:2] == 0x2000'".format(interface)
    p1 = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(['egrep', 'Device-ID|Port-ID|VLAN'], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.stdout.close()
    outs, err = p.communicate()
    outs = outs.split(b'\n')
    out = []
    for line in outs:
        out.append(line)

    #Switch bilgi alinip, parse edilir.
    switch = str(out[0])
    switch = re.findall("[A-Za-z-]+[0-9]+[A-Z]+[0-9]+", switch)
    switch = switch[0]

    #Port bilgisi alinip, parse edilir.
    port = str(out[1])
    port = re.findall("[A-z-]+[0-9]+[[0-9]+[\W]+[0-9]+[\W]+[0-9]+", port)
    if len(port) == 0:
        port = str(out[1])
        port = re.findall("[A-z]+[0-9]+[\W]+[0-9]+", port)
    port = port[0]

    #Vlan bilgisi alininir, parse edilir.
    vlan = str(out[2])
    vlan = re.findall("[0-9]+", vlan)
    vlan = vlan[3]
    
    print('Switch: ' + switch)
    print('Port: ' + port)
    print('Vlan: ' + vlan)
    
if versioncheck == 2:
    switchportV2(interface)
elif versioncheck == 3:
    switchportV3(interface)
