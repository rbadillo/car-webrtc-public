#!/bin/bash

echo "Starting Streaming"
/usr/bin/curl -s -k 'https://127.0.0.1:8080/janus?action=Start'
