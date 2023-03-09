```java
public class ProxyTest {
    public static void main(String[] args) {
        IUser user = new UserImpl();
//        user.show();
//        静态代理
        IUser userProxy = new UserProxy(user);
        userProxy.show();

    }
}
```

静态代理的问题

1. 实现接口的类如果太多需要写很多重复方法

动态代理

```java
public class ProxyTest {
    public static void main(String[] args) {
        IUser user = new UserImpl();
//        user.show();
//        静态代理
//        IUser userProxy = new UserProxy(user);
//        userProxy.show();
//      动态代理
//        要代理的接口，要做的事情,classloader
        InvocationHandler userinvocationhandler=new UserInvocationHandler(user);
        IUser userproxy= (IUser) Proxy.newProxyInstance(user.getClass().getClassLoader(), user.getClass().getInterfaces(),userinvocationhandler);
        userproxy.show();
    }
}

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class UserInvocationHandler implements InvocationHandler {
    IUser user;
    public UserInvocationHandler(){

    }
    public UserInvocationHandler(IUser user){
        this.user=user;
    }
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        method.invoke(user,args);
        return null;
    }
}

```

动态代理的意义：

1. 不修改原有类 增加功能
2. 少修改代码 适配性强

反序列化漏洞中的利用

1. readObject>反序列化自动执行
2. invoke >有函数调用
3. 拼接两条链
4. 任意 > 固定