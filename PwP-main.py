import port_scanner as pscan
import tcp_proxy as tproxy
import tcp_server as tserver
import p_netcat as pnetcat

def main_menu():
    choice = raw_input("> ")

    if choice == "1":
        pscan.main()
    elif choice == "2":
        pnetcat.main()



main_menu()
