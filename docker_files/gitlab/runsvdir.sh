#!/bin/bash
rm /var/opt/gitlab/gitlab-rails/sockets/gitlab.socket
sysctl -w kernel.shmmax=209715200
/opt/gitlab/embedded/bin/runsvdir-start
