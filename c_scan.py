# coding:utf-8
import argparse
from queue import Queue
from threading import Thread
import requests
import wmi
from nmap import nmap
from config import *


class nm:

    @classmethod
    def get_CIDR(cls):
        wmi_obj = wmi.WMI()
        wmi_sql = "select IPAddress,DefaultIPGateway,IPSubnet  from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        wmi_out = wmi_obj.query(wmi_sql)

        def netmask_to_bit_length(netmask):
            """
            子网掩码1的个数
            :param netmask: 子网掩码
            :return: 子网掩码1的个数
            """
            return sum([bin(int(i)).count('1') for i in netmask.split('.')])

        return f"{wmi_out[0].DefaultIPGateway[0]}/{netmask_to_bit_length(wmi_out[0].IPSubnet[0])}"

    @classmethod
    def all_hosts(cls):
        nmPS = nmap.PortScanner()
        nmPS.scan(cls.get_CIDR(), arguments='-sP')
        hosts_list = [x for x in nmPS.all_hosts()]
        return hosts_list

    @classmethod
    def ports_and_ip_factory(cls, hosts_list=None, ports=common_ports):
        queue = Queue()
        if not hosts_list:
            hosts_list = cls.all_hosts()
        [[queue.put(f"http://{x}:{port[0]}") for port in ports] for x in hosts_list]
        return queue


class c_scan:

    def __init__(self, thread_count=20, ports=common_ports):
        self.__queue = nm.ports_and_ip_factory(ports=ports)
        self.__thread_count = thread_count
        self.__ports = ports
        self.__result = []

    def start(self):
        for i in range(self.__thread_count):
            if not self.__queue.empty():
                my_thread = self.my_threading(self.__queue, self.__result)
                my_thread.start()
                my_thread.join()
        print("扫描完成！")
        for r in self.__result:
            print(r)

    class my_threading(Thread):

        def __init__(self, queue, result):
            super().__init__()
            self.__queue = queue
            self.__result = result

        def run(self):
            while not self.__queue.empty():
                scan_url = self.__queue.get()
                try:
                    print(f"正在请求{scan_url}")
                    response = requests.get(scan_url, timeout=1)
                    if response.status_code != 404:
                        self.__result.append(f"[{response.status_code}]{scan_url}")
                except Exception:
                    pass


parser = argparse.ArgumentParser(description='抓取网关的IP地址机器常用端口.')
parser.add_argument('-n', '--number', type=int, help='线程使用数量，默认为（20）.', required=False)
parser.add_argument('-p', '--ports', type=str, help='检索端口，默认为配置文件的端口.', required=False)
args = parser.parse_args()

n = 20
p = common_ports
if args.number:
    n = int(args.number)
if args.ports:
    p = int(args.ports)

scan = c_scan(thread_count=n, ports=p)
scan.start()
