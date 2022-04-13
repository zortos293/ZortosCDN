#/bin/sh
# wget "https://Zortosdev.tech/ProxyBoot.sh" && chmod +x ./ProxyBoot.sh && ./ProxyBoot.sh
cd /root/
mkdir /root/ZortosProxy
cd /root/ZortosProxy/
apt update
apt install python3 -y
apt install python3-pip -y
curl -o /root/ZortosProxy/pysoxy.py  "https://raw.githubusercontent.com/zortos293/ZortosCDN/master/pysoxy.py"
curl -o /root/ZortosProxy/requirements.txt "https://raw.githubusercontent.com/zortos293/ZortosCDN/master/requirements.txt"
ufw enable 
ufw allow 5000/tcp
ufw allow 5000/udp
pip install -r /root/ZortosProxy/requirements.txt
nohup python3 ./root/ZortosProxy/pysoxy.py & 
