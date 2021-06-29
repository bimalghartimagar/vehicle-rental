FROM python:alpine

# build base to fix 
# https://stackoverflow.com/questions/11912878/gcc-error-gcc-error-trying-to-exec-cc1-execvp-no-such-file-or-directory
# gcc: fatal error: cannot execute 'cc1plus': execvp: No such file or directory
# compilation terminated.
# error: command '/usr/bin/gcc' failed with exit code 1
RUN apk update && apk add build-base && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev make

RUN mkdir /rentalapi/ 

WORKDIR /rentalapi/

ADD requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

WORKDIR /