from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#automatic open chrome driver when whatsapp class created

#use specific profile chrome
# options = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data")
# options.add_argument('--profile-directory=Profile 3')
# driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe', chrome_options=options)

#use default chromedriver
path = 'C:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(path)

#get address wa web
driver.get("https://web.whatsapp.com/")

class whatsapp:
    lastMsg = ""

    def __init__(self, name):
        self.name = name

    def setLastMsg(self, newMsg):
        self.lastMsg = newMsg

    def clickMSg(self, notif):
        try:
            print("klik kontak pengirim")
            notif.click()
        except:
            print("Gagal Klik")

    def getMsg(self):
        msg = ""
        try:
            for msgIn in driver.find_elements_by_class_name("message-in"):
                msgIn = msgIn.find_elements_by_class_name("_1Gy50")
                msgIn = msgIn[len(msgIn)-1]
                msg = msgIn.text
        except:
            print("Can't found last message")

        return msg

    def isNewMsg(self, to):
        print("Mengecek pesan baru . . .")
        try:
            element = WebDriverWait(driver, to).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_23LrM"))
            )
        except:            
            return False
        return True

    def isEmptyMsg(self, str):
        if(len(str) == 0):
            return True
        return False

    def isUpdateMsg(self):
        updateMsg = self.getMsg()
        if (self.lastMsg != updateMsg) and (not self.isEmptyMsg(updateMsg)):
            self.lastMsg = updateMsg
            return True

        return False

    def processMsg(self, msgIn):
        msg = msgIn.lower()
        responseMsg = "Maaf, bahasa anda tidak kami kenali :("
        if msg.find("hello") != -1:
            responseMsg = "Hai, "
        
        if msg.find("hai") != -1:
            responseMsg = "Hello, "

        if msg.find("?") != -1:
            responseMsg += "Mohon maaf. Layanan belum bisa memproses pertanyaan anda! "    
        
        return responseMsg

    def postMsg(self, msg):
        try:
            textInput = driver.find_elements_by_class_name("_13NKt")
            textInput[len(textInput)-1].send_keys(msg)
            try:
                send = driver.find_element_by_class_name("_4sWnG")
                send.click()
            except:
                print("Gagal Klik")
        except:
            print("tidak bisa input")
        print("Response me : " + msg)

    #mengirimi jawaban ke kontak yang berbeda
    def sendRDC(self):
        contacts = driver.find_elements_by_class_name('_23LrM')
        for notif in contacts:
            self.clickMSg(notif)
            self.lastMsg = self.getMsg()
            print("Pesan terakhir adalah : " + self.lastMsg)
            self.postMsg(self.processMsg(self.lastMsg))
            print("=====================================")
    
    #mengirimi jawaban ke kontak yang sama atau active
    def sendRSC(self):
        print("Pesan terakhir adalah : " + self.lastMsg)
        self.postMsg(self.processMsg(self.lastMsg))