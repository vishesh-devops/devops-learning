FROM ubuntu:latest
COPY app.txt /app/app.txt
RUN apt update && apt install -y curl
CMD ["cat","/app/app.txt"]

