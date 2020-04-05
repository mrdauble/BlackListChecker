<h2>Özellikleri</h2>
<p>-IP aralığına göre tek tek ip black list kontrolü yapmaktadır.</p>
<p> -120 yerden  IP adreslerini kontrol etmektedir.</p>
 <p> -Tek ip adresi, yada liste formatında arama yapabilmektedir.</p>
   <h2>Kurulum</h2>
  sudo git clone https://github.com/mrdauble/BlackListChecker.git
  
  
<h4>Çalıştırmadan önce:</h4>

 pip3 install urllib3 
 <br>
 pip3 install dnspython
 
 
<h4>Toolda hata alırsanız:</h4>

urllib3 >= 1.21.1 üstü sürümler
<br>
dnspython >= 2.0.0 üstü sürümler

Ayrıca bana ulaşabilirsiniz.
_____________________
<h2>#Kullanım</h2>

<h3>IP aralığını listeleyip blacklist check yapacaksanız.</h3>

"sudo python3 ip.py" Şekilde toolu çalıştırın sonrasından Oklet Oklet Ip aralığını verin.

<h5>Örnek kullanım(Şuan sadece son oklete göre listeleme yapmaktadır.):</h5>

Oklet1:192
<br>
Oklet2:168
<br>
Oklet3:1
<br>
Oklet4:0 //( 0 dan başla)

<br>

Oklet1:192
<br>
Oklet2:168
<br>
Oklet3:1
<br>
Oklet4:5 //( 5'e kadar ip'leri çıkar)

<br>

192.168.1.0
<br>
192.168.1.1
<br>
192.168.1.2
<br>
192.168.1.3
<br>
192.168.1.4
<br>
192.168.1.5

//ve sonrasında tek tek iplerde blacklist taraması başlar.

<h3>Eğer sadece blacklist kontrolü yapacaksanız örnek kullanım:</h3>

sudo python3 blacklist.py -i <İP adresi> #sudo python3 blacklist.py -i 8.8.8.8#
<br>
sudo python3 blacklist.py -f <ip.txt (Liste Şeklinde İp adresi kontrolü)> #sudo python3 blacklist.py -f iplist.txt#
