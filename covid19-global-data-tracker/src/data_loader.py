class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        import pandas as pd
        return pd.read_csv(self.file_path)

    def fetch_data(self, api_url):
        import requests
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()