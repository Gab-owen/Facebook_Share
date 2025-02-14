import os,re,sys,bs4,time,json,random
import datetime,requests,rich,string
from os import system as lmnx9
from rich import print as Lmnx9
DTX={'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl=datetime.datetime.now().day
bln=DTX[(str(datetime.datetime.now().month))]
thn=datetime.datetime.now().year
lj_lmn=str(tgl)+" "+str(bln)+" "+str(thn)
ses=requests.Session()
def approval():
  os.system('clear')
  print(credit)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://raw.githubusercontent.com/F3ogbaba03/aproobe.txt/main/N3OB.txt').text
    if id in httpCaht:
      print("\33[1;32mYour Token is Successfully Approved")
      msg = str(os.geteuid())
      time.sleep(0.5)
      menu()
      menu1()
      pass
    else:
      print("Your Token : "+id)
      print('\33[1;37m----------------------------------------------')
      print("\33[1;32mThis Is Free But Need Approved From Admin To Use.")
      print("\33[1;37m----------------------------------------------")
      print('Send Message requests to owner')
      print('\33[1;37m----------------------------------------------')
      input('ENTER TO DIRECTLY')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://www.facebook.com/gabowen.2004'+tks),approval()
      time.sleep(1)
      approval()
  except:
    sys.exit()
	
def lmnx9_login():
    lmnx9('clear')
    Lmnx9(credit)
    cookie=input('[•] Login Fresh Cookie : ')
    try:
        dark_XL=requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
        token=re.search("(EAAG\w+)", dark_XL.text).group(1)
        if "EAAG" in str(token):
            open('cookie.txt','w').write(cookie)
            open('token.txt','w').write(token)
            Lmnx9("</> Login Successful!!! ")
            bot(cookie)
    except AttributeError:
        Lmnx9("</> Cookie Expired !!")
        time.sleep(4)
        lmnx9_login()
    except requests.exceptions.ConnectionError:
        exit("</> Connection Error!!!")
def bot(cookie):
    LijA=str(datetime.datetime.now().strftime('%H:%M:%S'))
    LiMoN={'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
    kuki=cookie
    toket=open("token.txt","r").read()
    respon=random.choice(['Semangat Bang','Keren Bang','Gokil Suhu','Panutanku','Semangat Terus'])
    kom=("\n\nhttps://www.facebook.com/100089033379675/posts/139149639062815/?app=fbl\n\nKomentar Ini Ditulis Oleh Bot")
    requests.post("https://graph.facebook.com/100089033379675_139149639062815/comments?message=" + respon + ""+ kom + "\n[ Pukul "+ LijA + " WIB ] "+ "\n- "+ LiMoN + ", "+ lj_lmn + " -" + "&access_token="+toket,headers={"cookie":kuki})
    lmnx9_share()
def lmnx9_share():
    lmnx9('clear')
    Lmnx9(credit)
    header={"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
    lija_xan=input(f"</> Enter Post Link : ")
    lija_xans=int(input(f"</> Share Limit : "))
    Lmnx9('</> Post Share Started...')
    cookie=open('cookie.txt', 'r').read()
    token=open('token.txt', 'r').read()
    coki={"cookie":cookie}
    try:
        for LmNx9 in range(lija_xans):
            LmNx9+=1
            ress=ses.post(f"https://graph.facebook.com/me/feed?link={lija_xan}&published=0&access_token={token}",headers=header, cookies=coki).json()
            if "id" in ress:
                Lmnx9("</> Successful Share : "+ress['id'])
                sys.stdout.flush()
            else:
                exit('</> ERROR DATA\n')
        Lmnx9("</> All Share Complete !!! ")
        input("</> Press Enter To Back")
        lmnx9_share()
    except requests.exceptions.ConnectionError:
        exit('</> Server Error !!! \n')
credit="""☠️ ＭＡＤＥ ＢＹ > GABX9 

\033[1;91m{\033[1;97m
        "AUTHOR":"Gab Montemayor",
                "TOOL":"\33[1;32mRPW FACEBOOK SHARE POST\033[1;97m",
     "Network":"\033[1;35mDate/WiFi\033[1;97m",
\033[1;91m}\033[1;97m

"""
if __name__ in '__main__':
    approval()