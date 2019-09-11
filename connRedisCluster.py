#-*-coding:utf8 -*

from rediscluster import StrictRedisCluster
import time

def redis_cluster():
    redis_nodes = [{'host': '106.52.17.6', 'port': 7001},
                   {'host': '106.52.17.6', 'port': 7002},
                   {'host': '106.52.17.6', 'port': 7003},
                   {'host': '106.52.17.6', 'port': 7004},
                   {'host': '106.52.17.6', 'port': 7005},
                   {'host': '106.52.17.6', 'port': 7006}
                   ]
    print(time.time())
    redisconn = StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True)
    redisconn.set('name', 'admin')
    print("name is: ", redisconn.get('name'))
    print(time.time())

redis_cluster()