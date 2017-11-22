FROM python:2-slim
LABEL maintainer "Peter Benjamin"
WORKDIR /src/gitminer
COPY [ ".", "." ]
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "git_miner.py" ]

