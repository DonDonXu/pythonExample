from pyhive import hive

"""
使用kerberos认证，连接程序需要安装客户端
"""

conn = hive.Connection(host='master1-dev.pagoda.com.cn', port=10000, auth="KERBEROS", kerberos_service_name="hive", username='hive/master1-dev.pagoda.com.cn@PAGODA.COM.CN', database='default')
cursor = conn.cursor()
cursor.execute('show tables')

for result in cursor.fetchall():
    print(result)