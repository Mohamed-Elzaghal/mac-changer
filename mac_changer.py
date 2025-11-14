import subprocess
import optparse
import re

def banner():
    print(r"""
 █~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~  ███████╗██╗         ███████╗ █████╗  ██████╗ ██╗  ██╗ █████╗ ██╗       ~
# ~  ██╔════╝██║         ╚══███╔╝██╔══██╗██╔════╝ ██║  ██║██╔══██╗██║       ~
# ~  █████╗  ██║           ███╔╝ ███████║██║  ███╗███████║███████║██║       ~
# ~  ██╔══╝  ██║          ███╔╝  ██╔══██║██║   ██║██╔══██║██╔══██║██║       ~
# ~  ███████╗███████╗    ███████╗██║  ██║╚██████╔╝██║  ██║██║  ██║███████╗  ~
# ~  ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                > MAC CHANGER TOOL — ELZAGHAL <
    """)

def help_function():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="the interface that want to change it")
    parser.add_option("-m", "--mac", dest="new_mac", help="the new mac ")
    (options,agrumnts)=parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify the interface use--help for more info  ")
    elif not options.new_mac:
        parser.error("[-] please specify the new mac address use --help for more info")
    else:
        return options
    
def mac_changer(interface, new_mac):
    try:
        print("[+]changing the mac address to {}".format(new_mac))
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    except Exception as e:
        print(f"[-] error {e}")

def check(interface):
    cap=subprocess.check_output(["ifconfig", interface]).decode()
    se=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", cap)
    if se :
        return se.group(0)
    else:
        print("[-]could not find the mac address")

banner()
options= help_function()
current=check(options.interface)
mac_changer(options.interface, options.new_mac)
new_current=check(options.interface)
if current == new_current:
    print("THE MAC did NOT change! Something went wrong try ==> sudo.")
else:
    print("[+] MAC successfully changed ")
    print("{} ===> {}".format(current, new_current))
    
