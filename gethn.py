"""
获取系统变量
import os
podname = os.environ.get('HOSTNAME')
k8s = os.environ.get('KUBERNETES_SERVICE_HOST')

在字符串中引入变量
url = 'https://' + k8s + ':443/api/v1/namespaces/default/pods/' + podname

将python变量转为系统变量
os.environ['URL']=str(url)
os.system('echo $URL')

在python执行系统命令
import commands
commands.getoutput("curl -k -s '%s'" % url)
不知为何没有直接返回值,可能是长度或格式问题

将获取值json格式化
import json
json_string = commands.getoutput("curl -k -s '%s'" % url)
print(json_string) #此时已获得值
jsload = json.loads(json_string) #解析为dict
print type(jsload)

jsload这个字典中的项
print jsload['status']['containerStatuses'][0]['name']
print jsload['status']['containerStatuses'][0]['containerID']

通过循环遍历将字典中的项找出
for i in range(len(jsload['status']['containerStatuses'])):
  if jsload['status']['containerStatuses'][i]['name'] != 'logcollector':
    cname = jsload['status']['containerStatuses'][i]['name']
    cid = jsload['status']['containerStatuses'][i]['containerID']
print('containerName: %s containerID: %s' % (cname,cid))

将cid值写入文件
commands.getoutput("echo '%s' > /cid.txt" % cid)
"""

#整个脚本示例
import os
import commands
import json

podname = os.environ.get('HOSTNAME')
k8s = os.environ.get('KUBERNETES_SERVICE_HOST')
url = 'https://' + k8s + ':443/api/v1/namespaces/default/pods/' + podname
json_string = commands.getoutput("curl -k -s '%s'" % url)
jsload = json.loads(json_string)
for i in range(len(jsload['status']['containerStatuses'])):
  if jsload['status']['containerStatuses'][i]['name'] != 'logcollector':
    cname = jsload['status']['containerStatuses'][i]['name']
    cid = jsload['status']['containerStatuses'][i]['containerID']
print('containerName: %s containerID: %s' % (cname,cid))
commands.getoutput("echo '%s' > /cid.txt" % cid)
