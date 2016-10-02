import port_scanner as pscan
import tcp_proxy as tproxy
import tcp_server as tserver
import p_netcat as pnetcat
#import keylog as klog

print 'Welcome to Pentesting-with-Python'
print 'PwP is a simple framework providing basic toolkit \n'
print 'Available remote tools:'
print '\t1. TCP port scanner'
print '\t2. Netcat'
print '\t3. TCP server'
print '\t4. TCP proxy'
print '\n'
print 'Available local tools:'
print '\t5. Keylogger'

def main_menu():
    choice = raw_input("Select tool > ")

    if choice == "1":
        pscan.main()
    elif choice == "2":
        pnetcat.main()
    elif choice == "3":
        tserver.server()
    elif choice == "4":
        tproxy.main()
    else:
        print 'Command not recognised. Please select tool from the list'

main_menu()
