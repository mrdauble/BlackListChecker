

#Çalıştırmadan önce:

 pip3 install urllib3 
 
 pip3 install dnspython
 
Toolda hata alırsanız
urllib3 >= 1.21.1 üstü sürümler

dnspython >= 2.0.0 üstü sürümler 

_____________________
#Kullanım

İP aralığını listeleyip blacklist check yapacaksanız.

"sudo python3 ip.py" Şekilde toolu çalıştırın sonrasından Oklet Oklet Ip aralığını verin.

Örnek kullanım(Şuan sadece son oklete göre listeleme yapmaktadır.):

Oklet1:192

Oklet2:168

Oklet3:1

Oklet4:0 //( 0 dan başla)


Oklet1:192
Oklet2:168
Oklet3:1
Oklet4:5 //( 5'e kadar ip'leri çıkar)

192.168.1.0

192.168.1.1

192.168.1.2

192.168.1.3

192.168.1.4

192.168.1.5

//ve sonrasında tek tek iplerde blacklist taraması başlar.
_________________________________________
Eğer sadece blacklist kontrolü yapacaksanız örnek Kullanım:

sudo python3 blacklist.py -i <İP adresi>

sudo python3 blacklist.py -i 8.8.8.8



sudo python3 blacklist.py -f <ip.txt (Liste Şeklinde İp adresi kontrolü)>


sudo python3 blacklist.py -f iplist.txt




