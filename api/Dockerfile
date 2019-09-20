FROM python:3-onbuild
COPY requirements.txt /usr/src/app/requirements.txt
COPY app/ /usr/src/app

#CMD ["./wait-for-it.sh", "--host=fhir", "--port=8080", "--timeout=120", "--", "python3", "app.py"]
CMD ["python3", "app.py"]