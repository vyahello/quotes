FROM vyahello/quotes-base:0.1.0
LABEL version=0.1.2 \
      metadata="The main image for quotes application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ARG REPOSITORY
ENV CODE_DIR="/code" \
    SERVER_PORT="5001" \
    IMAGE_VERSION=${VERSION} \
    IMAGE_REPO=${REPOSITORY}
WORKDIR ${CODE_DIR}
COPY quotes quotes
COPY requirements.txt docker-entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/code/docker-entry.sh"]