import os
import random
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["|","/","-","\\"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()

    def terminate(self,excuse):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{excuse}", flush=True)

random_text = "This is a security web where you are now trapped you cannot find where the actual data is stored unless you are the owner as there are too many files and folders to go through and I dont think you are here to waste your time in such a pathetic task right So just get the hell out of here otherwise someone will catch you like this and you wont be able to escape then Thank you for considering my humble web Have a nice day"
list_text = random_text.split(" ")
list_file_type = [".mkv",".jpg",".mp4",".avi",".png",".txt",".py",".cpp",".doc",".zip",".dmg",".exe",".gif",".php",".tar",".wim",".xap",".cad"]

class Creation:
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.thread_list = []
        self.path = os.path.join(".",self.name)
        self.thread_count = 16
        
    def create_dummy(self,sub):
        if len(os.listdir(sub)) == 0:
            for j in range(len(list_text)):
                file_path = os.path.join(sub,list_text[j])
                f = open(file_path+random.choice(list_file_type),"w")
                f.write("Now the file has more content!")
                f.close()

    def create_folder(self,start,end):
        for k in range(start,end):
            name = "{:03d}".format(k)
            subDir = os.path.join(self.path,str(name))
            if not os.path.isdir(subDir):
                try: 
                    os.mkdir(subDir)
                except OSError as error: 
                    print(error)
            if(self.sub2>0):
                for k2 in range(self.sub2):
                    name2 = "{:02d}".format(k2)
                    subDir2 = os.path.join(subDir,str(name2))
                    if not os.path.isdir(subDir2):
                        try: 
                            os.mkdir(subDir2)
                        except OSError as error: 
                            print(error)
                    if(self.sub3>0):
                        for k3 in range(self.sub3):
                            name3 = "{:01d}".format(k3)
                            subDir3 = os.path.join(subDir2,str(name3))
                            if not os.path.isdir(subDir3):
                                try: 
                                    os.mkdir(subDir3)
                                except OSError as error: 
                                    print(error)
                            self.create_dummy(subDir3)
                    else:
                        self.create_dummy(subDir2)
            else:
                self.create_dummy(subDir)

    def create_virus(self):
        excuse = None
        
        if not os.path.isdir(self.path):
            try: 
                os.mkdir(self.path) 
            except OSError as error: 
                print(error)
        else:
            excuse = "dir already exists"
            return excuse
        
        if(self.sub1>0):
            x =self.sub1
            for i in range(0,x,max(1,x//self.thread_count)):
                print("creating folder from ",i,">",min(x,i-1+max(2,x//self.thread_count)))
                thread = Thread(target=self.create_folder,args=(i,min(x,i-1+max(2,x//self.thread_count))),daemon=True) 
                thread.start()
                self.thread_list.append(thread)
            for thread in self.thread_list:
                thread.join()

        else:
            excuse = "Insufficient number of 1st level Sub directories"
        return excuse

class Heaven:
    def __init__(self,dir):

        self.f = open(os.path.join(".",dir,"heaven.py"),"w")

    def change_to_be_hex(self,s):
        s = s.encode('utf-8')
        return int(s.hex(),16)
        
    def xor_two_str(self):
        a = self.change_to_be_hex(self.path)
        b = self.change_to_be_hex(self.passkey)
        return hex(a ^ b)
    
    def encrypt(self,passkey,path):
        self.passkey = passkey
        print(passkey)
        self.path = path
        print(path)
        self.cipher_text = " "+bytes.fromhex(self.xor_two_str()[2:]).decode('utf-8')+" "

    def create_file(self):
        code = """
import os
import webbrowser
cipher_text = "{}"
def change_to_be_hex(s):
    s = s.encode('utf-8')
    return int(s.hex(),16)
    
def xor_two_str(str1,str2):
    a = change_to_be_hex(str1)
    b = change_to_be_hex(str2)
    return hex(a ^ b)
def check(passkey):
    if(not (passkey and not passkey.isspace())):
        return False
    else:
        return True
def decrypt(passkey):
    return  bytes.fromhex(xor_two_str(passkey,cipher_text[1:-1])[2:]).decode('utf-8')
while(1):
    passkey = input("Enter your passkey: ")
    if(check(passkey)):
        path = decrypt(passkey)
        dirs = path.split("&")
        if(len(dirs)==3):
            dir = os.path.join(dirs[0],dirs[1],dirs[2])
            if(os.path.isdir(dir)):
                webbrowser.open(os.path.realpath(dir))
                break
            else:
                print("invalid key\\n")
        else:
            print("invalid key\\n")
    else:
        print("invalid input\\n")
""".format(self.cipher_text)

        self.f.write(code)

        return self.f
    

def main():
    start = input("Do you want to create an anti-malicious system inorder to enhance your privacy?\nYes - to continue\nNo - to cancel\nPlease input your choice: ")
    if(start == 'Yes' or start == 'yes' or start == 'y' or start == 'Y'):
        s = input("Enter a dir name: ")
        name = "".join(x for x in s if (x.isalnum() or x=='_' or x==" "))
        # print(name)
        
        while(1):
            sub1 = input("Enter the number of 1st level sub dir you want (limit 1000): ")
            if(not sub1.strip().isdigit()):
                print("Please enter a interger input\n")
            elif( not int(sub1) in range(1,1001)):
                print("Please provide an input within the given range\n")
            elif(int(sub1) in range(1,1001)):
                sub1 = int(sub1)
                break
            else:
                print("Invalid input")

        while(1):
            sub2 = input("Enter the number of 2nd level sub dir you want (limit 100): ")
            if(not sub2.strip().isdigit()):
                print("Please enter a interger input\n")
            elif( not int(sub2) in range(0,101)):
                print("Please provide an input within the given range\n")
            elif(int(sub2) in range(0,101)):
                sub2 = int(sub2)
                break
            else:
                print("Invalid input")

        while(1):
            sub3 = input("Enter the number of 3rd level sub dir you want (limit 10): ")
            if(not sub3.strip().isdigit()):
                print("Please enter a interger input\n")
            elif( not int(sub3) in range(0,11)):
                print("Please provide an input within the given range\n")
            elif(int(sub3) in range(0,11)):
                sub3 = int(sub3)
                break
            else:
                print("Invalid input")
        
        waiting = Loader("Creating your privacy ","Thanks for your patience! Work is now done",0.05).start()
        creation = Creation(name,sub1,sub2,sub3)
        excuse = creation.create_virus()
        # excuse = None
        if(excuse == None):
            waiting.stop()
            print("Well in this security system we have provided you with a large amount of dummy folder to keep your actual private file secure.\n"+
            "As accessing a particular folder could be a hactic task for you as well so we have created a simple system for that as well.\n"+
            "You just need to enter the directories number till the end and a passkey to keep it quickly accessible\n")
            while(1):
                subd1 = input("Enter your 1st directory number (0,{})".format(str(sub1)))
                if(not subd1.strip().isdigit()):
                    print("Please enter a interger input\n")
                elif( not int(subd1) in range(0,sub1)):
                    print("Please provide an input within the given range\n")
                elif(int(subd1) in range(0,sub1)):
                    break
                else:
                    print("Invalid input")
            while(1):
                if(sub2==0):
                    subd2 =0
                    break
                subd2 = input("Enter your 2nd directory number (0,{})".format(str(sub2)))
                if(not subd2.strip().isdigit()):
                    print("Please enter a interger input\n")
                elif( not int(subd2) in range(0,sub2)):
                    print("Please provide an input within the given range\n")
                elif(int(subd2) in range(0,sub2)):
                    break
                else:
                    print("Invalid input")
            while(1):
                if(sub3==0):
                    subd3 =0
                    break
                subd3 = input("Enter your 3rd directory number (0,{})".format(str(sub3)))
                if(not subd3.strip().isdigit()):
                    print("Please enter a interger input\n")
                elif( not int(subd3) in range(0,sub3)):
                    print("Please provide an input within the given range\n")
                elif(int(subd3) in range(0,sub3)):
                    break
                else:
                    print("Invalid input")

            secret_path = "{:03d}".format(int(subd1))+"&"+"{:02d}".format(int(subd2))+"&"+"{:01d}".format(int(subd3))
            
            passkey = input("Now Insert your passkey and do remember it to easily access your folder: ")
            heaven = Heaven(name)
            heaven.encrypt(passkey,str(secret_path))
            heaven.create_file()
            print("Along with your super private security system a file name {'heaven.py'} is created which will let you to your secrets! Just run it and enter your key!")
        else:
            waiting.terminate(excuse)
    else:
        print("If not safe out there! Its highly recommended to use this system to create your own privacy system!")


if __name__ == "__main__":
    main()

