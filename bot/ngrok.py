import requests
from pyngrok import ngrok

def get_ngrok_base():
    r = requests.get('http://localhost:4040/api/tunnels')
    info_json = r.json()
    remote_base = next(t["public_url"] for t in info_json["tunnels"] if t["public_url"].startswith('https'))
    return remote_base

def start_pyngrok():
    ngrok_tunnel = ngrok.connect(5000, bind_tls=True) # only https
    return ngrok_tunnel.public_url 
    
def stop_pyngrok():
    ngrok_tunnel = ngrok.get_tunnels()[0]
    ngrok.disconnect(ngrok_tunnel.public_url)
    print('ngrok stopped')

if __name__ == "__main__":
    start_pyngrok()

