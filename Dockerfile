FROM alpine


RUN apk --update add --no-cache python3 py3-pip openssl ca-certificates
RUN apk --update add --virtual build-dependencies python3-dev build-base wget git py3-lxml \
  && git clone https://github.com/UnkL4b/GitMiner.git
WORKDIR GitMiner
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "git_miner.py"]
CMD ["--help"]
