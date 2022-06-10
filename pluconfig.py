import json
import os

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
print("3. 请在地址的结尾加上 '/'。 (如: https://example.com/)")
print("4. 如果存储在服务器的某个文件夹中，请指定文件夹 (如: https://example.com/plusto/)")
configs["ip"] = input("")
