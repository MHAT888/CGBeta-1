EmailsFile = "emails.txt"
JsonFile = "m1.json"


EmailsPassword="nnnnnn"
CommunityLink="http://aminoapps.com/c/zerozero1"


import os
import time
import random
import requests
import json


import hmac
import base64


try:
	import colorama
except ModuleNotFoundError:
	os.system("pip install colorama")

try:
	import pyfiglet
except ModuleNotFoundError:
	os.system("pip install pyfiglet")

try:
	import json_minify
except ModuleNotFoundError:
	os.system("pip install json_minify")

try:
	import threading
except ModuleNotFoundError:
	os.system("pip install threading")

try:
	import flask
except ModuleNotFoundError:
	os.system("pip install flask")


from json_minify import json_minify
from threading import Thread
from flask import Flask
from colorama import Fore, Style


from hashlib import sha1


A = "\033[1;91m"
E = "\033[1;92m"
H = "\033[1;93m"
L = "\033[1;95m"
X = '\033[2;36m'
M = "\033[1;94m"
B = "\033[1;90m"
C = "\033[1;97m"


select = input(f"{A}[ 1 ] 𝔧𝔰𝔬𝔫 𝔣𝔦𝔩𝔢\n{E}[ 2 ] 𝔱𝔵𝔱 𝔣𝔦𝔩𝔢\n\n{C}𝔰𝔢𝔩𝔢𝔠𝔱\n》")



os.system("clear")



app = Flask('')
@app.route('/')
def home():
	return 'YOUR IN !!!'
def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000))
def keep_alive():
	t = Thread(target=run)
	t.start()



class Main:
	def __init__(self):
		self.time = self.time();self.device = self.device();self.api = "https://service.aminoapps.com/api/v1";self.headers = {"NDCDEVICEID": self.device,"Accept": "*/*","NDCLANG": "ar","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-GB,3n;q=0.9","Content-Type": "application/json","User-Agent":"Apple iPad6,12 iPadOS v15.4.1 Main/3.14.0","Connection":"keep-alive"};self.comId =int(self.comId(CommunityLink)['linkInfoV2']['extensions']['community']['ndcId']);self.sid = None
	
	def time(self):
		hour=time.strftime("%H", time.gmtime()); minute=time.strftime("%M", time.gmtime());
		UTC={"GMT0":'+0', "GMT1":'+60', "GMT2":'+120', "GMT3":'+180', "GMT4":'+240', "GMT5":'+300', "GMT6":'+360', "GMT7":'+420', "GMT8":'+480', "GMT9":'+540', "GMT10":'+600', "GMT11":'+660', "GMT12":'+720', "GMT13":'+780', "GMT-1":'-60', "GMT-2":'-120', "GMT-3":'-180',"GMT-4":'-240', "GMT-5":'-300', "GMT-6":'-360', "GMT-7":'-420', "GMT-8":'-480', "GMT-9":'-540', "GMT-10":'-600', "GMT-11":'-660'}; Hour = [hour, minute]
		if Hour[0]=="00":tz=UTC["GMT-1"];return int(tz)
		if Hour[0]=="01":tz=UTC["GMT-2"];return int(tz)
		if Hour[0]=="02":tz=UTC["GMT-3"];return int(tz)
		if Hour[0]=="03":tz=UTC["GMT-4"];return int(tz)
		if Hour[0]=="04":tz=UTC["GMT-5"];return int(tz)
		if Hour[0]=="05":tz=UTC["GMT-6"];return int(tz)
		if Hour[0]=="06":tz=UTC["GMT-7"];return int(tz)
		if Hour[0]=="07":tz=UTC["GMT-8"];return int(tz)
		if Hour[0]=="08":tz=UTC["GMT-9"];return int(tz)
		if Hour[0]=="09":tz=UTC["GMT-10"];return int(tz)
		if Hour[0]=="10":tz=UTC["GMT13"];return int(tz)
		if Hour[0]=="11":tz=UTC["GMT12"];return int(tz)
		if Hour[0]=="12":tz=UTC["GMT11"];return int(tz)
		if Hour[0]=="13":tz=UTC["GMT10"];return int(tz)
		if Hour[0]=="14":tz=UTC["GMT9"];return int(tz)
		if Hour[0]=="15":tz=UTC["GMT8"];return int(tz)
		if Hour[0]=="16":tz=UTC["GMT7"];return int(tz)
		if Hour[0]=="17":tz=UTC["GMT6"];return int(tz)
		if Hour[0]=="18":tz=UTC["GMT5"];return int(tz)
		if Hour[0]=="19":tz=UTC["GMT4"];return int(tz)
		if Hour[0]=="20":tz=UTC["GMT3"];return int(tz)
		if Hour[0]=="21":tz=UTC["GMT2"];return int(tz)
		if Hour[0]=="22":tz=UTC["GMT1"];return int(tz)
		if Hour[0]=="23":tz=UTC["GMT0"];return int(tz)
	
	def sig(self, data):
		return base64.b64encode(bytes.fromhex("19") + hmac.new(bytes.fromhex("DFA5ED192DDA6E88A12FE12130DC6206B1251E44"), data.encode("utf-8"), sha1).digest()).decode("utf-8")
	
	def device(self):
		identifier = os.urandom(20)
		return ("19" + identifier.hex() + hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, sha1).hexdigest()).upper()
	
	def log(self, email: str, password: str):
		data = json.dumps({"email": email, "secret": f"0 {password}", "deviceID": self.device, "clientType": 100, "action": "normal", "timestamp": (int(time.time() * 1000))})
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/g/s/auth/login", data = data, headers = self.headers)
		try:self.sid = request.json()["sid"]
		except:pass
		return request.json()
	
	def comId(self, CommunityLink):
		return requests.get(f'{self.api}/g/s/link-resolution?q={CommunityLink}',headers = self.headers).json()
	def join(self, comId: int):
		data = json.dumps({"timestamp": int(time.time()*1000)})
		self.headers["NDC-MSG-SIG"] = self.sig(data=data)
		request = requests.post(f"{self.api}/x{comId}/s/community/join?sid={self.sid}", data = data, headers = self.headers)
		return request.json()
	
	def check_in(self, comId: int, timezone: int):
		data = json.dumps({"timezone": timezone, "timestamp": int(time.time() * 1000)})
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/x{comId}/s/check-in/lottery?sid={self.sid}", data = data, headers = self.headers)
		return request.json()
	
	def send_time(self, comId: int, start: int = None, end: int = None, timers: list = None, timezone: int=None ):
		data = {"userActiveTimeChunkList": [{"start": start, "end": end}], "timestamp": int(time.time() * 1000), "optInAdsFlags": 2147483647, "timezone": timezone}
		if timers: data["userActiveTimeChunkList"] = timers
		data = json_minify(json.dumps(data))
		self.headers["NDC-MSG-SIG"] = self.sig(data = data)
		request = requests.post(f"{self.api}/x{comId}/s/community/stats/user-active-time?sid={self.sid}", data = data, headers = self.headers)
		return request.json()

