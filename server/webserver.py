import os

ports = int(input("\n请输入要开放的端口号\n>"))

commands = 'python -m http.server', ports

os.system(commands)