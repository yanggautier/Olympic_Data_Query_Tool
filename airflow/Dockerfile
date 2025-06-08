FROM apache/airflow:3.0.1
USER root

# Install Python dependencies
COPY requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt