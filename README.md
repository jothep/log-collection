# log-collection
use k8s shellscript filebeat to collect logs

版本更新:
通过python脚本获取主应用的containerID,并且将创建目录名改为主应用ID.只支持一个主应用容器存在.

应用在k8s中运行时,可以有多个pod副本.每个副本中,可能产生信息不同的日志文件.这些日志文件并不能全部通过docker logs来读取.
为了区分每个pod中的容器所产生的日志文件,并将这些日志文件存放在统一存储中,可以使用此项目的配置方法.
还要考虑面对分布式程序,最终将把所有日志重新汇集到原有日志文件中,则需要在日志区分化获取后,再进行统一汇聚.

docker build command:

docker build -t jasko/log-collect:0.1 -f Dockerfile .

共享存储目录 /opt/cephfs/projA
日志共享暂存目录 
name: logvol 
original: /usr/local/tomcat/logs 
target: 通过变量LOG_LOCATION实现,在挂载目录种仍需要填写
日志搜集器变量:
env:
        - name: LOG_LOCATION #日志路径,与logvol一致
          value: /opt/logs
        - name: INTERVAL  #时间间隔
          value: 5
		- name: LOGOPT #rsync参数
          value: -a
查看日志搜集容器运行状态
kubectl logs -f $PODNAME -c logcollector