class Run:
	def __init__(self):
		self.client = Main()
		self.comId = self.client.comId
	
	def run(self, email: str, password :  str):
		try:
			print(f'{X}[ 𝔩𝔬𝔤𝔦𝔳 ]{A}[{email}]{C}[{self.client.log(email,password)["api:message"]}]')
			print(f'{L}[ 𝔧𝔬𝔦𝔶 𝔠𝔬𝔴𝔴𝔲𝔳𝔦𝔱𝔶 ]{C}[{self.client.join(comId=self.comId)["api:message"]}]')
			print(f'{E}[ 𝔠𝔥𝔢𝔠𝔨 𝔦𝔳 ]{C}[{self.client.check_in(comId=self.comId,timezone=self.client.time)["api:message"]}]')
			for i in range(24):
				print(f'{A}[ 𝔤𝔢𝔫𝔢𝔯𝔞𝔱𝔦𝔳𝔤 𝔠𝔬𝔦𝔳𝔰 ]{X}[ {i+1} 𝔱𝔦𝔪𝔢𝔰 ]{C}[{self.client.send_time(comId = self.comId, timers = [{"start": int(time.time()), "end": int(time.time()) + 180}for i in range(20)],timezone=self.client.time)["api:message"]}]')
				time.sleep(12)
		except Exception as e:print(e);pass
	
	def main(self):
		os.system("clear")
		print(Fore.GREEN)
		print("𝔴𝔞𝔡𝔢 𝔟𝔶 𝔪𝔥𝔞𝔱")
		print(Fore.RED + Style.BRIGHT)
		print(pyfiglet.figlet_format("CoinGen", font="sblood"))
		print("")
		
		if select=="1":
			accs = json.load(open(f"{JsonFile}"))
			for acc in accs:
				email = acc["email"]
				password = acc["password"]
				self.run(email,password)
		
		if select=="2":
			password = EmailsPassword
			emails = open(f"{EmailsFile}")
			for email in emails:
				email = email.strip()
				self.run(email,password)


if __name__=='__main__':
	while True:
		keep_alive()
		Run().main()
