FROM python:3.9

WORKDIR /app

COPY ./server /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pandas
RUN pip install openpyxl
ENV NAME World

# RUN python database/up.py
EXPOSE 5000

CMD ["python", "app.py"]
