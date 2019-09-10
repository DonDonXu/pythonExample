import jpype, jaydebeapi
import os

"""
jpype版本：0.6.3
python版本：3.7.3
JayDeBeApi版本：：1.1.1
"""

classpath='/opt/ojdbc6.jar'
os.environ['JAVA_HOME']="/usr/java/jdk1.8.0_181-amd64"
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)
conn = jaydebeapi.connect('oracle.jdbc.driver.OracleDriver', 'jdbc:oracle:thin:@192.168.2.182:1521:serp', ["serp", "serppasswd"])

sqlStr='select * from dual'
curs = conn.cursor()
curs.execute(sqlStr)
result=curs.fetchall()
print(result)
curs.close()
conn.close()