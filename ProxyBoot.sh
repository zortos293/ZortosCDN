#/bin/sh
# wget "https://github.com/zortos293/ZortosCDN/raw/master/ProxyBoot.sh" && chmod +x ./ProxyBoot.sh && sudo ./ProxyBoot.sh
cd /root/
sudo mkdir /root/ZortosProxy
cd /root/ZortosProxy/
sudo apt update
sudo apt install python3 -y
sudo apt install python3-pip -y
curl -o /root/ZortosProxy/pysoxy.py  "https://raw.githubusercontent.com/zortos293/ZortosCDN/master/pysoxy.py"
curl -o /root/ZortosProxy/requirements.txt "https://raw.githubusercontent.com/zortos293/ZortosCDN/master/requirements.txt"
sudo ufw enable 
sudo ufw allow 5000/tcp
sudo ufw allow 5000/udp
pip install -r /root/ZortosProxy/requirements.txt
nohup python3 ./root/ZortosProxy/pysoxy.py & 
