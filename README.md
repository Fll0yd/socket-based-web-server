# Simple HTTP Server (Python Sockets)

## Overview
This project demonstrates how HTTP servers work at a low level using raw Python sockets.

## What it does
- Binds to a port and listens for incoming connections
- Handles HTTP requests manually
- Sends back a valid HTTP response

## Why this matters
Most backend frameworks (Flask, FastAPI, etc.) abstract this layer.

This project shows:
- how servers actually accept connections
- how HTTP responses are structured
- how backend services communicate over TCP

## Tech
Python, socket programming

## Example Response
HTTP/1.1 200 OK
Hello, World!
