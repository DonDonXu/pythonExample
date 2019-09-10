#!/usr/bin/python3.7

from requests.auth import HTTPBasicAuth
import requests
import json
import logging
import sys

def getclustername(ip: str, apiver: str, user: str, passwd: str) -> str:
    getreq = requests.get("http://" + ip + apiver + "/clusters", auth=HTTPBasicAuth(user, passwd))
    reqjson = json.loads(getreq.content.decode("utf-8"))

    return reqjson["items"][0]["displayName"]

def get_yarn_queries(ip, apiver, user, passwd, clusterName, queryStr):
    res = requests.get("http://" + ip + apiver + "/clusters/" + clusterName + queryStr, auth=HTTPBasicAuth(user, passwd))
    hjson = json.loads(res.content.decode("utf-8"))
    return hjson

def kill_yarn_queries(ip, apiver, user, passwd, clusterName, queryStr, appId):
    res = requests.post("http://" + ip + apiver + "/clusters/" + clusterName + queryStr + "/" + appId + "/kill",
                        auth=HTTPBasicAuth(user, passwd))
    return res

def main():
    IP = "10.8.22.223:7180"
    APIVER = "/api/v18"
    USER = "admin"
    PASSWD = "passwdor"
    YARNRESTAPI = "/services/yarn/yarnApplications"
    QUERY_USER = ["hive", "deploy", "hadoop"]
    PATH_LOG = sys.path[0] + "/logs/yarn.log"
    logging.basicConfig(filename=PATH_LOG, level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    clusterName = getclustername(ip=IP, apiver=APIVER, user=USER, passwd=PASSWD)

    yarn_query = get_yarn_queries(ip=IP, apiver=APIVER, user=USER, passwd=PASSWD, clusterName=clusterName,
                                   queryStr=YARNRESTAPI)

    for yarnapp in yarn_query["applications"]:
        if (yarnapp["user"] not in QUERY_USER) and (yarnapp["state"] == "RUNNING"):
            print(yarnapp["applicationId"])
            kill_yarn_queries(ip=IP, apiver=APIVER, user=USER, passwd=PASSWD, clusterName=clusterName,
                                queryStr=YARNRESTAPI, appId=yarnapp["applicationId"])

if __name__ == '__main__':
    main()