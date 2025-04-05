FROM apache/airflow:2.5.0

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install psycopg2-binary requests bs4 

COPY app/ /opt/airflow/app/
COPY dags/ /opt/airflow/dags/

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/"
