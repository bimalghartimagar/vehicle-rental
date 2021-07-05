FROM python:alpine as base

# build base to fix 
# https://stackoverflow.com/questions/11912878/gcc-error-gcc-error-trying-to-exec-cc1-execvp-no-such-file-or-directory
# gcc: fatal error: cannot execute 'cc1plus': execvp: No such file or directory
# compilation terminated.
# error: command '/usr/bin/gcc' failed with exit code 1
RUN apk update && apk add build-base && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev make curl

RUN mkdir /rentalapi/ 
WORKDIR /rentalapi/

RUN curl https://raw.githubusercontent.com/eficode/wait-for/master/wait-for -o /tmp/wait-for.sh && chmod +x /tmp/wait-for.sh

ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /

EXPOSE 8000

FROM base as development
ADD requirements.dev.txt .
RUN pip install -r requirements.dev.txt