1. 类加载与反序列化：

类加载的时候会执行代码
初始化：静态代码块
实例化：构造代码块，无参构造函数

2. 动态类加载方法

Class.forname

初始化/不初始化

ClassLoader.loadClass 不进行初始化
底层的原理，实现加载任意的类

ClassLoader->SecureClassLoader->URLClassLoader->AppClassLoader
loadClass->findClass(重写的方法)->defineClass(从字节码加载类)

URLClassLoader 任意类加载 file/http/jar
ClassLoader.defineClass 字节码加载任意类 私有
Unsafe.defineClass 字节码加载 public 类不能直接生成 Spring 里可以直接生成



rdesktop -g 1440x900 -r disk:LinuxDisk=/root/Downloads -u username -p "password" 192.168.10.1:3389
