FROM python:3-onbuild

RUN apt-get update ; apt-get upgrade ; apt-get install -y poppler-utils

COPY requirements.txt /usr/src/app/requirements.txt
COPY app/ /usr/src/app

#CMD ["./wait-for-it.sh", "--host=fhir", "--port=8080", "--timeout=120", "--", "python3", "app.py"]
CMD ["python3", "app.py"]