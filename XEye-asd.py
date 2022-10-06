#! /usr/bin/env python3
import scapy.all as sc
import subprocess,re,time
def udte():
    print("\n[Info] --> The XEye-asd tool will check for its updates, please wait .....\n\n")
    time.sleep(1)
    chupd = subprocess.check_output(['git','pull'])
    chked = re.search(r"Already up to date", str(chupd))
    chkeds = re.search(r"actualizado", str(chupd))
    bupted = re.search(r"changed,", str(chupd))
    if chked or chkeds:
        #print("\n[Congrats] --> the tool is "+str(chked[0].lower()))
        print("\n[Congrats] --> The XEye-asd tool on your PC is already up to date")
        time.sleep(1)
    else:
        print("\n[Info] --> The XEye-asd tool will be updated, please wait ...... \n")
        time.sleep(3)
        if bupted:
            print("\n[Congrats] --> XEye-asd on your machine is updated. Now bugs are fixed and more features added ")
            time.sleep(3)
            print("[Instruction] --> Please rerun XEye-asd so the updates will take effect.   Exiting ........")
            time.sleep(2)
            exit()
        else:
            print("\n[Warning] --> The tool couldn't be updated, please try again or reclone the tool by following the next instructions \n")
            time.sleep(3)
            print("\n[Instruction] --> Remove the \"XEye-asd\" folder by going up one directory and by running this command \"cd ..\" ")
            print("\n[Instruction] -->  then run this cmd \"rm -rf XEye-asd\" to remove the XEye-asd folder ")
            print("\n[Instruction] --> Run this command \"git clone https://github.com/Engmostafa26/XEye-asd.git\" ")
            print(" [Assistance] --> If you need any further assistance, please contact us on our Facebook page: https://facebook.com/XEyecs")
            exit()
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        udte()
    else:
        print("\n\n [Warning] --> You are not root - Please run the tool with \"sudo\" command \n ")
        exit()
def gmac(ip):
    areq = sc.ARP(ip)
    bcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    comb = bcast/areq
    snr = sc.srp(comb,timeout=1,verbose=False)[0]
    return snr[0][1].hwsrc
def sniff(iface):
    sc.sniff(iface=iface,store=False,prn=packets)
def packets(packet):
    if packet.haslayer(sc.ARP) and packet[sc.ARP].op == 2:
        try:
            try:
                rmac = gmac(packet[sc.ARP].psrc)
                resmac = packet[sc.ARP].hwsrc
                if rmac != resmac:
                    print("[Warning] --> Your are under attack......")
            except IndexError:
                pass
        except:
            print("\t\t\t\t[*] Thanks for using XEye-asd. Below are our Ethical Hacking courses recommended for you:) [*]")
            print("\n [***] --> The Ultimate Social Media OSINT Hacking Bundle: https://rb.gy/xgrdmv")
            print(" [***] --> Instagram OSINT Hacking for Ethical Hackers and OSINTeers: https://rb.gy/glnllu")
            print(" [***] --> Facebook OSINT Hacking for Ethical Hackers and OSINTeers: https://rb.gy/ymzseh")
            print(" [***] --> Twitter OSINT Hacking for Ethical Hackers and OSINTeers: https://rb.gy/hogdor")
            print(" [***] --> The Optimal Introduction to Ethical Hacking: https://rb.gy/kanwhs")
            print(" [***] --> Kali Linux For Ethical Hackers and Penetration Testers: https://rb.gy/cyw562")
            print("*******************************************************************************************************")
            print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
            exit()
iface = input("[Required] --> Please enter the Interface to check on ")
sniff(str(iface))
