FROM python:3.10.4-alpine3.15 as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache build-base
RUN /usr/local/bin/python -m pip install --upgrade pip

FROM base AS builder
ENV PYTHONPATH=/usr/lib/python3.10/site-packages
RUN mkdir -p /build
WORKDIR /build
COPY /requirements.txt /build/requirements.txt
COPY uvloop-0.17.0.whl /build/uvloop-0.17.0.whl
RUN pip install --prefix=/build -r /build/requirements.txt

FROM base
COPY --from=builder /build /usr/local
COPY . /code
WORKDIR /code

EXPOSE 5000
CMD uvicorn app:app --host=0.0.0.0 --port=5000 --workers 4
