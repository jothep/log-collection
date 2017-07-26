# log-collection
use k8s shellscript filebeat to collect logs

应用在k8s中运行时,可以有多个pod副本.每个副本中,可能产生信息不同的日志文件.这些日志文件并不能全部通过docker logs来读取.
为了区分每个pod中的容器所产生的日志文件,并将这些日志文件存放在统一存储中,可以使用此项目的配置方法.
还要考虑面对分布式程序,最终将把所有日志重新汇集到原有日志文件中,则需要在日志区分化获取后,再进行统一汇聚.

docker build command:
docker build -t jasko/log-collect:0.1 -f Dockerfile .
