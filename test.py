import requests

while True:
    try: 
        uri = input()
        r = requests.get(uri)
        print(f'uri: {uri}')
        print(f'status code: {r.status_code}')
        print(f'content length: {len(r.content)} bytes')
        print(f'elapsed time: {r.elapsed.total_seconds()} s')
    except EOFError:
        break    
