import os

def get_environ():
        try:
            version = os.environ["APP_VERSION"]
            stage = os.environ["environment"]
        except Exception:
            version = "latest"
            stage = "local"
        return version, stage