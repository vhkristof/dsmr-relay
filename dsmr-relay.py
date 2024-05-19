from flask import Flask, request, Response
from datetime import datetime, timedelta

app = Flask(__name__)

telegram = None
telegram_timestamp = None

@app.route('/api/v1/datalogger/dsmrreading', methods=['POST', 'GET'])
@app.route('/telegram', methods=['GET'])
def dsmr():
    global telegram
    global telegram_timestamp

    if request.method == 'POST':
        telegram = request.form.get('telegram')
        telegram_timestamp = datetime.utcnow()
        return Response(status=201)
    elif telegram_timestamp is not None:
        if datetime.utcnow() <= telegram_timestamp + timedelta(seconds=10):
            return Response(telegram, mimetype="text/plain")
    

if __name__ == '__main__':
    import sys
    
    port = 8000
    if len(sys.argv) == 1: pass
    elif len(sys.argv) == 2: port = int(sys.argv[1])
    else: 
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    app.run(host='0.0.0.0', port=port)