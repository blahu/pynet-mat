#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    sys.exit( "Usage: " + sys.argv[0] + " <ip address>")

ip = sys.argv[1]

l = ip.split(".")
if (len(l) != 4):
    sys.exit( "Not an IP address: " + ip)

# blink list to store binary ip
bin_ip = []

for byte in l:   

    # check if bytes are 0..255
    if int(byte) > 255:
        sys.exit("Not an IP address: " + ip)

    # convert to binary and strip of first "0b"
    just_byte = bin(int(byte))[2:]

    # calulate padding of "0s"
    padding = "0" * (8 - len(just_byte))

    # add to list
    bin_ip.append(padding + just_byte)

# join the list making it dotted format
bin_ip = ".".join(bin_ip)

print "%-20s %-35s" %("IP address", "Binary",)
print "%-20s %-35s" %(ip, bin_ip,)