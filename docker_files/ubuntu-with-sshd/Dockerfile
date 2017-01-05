FROM ubuntu:trusty
RUN apt-get update
RUN apt-get -y install openssh-server
RUN apt-get -y install supervisor
RUN apt-get -y install vim
ADD ./vimrc /root/.vimrc
RUN echo "root:root" | chpasswd
RUN mkdir -p /var/run/sshd
RUN sed -i "s/PermitRootLogin .*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN echo "[supervisord]\nnodaemon = true\n\n[program:sshd]\ncommand = /usr/sbin/sshd -p 22 -o \"ListenAddress 0.0.0.0\" -D\nstdout_logfile=/var/log/supervisor/%(program_name)s.log\nstderr_logfile=/var/log/supervisor/%(program_name)s.log\nautorestart=true" > /etc/supervisor/conf.d/services.conf
EXPOSE 22
Cmd ["/usr/bin/supervisord", "-n"]
