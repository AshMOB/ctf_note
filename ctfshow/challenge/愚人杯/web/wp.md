# easy_signin

前台显示一个图片，直接以 base64 编码传回前端，url 中的参数也以 base64 编码，因而猜测存在文件包含，包含 index.php 即可看到返回页面 存在 base64 编码的数据

```php
<?php
/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2023-03-27 10:30:30
# @Last Modified by:   h1xa
# @Last Modified time: 2023-03-28 12:15:33
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$image=$_GET['img'];

$flag = "ctfshow{3a547e78-aa98-44f5-87a6-dd2f4c2e773d}";
if(isset($image)){
	$image = base64_decode($image);
	$data = base64_encode(file_get_contents($image));
	echo "<img src='data:image/png;base64,$data'/>";
}else{
	$image = base64_encode("face.png");
	header("location:/?img=".$image);
}



```

# 被遗忘的反序列化

```php
<?php

# 当前目录中有一个txt文件哦
error_reporting(0);
show_source(__FILE__);
include("check.php");

class EeE{
    public $text;
    public $eeee;
    public function __wakeup(){
        if ($this->text == "aaaa"){
            echo lcfirst($this->text);
        }
    }

    public function __get($kk){
        echo "$kk,eeeeeeeeeeeee";
    }

    public function __clone(){
        $a = new cycycycy;
        $a -> aaa();
    }

}

class cycycycy{
    public $a;
    private $b;

    public function aaa(){
        $get = $_GET['get'];
        $get = cipher($get);
        if($get === "p8vfuv8g8v8py"){
            eval($_POST["eval"]);
        }
    }


    public function __invoke(){
        $a_a = $this -> a;
        echo "\$a_a\$";
    }
}

class gBoBg{
    public $name;
    public $file;
    public $coos;
    private $eeee="-_-";
    public function __toString(){
        if(isset($this->name)){
            $a = new $this->coos($this->file);
            echo $a;
        }else if(!isset($this -> file)){
            return $this->coos->name;
        }else{
            $aa = $this->coos;
            $bb = $this->file;
            return $aa();
        }
    }
}

class w_wuw_w{
    public $aaa;
    public $key;
    public $file;
    public function __wakeup(){
        if(!preg_match("/php|63|\*|\?/i",$this -> key)){
            $this->key = file_get_contents($this -> file);
        }else{
            echo "不行哦";
        }
    }

    public function __destruct(){
        echo $this->aaa;
    }

    public function __invoke(){
        $this -> aaa = clone new EeE;
    }
}

$_ip = $_SERVER["HTTP_AAAAAA"];
unserialize($_ip);
```

分析反序列化链
第一种
w_wuw_w