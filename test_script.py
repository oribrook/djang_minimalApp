import requests


file_path = r"some-path-to-file"
with open(file_path, 'rb') as f:
    r = requests.post('http://127.0.0.1:8000/upload', files={"file": ('test.txt', f)})