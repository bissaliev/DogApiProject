FROM python:3.12
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY dog_app .
CMD [ "python3", "manage.py", "runserver", "0:8000" ]