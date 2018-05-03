FROM python:3.6.2-slim
WORKDIR '/skills-labeller'

# Required system libraries
RUN apt-get update &&\
    apt-get install -y build-essential &&\
    apt-get install -y git

# Required inital python related files
COPY dispatcher/requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# Clean up
RUN apt-get remove -y build-essential && apt-get remove -y git && apt-get -y autoremove

COPY dispatcher dispatcher
COPY test test

RUN ls
ENTRYPOINT '/skills-labeller/dispatcher/run.sh'
