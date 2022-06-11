import json
import os
import wget

def ret():
    print("", end="\n")

print("欢迎使用 Plusto Package Manager！")
print("让我们先来配置一下 Plusto，然后继续使用。")

input('>')

configs = {

}

print("请先输入服务器地址，此是您从服务器下载软件包的关键。")
print("如果您乱填或填错，可能导致无法下载等错误。")
print("再此，我们整理出以下注意事项。")
print("1. 请带上协议名。(如: https://)")
print("2. 如有端口号请在结尾加上端口号。(如: https://example.com:8000/)")
print("4. 如果存储在服务器的某个文件夹中，请指定文件夹 (如: https://example.com/plusto/)")

ip = input(">")

print("正在进行服务器下载测试...")

print("在安装 Plusto Install Module 期间，请保持您的互联网连接。")
print("若您当前正在使用计费 Internet 连接，安装过程大约会产生 173 Bytes 的数据流量费用。")

filename = wget.download(ip + "/test.txt")
ret()
with open(filename, "r") as f:
    print(f.read())
    f.close()
os.remove(filename)

print("正在下载安装器...")

installlist = {
    "format_version": "v1",
}

packname = "plusto-install-module"
filename = wget.download(ip + "/install.py")
ret()

import install
installlist[packname] = {
    "namespace": "install",
    "version": install.pure_version
    }
print("安装器已安装。")
print("正在保存配置文件... 1/2")
with open("installed.plujsn", "w") as f:
    json.dump(installlist, f, indent=4, sort_keys=True)
    f.close()

configs["ip"] = ip

print("正在保存配置文件... 2/2")
with open("configs.plujsn", "w") as f:
    json.dump(configs, f, indent=4, sort_keys=True)
    f.close()



print("配置完成。")