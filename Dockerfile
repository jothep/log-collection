#FROM jasko/centos
#MAINTAINER Jasko version: 0.1
#COPY log-collect.sh /
#RUN yum install -y rsync && chmod +x log-collect.sh
#CMD ["bash", "/log-collect.sh"]

FROM jasko/centos
MAINTAINER Jasko version: 0.2
COPY log-collect.sh /
COPY gethn.py /
RUN yum install -y rsync && chmod +x log-collect.sh
CMD ["bash", "/log-collect.sh"]
