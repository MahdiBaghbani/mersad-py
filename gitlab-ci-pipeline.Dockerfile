FROM ubuntu:bionic

# install system requirements
RUN apt-get update -y
RUN apt-get install -y git
RUN apt-get install -y curl
RUN apt-get install -y python3 python3-dev python3-pip

# install codeclimate's code coverage reporter
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > /usr/bin/cc-test-reporter
RUN chmod +x /usr/bin/cc-test-reporter

# install python packages
RUN pip3 install --upgrade setuptools wheel
RUN pip3 install --upgrade pipenv
RUN pip3 install --upgrade twine

# set environment variables
# LC_ALL and LANG are set to UTF-8 to
# prevent pipenv runtime error
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
