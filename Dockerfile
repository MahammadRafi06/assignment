FROM python:3.12-alpine

COPY . /app

WORKDIR /app
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["streamlit","run" "app.py"]