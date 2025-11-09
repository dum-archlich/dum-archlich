import requests
import base64
import webbrowser

# Spotify credentials
CLIENT_ID = '4d3e63daab074402ac763d9e511a66db'
CLIENT_SECRET = 'acd880ba00e1484faa783bb7dd27cc1d'
REDIRECT_URI = 'https://spotify-callback-a2uuwol9z-makdum-ibrohims-projects.vercel.app'

# Step 1: Get authorization URL
def get_auth_url():
    scope = 'user-read-currently-playing user-read-recently-played'
    auth_url = f'https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}'
    return auth_url

# Step 2: Exchange code for tokens
def get_tokens(auth_code):
    auth_header = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    return response.json()

# Main function
if __name__ == '__main__':
    print("Buka URL ini di browser dan authorize aplikasi:")
    auth_url = get_auth_url()
    print(auth_url)
    webbrowser.open(auth_url)

    auth_code = input("Masukkan kode dari URL redirect (setelah 'code='): ")
    tokens = get_tokens(auth_code)
    if 'refresh_token' in tokens:
        print(f"Refresh Token: {tokens['refresh_token']}")
    else:
        print("Error:", tokens)