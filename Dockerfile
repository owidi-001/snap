FROM python:3.9.7

WORKDIR /snap

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD [ "python3 manage.py runserver " ]