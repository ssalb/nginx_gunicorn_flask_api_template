FROM python:3.6.6

ENV API_PORT 80
COPY . /api

WORKDIR /api
RUN mkdir logs

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn.py", "api:app"]
