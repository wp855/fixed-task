
FROM python:3.11-slim-bookworm@sha256:d554a72d3e9c1dbde09e25b1842a59eafcc0855ec70bb635581172db7bd29bb2

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log