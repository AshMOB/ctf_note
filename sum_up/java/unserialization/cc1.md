应用场景：
保存在文件里
网络传输

CommonsCollections 链

可以作为传递的载体，因为参数经常是 object

原理：
接受任意对象
执行固定（readobject）方法

不同类的同名函数任意方法调用（反射/动态加载字节码）

入口类的要求：
可序列化
重写 readobject
接受任意对象作为参数

传递链的要求：
可序列化
集合类型，接收 object/map

压缩包安装 jdk 时需要输入
for /r %x in (\*.pack) do .\bin\unpack200 -r "%x" "%~dx%~px%~nx.jar"
