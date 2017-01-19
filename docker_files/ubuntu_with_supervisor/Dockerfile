FROM ubuntu:xenial
RUN apt-get update
RUN apt-get -y install supervisor
RUN apt-get -y install vim
RUN apt-get -y clean
RUN locale-gen en_US.UTF-8
RUN update-locale  LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8"
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ADD ./vimrc /root/.vimrc
ADD ./services.conf  /etc/supervisor/conf.d/services.conf
CMD ["/usr/bin/supervisord", "-n"]
