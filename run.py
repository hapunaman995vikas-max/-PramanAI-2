#!/usr/bin/env python3
"""
Run BIS Intelligent Assistant locally.

Usage:
    python run.py

This starts a local web server for the already-built website (the
`dist` folder) and opens it in your default browser. No Node.js,
npm, or internet connection is required to run it this way.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading

PORT = 5173
DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")


class SinglePageAppHandler(http.server.SimpleHTTPRequestHandler):
    """Serves the dist folder, falling back to index.html for client-side routes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.path = "/index.html"
            return self.do_GET()
        return super().send_error(code, message, explain)

    def log_message(self, format, *args):
        pass  # keep the console output clean


def find_free_port(start_port):
    port = start_port
    while port < start_port + 50:
        try:
            with socketserver.TCPServer(("", port), None):
                return port
        except OSError:
            port += 1
    return start_port


def main():
    if not os.path.isdir(DIST_DIR):
        print("ERROR: 'dist' folder not found next to run.py.")
        print("Make sure run.py sits inside the bis-intelligent-assistant folder.")
        sys.exit(1)

    port = find_free_port(PORT)
    url = f"http://localhost:{port}"

    with socketserver.TCPServer(("", port), SinglePageAppHandler) as httpd:
        print("=" * 55)
        print("  BIS Intelligent Assistant — running locally")
        print(f"  Open in browser: {url}")
        print("  Press CTRL+C to stop the server")
        print("=" * 55)

        threading.Timer(0.7, lambda: webbrowser.open(url)).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
