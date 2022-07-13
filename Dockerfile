FROM python:3.9

ARG APP_VERSION="latest"
# ENV DONKEYKONG_VERSION ${APP_VERSION}
ENV PROJECT_NAME="donkeykong"

WORKDIR /code

COPY . ./
RUN apt-get update
RUN apt-get install sudo -y
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-1.19.1.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
ENV PIP_CONFIG_FILE pip.conf
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN sed -i 's/\r$//' start.sh
RUN sed -i 's/\r$//' start-dev.sh
