FROM python:3.6.6-stretch

ENV API_PORT 80
COPY . /api

WORKDIR /api
RUN mkdir logs

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "model_process.py", "&", "gunicorn", "-c", "gunicorn.py", "api:app"]
CMD ["gunicorn", "-c", "gunicorn.py", "api:app"]
