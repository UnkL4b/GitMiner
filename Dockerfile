FROM python:3-alpine

RUN apk add --update git python-dev g++ gcc libxslt-dev
RUN git clone https://github.com/UnkL4b/GitMiner.git
WORKDIR GitMiner/
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "git_miner.py"]
CMD ["-h"]