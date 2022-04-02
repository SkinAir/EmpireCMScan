from ast import arg
import threading
import requests
from queue import Queue
from colorama import Fore, Back, Style
import argparse
import sys
import threading, time, signal
#用以ctrl+c


#目录遍历
class Dirscan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()    
            try:
                headers = {
                    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                }
                #发送请求
                res = requests.get(url=url,headers=headers)
                lock.acquire()#获取锁
                if res.status_code == 200:
                    print(Fore.GREEN + "[+] Success is %s : 200 " % url)
                    with open('result.txt','a',encoding='utf-8')as f:
                        f.write(Fore.GREEN + "[+] Success is %s : 200 " % url + '\n')
                        f.close()
                elif res.status_code !=200 :
                    print(Fore.RED + "[-] Fail is %s : %d" % (url,res.status_code))
                    with open('result.txt','a',encoding='utf-8')as f:
                        f.write(Fore.RED + "[-] Fail is %s : %d" % (url,res.status_code) + '\n')
                        f.close()
                lock.release()
            except Exception as e:
                print("主机拒绝连接")

lock = threading.Lock()

#启动函数
def start(url,web,count):
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)

        queue = Queue()
    #引用目录文件
        with open("%s.txt" % web, "r")as f:
            for i in f:
                newUrl = url + i.strip('\n')
                queue.put(newUrl)

        threads = []
        thread_conut = int(count)
    #多线程
        for i in range(thread_conut):
            threads.append(Dirscan(queue))
        
        for t in threads:
            t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()
    except Exception as e:
        print(e)

def clear():
    file = open("result.txt", 'w').close()#清空文件内容

#定义ctrl+c
def quit(signum, frame):
    print('You choose to stop me.')
    sys.exit()

#定义命令行参数
def parse_args():
    #创建解析对象
    parser = argparse.ArgumentParser()
    #添加命令
    parser.add_argument("-u","--url",help="Specify your URL")
    #解析复制给args
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    clear()
    args = parse_args()
    url = str(args.url)
    web = "DIR"
    count = 50
    start(url, web, count)