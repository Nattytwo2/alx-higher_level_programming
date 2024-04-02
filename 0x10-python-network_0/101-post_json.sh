#!/bin/bash
# Bash Script that ends a JSON POST request to a URL passed as the first argument
curl -sH "Content-Type: application/json" --data "$(cat "$2")" "$1"
