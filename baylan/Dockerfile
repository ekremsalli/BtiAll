FROM python:3.9.6-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers zlib zlib-dev python3-dev \
      libxml2-dev libxslt-dev build-base unixodbc-dev \
      zeromq-dev libxslt dos2unix

RUN apk --no-cache add curl gnupg


RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.6.1.1-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.6.1.1-1_amd64.apk

RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.6.1.1-1_amd64.sig
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.6.1.1-1_amd64.sig

RUN curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import -
RUN gpg --verify msodbcsql17_17.6.1.1-1_amd64.sig msodbcsql17_17.6.1.1-1_amd64.apk
RUN gpg --verify mssql-tools_17.6.1.1-1_amd64.sig mssql-tools_17.6.1.1-1_amd64.apk

RUN apk add --allow-untrusted msodbcsql17_17.6.1.1-1_amd64.apk
RUN apk add --allow-untrusted mssql-tools_17.6.1.1-1_amd64.apk


RUN pip install --upgrade pip

COPY ./REQUIREMENTS .
COPY lib/ /usr/src/app/lib/

RUN pip install -r ./REQUIREMENTS


COPY ./entrypoint.sh .

RUN dos2unix entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

COPY . .