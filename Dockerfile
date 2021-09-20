FROM python:3.7-stretch
RUN apt-get update
RUN apt-get upgrade -y
COPY ./ /
WORKDIR ./
RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
EXPOSE 8000
