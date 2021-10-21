from flask import Flask, request,abort
import requests
app = Flask(__name__)
DiscordURL = 'https://canary.discord.com/api/webhooks/900769374422585404/NBk9F9AN5Kx1ODmX32rvTFRW7PnkY4u8BQ-s7qynJABP6UZ3MlmkTlbMaLWVpjMtIqsV'

@app.route('/discordwebhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print (request.json)
        result = requests.post(DiscordURL, json = request.json)
        try:
         result.raise_for_status()
        except requests.exceptions.HTTPError as err:
         print(err)
        else:
         print("Payload delivered successfully, code {}.".format(result.status_code))
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()       
