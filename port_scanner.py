#
#
# Simple TCP port scanner. Performs TCP full connection using socket library
#
# Based on implementation presented in 'Violent Python' by TJ O'Connor
#

import optparse
from socket import *
from threading import *
screenLock = Semaphore(value = 1)

def scanner(target_host, target_port):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((target_host, target_port))
        conn.send("Scanning\r\n")
        results = conn.recv(100)
        screenLock.acquire()
        print "[*]%d/ TCP open" % target_port
        print "[*]" + str(results)

    except:
        screenLock.acquire()
        print "[-]%d/ TCP closed" % target_port
    finally:
        screenLock.release
        conn.close()

def portScan(target_port, target_host):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print "[-] Cannot resolve '%s': unknown host" % target_host
        return

    try:
        target_name = gethostbyname(target_ip)
        print "\n [*] Scan reults for: " + target_name
    except:
        print "\n [*] Scan results for " + target_ip

    setdefaulttimeout(1)

    for target_port in target_ports:

        t = Thread(target = scanner, args = (target_host, int(target_port)))
        t.start()

def main():
    parser = optparse.OptionParser("usage port_scanner.py " + "-H <target host> -p <target port>")
    parser.add_option("-H", dest = "target_host", type = "string", help = "specify target host")
    parser.add_option("-p", dest = "target_port", type = "string", help = "specify target pors separated by comma")
    (options, args) = parser.parse_args()
    target_host = options.target_host
    target_port = str(options.target_port).split(", ")

    if (target_host == None) or (target_port == None):
        print parser.usage
        exit(0)

    portScan(target_host, target_port)

if __name__ == "__main__":
    main()
