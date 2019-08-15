FROM alpine:3.7 as downloader
RUN apk add --no-cache curl ca-certificates tar gzip
RUN curl -L https://github.com/tcnksm/ghr/releases/download/v0.12.2/ghr_v0.12.2_linux_amd64.tar.gz -o /tmp/ghr.tar.gz && \
    tar -xzvf /tmp/ghr.tar.gz -C /tmp --strip-components=1 && \
    chmod +x /tmp/ghr

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

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=downloader /tmp/ghr /usr/local/bin/ghr
COPY dump_gh_pull_labels/ .

