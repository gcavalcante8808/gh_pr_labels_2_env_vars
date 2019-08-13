FROM python:3-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    ca-certificates \
    binutils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dump_gh_pull_labels/ .

