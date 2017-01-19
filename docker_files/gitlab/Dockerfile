
FROM ubuntu:xenial
RUN apt-get update
RUN apt-get install -y curl openssh-server ca-certificates
RUN curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | bash
RUN apt-get install -y gitlab-ce
RUN apt-get install -y supervisor
RUN apt-get -y clean

RUN locale-gen en_US.UTF-8
RUN update-locale  LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8"
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

ADD ./runsvdir.sh /root/runsvdir.sh
RUN chmod +x /root/runsvdir.sh

ADD ./services.conf  /etc/supervisor/conf.d/services.conf

CMD ["/usr/bin/supervisord", "-n"]

