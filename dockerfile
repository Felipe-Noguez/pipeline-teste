FROM python:3.10.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install Flask Werkzeug
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
