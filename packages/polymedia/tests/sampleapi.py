
# From: https://github.com/uktrade/s3proxy/blob/master/test.py

import os 
import json
import signal 
import socket
import sys 
import time

from flask import Flask, request, Response
from multiprocessing import (
    Process,
)

def create_sample_api(
        max_attempts=100, is_logged_in=True,
        client_id='the-client-id',
        client_secret='the-client-secret',
        tokens_returned=('the-token',), token_expected='the-token',
        code_returned='the-code', code_expected='the-code',
        me_response_code=200,
        endpoints = []
):
    # Mock API in a different process to not block tests

    def start():
        os.environ['FLASK_ENV'] = 'development'  # Avoid warning about this not a prod server
        app = Flask('app')
        app.add_url_rule('/api/test/', view_func=handle_get, methods=['GET'])
        
        def _stop(_, __):
            sys.exit()

        signal.signal(signal.SIGTERM, _stop)

        try:
            app.run(host='', port=8088, debug=False)
        except SystemExit:
            # app.run doesn't seem to have a good way of killing the server,
            # and want to exit cleanly for code coverage
            pass

    def wait_until_connected():
        for i in range(0, max_attempts):
            try:
                with socket.create_connection(('127.0.0.1', 8081), timeout=0.1):
                    break
            except (OSError, ConnectionRefusedError):
                if i == max_attempts - 1:
                    raise
                time.sleep(0.01)

    def stop():
        process.terminate()
        process.join()

    def handle_get():
        correct = request.headers.get('authorization', '') == f'Bearer {token_expected}'
        me = {
            'email': 'test@test.com',
            'first_name': 'Peter',
            'last_name': 'Piper',
            'user_id': '7f93c2c7-bc32-43f3-87dc-40d0b8fb2cd2',
        }
        return Response(json.dumps(me), status=me_response_code)
        return \
            Response(json.dumps(me), status=me_response_code) if correct else \
            Response(status=403)

    process = Process(target=start)
    process.start()

    return wait_until_connected, stop