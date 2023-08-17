import requests

BASE_URL = "http://your-web-server-url"  # Replace with your actual web server URL

def register_user(email: str, password: str) -> None:
    url = f"{BASE_URL}/register"
    data = {"email": email, "password": password}
    response = requests.post(url, json=data)
    assert response.status_code == 200

def log_in_wrong_password(email: str, password: str) -> None:
    url = f"{BASE_URL}/login"
    data = {"email": email, "password": password}
    response = requests.post(url, json=data)
    assert response.status_code == 401

def log_in(email: str, password: str) -> str:
    url = f"{BASE_URL}/login"
    data = {"email": email, "password": password}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    return response.json()["session_id"]

def profile_unlogged() -> None:
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status_code == 401

def profile_logged(session_id: str) -> None:
    url = f"{BASE_URL}/profile"
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def log_out(session_id: str) -> None:
    url = f"{BASE_URL}/logout"
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.post(url, headers=headers)
    assert response.status_code == 200

def reset_password_token(email: str) -> str:
    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    return response.json()["reset_token"]

def update_password(email: str, reset_token: str, new_password: str) -> None:
    url = f"{BASE_URL}/update_password"
    data = {"email": email, "reset_token": reset_token, "new_password": new_password}
    response = requests.post(url, json=data)
    assert response.status_code == 200

if __name__ == "__main__":
    # You can call and test your functions here
    pass
