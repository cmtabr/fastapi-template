FROM python:3.12.10-alpine3.21 AS base

WORKDIR /app
    
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

FROM python:3.12.10-alpine3.21 AS final

WORKDIR /app
    
COPY --from=base /install /usr/local

COPY . .