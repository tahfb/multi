#!/bin/bash
apt-get update
git clone https://github.com/Ha3MrX/Gemail-Hack.git && mv Gemail-Hack gmail
cd gmail
chmod +x gemailhack.py
cd ..
mkdir facebook
cd facebook
wget raw.githubusercontent.com/Sup3r-Us3r/scripts/master/fb-brute.pl
cd ..
git clone https://github.com/umeshshinde19/instainsane && mv instainsane instagram
git clone https://github.com/NecktieRed/Brute-force-Twitter && mv Brute-force-Twitter twitter
apt install python-pip
pip install selenium==2.53.6 && pip install termcolor
cd instagram 
bash install.sh
cd ..
pkg install git 
pkg install perl
pkg install nmap 
pkg install python
pkg install fakeroot
git clone https://github.com/sullo/nikto.git 
