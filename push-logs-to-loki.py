# example of usage grafana/loki api when you need push any log/message from your python scipt
import time
import json
import requests


headers = {
    'Content-type': 'application/json',
    'Accept-Encoding': 'gzip',
    'X-Scope-OrgID': 'tenant_0'
}

def get_logs():
    while True:
        with open('data.json') as file:
            f = json.load(file)
            for line in f:
                content = {
                    'streams': [
                        {
                            'stream': {
                                'source': 'python',
                                'environment': 'local',
                                'team': 'new-team',
                                'app_name': 'app',
                                'component': 'component',
                                'log_type': 'access',
                                'service_name': 'loki-test'
                            },
                            'values': [
                                ['{}'.format(time.time_ns()), line['line']]
                            ]
                        }
                    ]
                }
                r = requests.post(
                    'http://loki:3100/loki/api/v1/push',
                    headers=headers,
                    data=json.dumps(content)
                )
                print(r.status_code, r.reason, r.text)
                time.sleep(.1)


logs = get_logs()
