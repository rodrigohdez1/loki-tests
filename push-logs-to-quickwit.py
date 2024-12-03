# example of usage grafana/loki api when you need push any log/message from your python scipt
import time
import json
import requests


headers = {
    'Content-type': 'application/json',
    'Accept-Encoding': 'gzip'
}

def get_logs():
    while True:
        with open('data.json') as file:
            f = json.load(file)
            for line in f:
                l = line['line']
                l = json.loads(l)
                l.update({'timestamp': '{}'.format(time.time_ns())})
                r = requests.post(
                    'http://quickwit:7280/api/v1/<index>/ingest?commit=force',
                    headers=headers,
                    data=json.dumps(l)
                )
                print(json.dumps(l))
                print(r.status_code, r.reason, r.text)
        time.sleep(.1)

get_logs()
