FROM ubuntu:latest
SHELL ["bin/bash", "-c"]
USER root
RUN apt-get update && apt-get install -y sudo
RUN apt-get install -y vim
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.7
RUN apt-get install -y python3.7-distutils
COPY . .
RUN python3.7 get-pip.py
RUN export PATH=LOCAL_PATH:$PATH
RUN source ~/.profile
RUN pip3 install -r requirements.txt
RUN pip3 install flask
ENV FLASK_APP=audit.py
CMD [ "python3.7","-m", "flask", "run", "--host=0.0.0.0"]
