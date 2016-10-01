import port_scanner as pscan
import tcp_proxy as tproxy
import tcp_server as tserver
import p_netcat as pnetcat

print 'Welcome to Pentesting-with-Python'
print 'PwP is a simple framework providing basic toolkit'
print 'Available remote tools:'
print '\t1. TCP port scanner'
print '\t2. Netcat'
print '\t3. TCP server'
print '\t4. TCP proxy'
print '\n'
print 'Available local tools:'
print '\t1. Keylogger'

def main_menu():
    choice = raw_input("Select tool > ")

    if choice == "1":
        pscan.main()
    elif choice == "2":
        pnetcat.main()



main_menu()
