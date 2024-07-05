import requests

base_url = "https://api-sandbox.orangehrm.com"  # Gantilah dengan URL yang sesuai

# Mendapatkan Token
auth_url = f"{base_url}/oauth/issueToken"
auth_payload = {
    "username": "Admin",
    "password": "admin123"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(auth_url, json=auth_payload, headers=headers)
response.raise_for_status()  # Cek jika ada error
token = response.json().get("access_token")

if not token:
    raise Exception("Failed to obtain token")

# Header dengan token
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Contoh request untuk mendapatkan daftar pengguna
users_url = f"{base_url}/v1/users"
response = requests.get(users_url, headers=headers)
response.raise_for_status()  # Cek jika ada error
users = response.json()

# Cetak hasil
print(users)
