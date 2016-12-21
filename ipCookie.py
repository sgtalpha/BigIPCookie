#!/usr/bin/env python

import argparse

# Create arguments for the script.
parser = argparse.ArgumentParser()
parser.add_argument("-c", dest="COOKIE", help="Specify the F5 BIG IP Cookie value")
args = parser.parse_args()

# Obtain the F5 BIG IP cookie (BIGipServer***) value from the argument.
cookie = args.COOKIE

# Require cookie: if not present, display error message and exit.
if cookie is None:
    print "You must specify the cookie using the '-c' argument. \nSee --help for assistance."
    raise SystemExit()

# Split input into an array so we can single out the IP and port info.
array = cookie.split('.')

#################
## Find the IP ##
#################

# Convert the decimal array[0] (which holds the IP) to hex.
ipHex = hex(int(array[0]))[2:]

# Split the hex into an array consisting of 2 bytes each.
ipHexArray = []
for index in range(0, len(ipHex), +2):
    ipHexArray.append(ipHex[index:index+2])

# Reverse the order of the array.
ipReverseHexArray = ipHexArray[::-1]

# Convert the hex array into a decimal array.
ipDecArray = []
for i in ipReverseHexArray:
    ipDecArray.append(int(i,16))

# Join the array, seperating each item by a "." to recreate the IP address. 
ipAddress = ".".join(str(octet) for octet in ipDecArray)

###################
## Find the port ##
###################

# Convert the decimal to hex for array[1] (the port).
portHex = hex(int(array[1]))[2:]

# Split the hex into an array consisting of 2 bytes each.
portHexArray = []
for index in range(0, len(portHex), +2):
    portHexArray.append(portHex[index:index+2])

# Reverse the order of the array.
portReverseHexArray = portHexArray[::-1]

# Join the hex array with no seperation.
portJoinHex = "".join(str(byte) for byte in portReverseHexArray)

# Convert the hex into a decimal.
port = int(portJoinHex,16)

#############
## RESULTS ##
#############

print "The F5 BIG IP cookie value you entered was: \n", cookie, "\n"
print "The IP Address and Port infomration is as follows: \n", str(ipAddress) + ":" + str(port), "\n"

