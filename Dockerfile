FROM ubuntu:latest
LABEL authors="LeCras"

ENTRYPOINT ["top", "-b"]