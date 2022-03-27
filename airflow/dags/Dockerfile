FROM puckel/docker-airflow:1.10.9

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2

RUN apt-get update && \
apt-get install -y --no-install-recommends \
        openjdk-11-jre

USER airflow
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
