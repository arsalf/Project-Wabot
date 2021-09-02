from time import sleep
from modelWA import whatsapp

def main():
    myWa = whatsapp("arsal fadilah")
    timeout = 3
    while True:
        sleep(1.5)
        if myWa.isNewMsg(timeout):
            print("Ada pesan baru dari beda contact")
            myWa.sendRDC()
        elif myWa.isUpdateMsg():
            print("New message from active contact !!!")
            myWa.sendRSC()
            print("=====================================")
        else:
            print("Selama " + str(timeout) + " detik belum ada pesan baru")
            print("=====================================")
main()
