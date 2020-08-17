#!/bin/bash


helper() {
:<<DOC
    Shows 'help' message
DOC
    cat <<HELP
    This program allows to launch quotes application via docker image.

    Please use next command:
      - 'help' to see tool help
         docker run ${IMAGE_REPO}:${IMAGE_VERSION} --help

      - 'quotes' to run quotes web application
         docker run -it -p {local-port}:${SERVER_PORT} ${IMAGE_REPO}:${IMAGE_VERSION} quotes
HELP
}


quotes() {
:<<DOC
    Entrypoint to launch 'quotes' web application
DOC
    python quotes/manage.py runserver 0.0.0.0:${SERVER_PORT}
}


main() {
:<<DOC
    Launches 'main' tools executor
DOC
    if (
        [[ "$1" == "-h" ]] ||
        [[ "$1" == "--help" ]] ||
        [[ "$1" == "help" ]] ||
        [[ $# -eq 0 ]]
    ); then
        helper
        exit 0
    fi
    local cmd=$1; shift
    eval "${cmd} $@"
}


main $@