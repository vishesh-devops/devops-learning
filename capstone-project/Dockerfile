FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN pip install psycopg2-binary
ENV USER_NAME=Vishesh
ENV TASK="Learn Docker"
CMD ["python3", "app.py"]
