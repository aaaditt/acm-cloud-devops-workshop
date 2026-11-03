import os
import socket

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

# Config comes from env vars, so the same image can behave differently (docker run -e ...)
VERSION = os.environ.get("VERSION", "v1")


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/info")
def info():
    # Inside a container the hostname is the container ID, the same one `docker ps` shows
    return jsonify(host=socket.gethostname(), version=VERSION)


if __name__ == "__main__":
    # 0.0.0.0 so the app is reachable from outside the container
    app.run(host="0.0.0.0", port=8080)
