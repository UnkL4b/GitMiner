FROM python:3-slim

#RUN apk add --update git python-dev g++ gcc libxslt-dev

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/UnkL4b/GitMiner.git
WORKDIR GitMiner/
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "git_miner.py"]
CMD ["-h"]