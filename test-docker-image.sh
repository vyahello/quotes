#!/usr/bin/env bash

IMAGE_REPO=vyahello/quotes
IMAGE_VERSION=raw
IMAGE_FULL_NAME=${IMAGE_REPO}:${IMAGE_VERSION}


test-build-image() {
:<<DOC
    Test 'docker' image build
DOC
  echo -e "Test docker image build"
  docker build --no-cache --tag ${IMAGE_FULL_NAME} \
     --build-arg VERSION=${IMAGE_VERSION} \
     --build-arg REPOSITORY=${IMAGE_REPO} \
     --file Dockerfile .
  (docker images | grep ${IMAGE_REPO}) || (echo 'Image was not built' && exit 100)
}


test-help-command() {
:<<DOC
    Test "help" command of a tool
DOC
    echo -e "Test docker image help command"
    (docker run --rm ${IMAGE_FULL_NAME} | grep help)  \
       || (echo 'Cannot verify help command' && exit 100)
    (docker run --rm ${IMAGE_FULL_NAME} -h | grep help) \
       || (echo 'Cannot verify help command' && exit 100)
    (docker run --rm ${IMAGE_FULL_NAME} --help | grep help) \
       || (echo 'Cannot verify help command' && exit 100)
}


test-quotes-command() {
:<<DOC
    Test "quotes" command of a tool
DOC
    echo -e "\n\n Test docker image quotes command"
    (docker run --rm ${IMAGE_FULL_NAME} | grep quotes) \
       || (echo 'Cannot verify quotes command' && exit 100)
}


test-image-version() {
:<<DOC
    Test "version" of a docker image
DOC
    echo -e "\n\n Test docker image version"
    (docker run --rm ${IMAGE_FULL_NAME} | grep ${IMAGE_VERSION}) \
       || (echo 'Docker image version is wrong' && exit 100)
}


cleanup() {
:<<DOC
    Cleans up environment
DOC
    docker rmi ${IMAGE_FULL_NAME}
}


main() {
:<<DOC
    Runs unit tests
DOC
    echo -e "Docker image ${IMAGE_FULL_NAME} assessment ..."
    test-build-image && \
    test-help-command && \
    test-quotes-command && \
    test-image-version && \
    cleanup
    echo -e "Docker image ${IMAGE_FULL_NAME} is ready to go"
}


main
