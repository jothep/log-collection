FROM jasko/centos
MAINTAINER Jasko version: 0.1
COPY log-collect.sh /
RUN yum install -y rsync && chmod +x log-collect.sh
CMD ["bash", "/log-collect.sh"]
