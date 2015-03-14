<?php
$username = json_decode($_POST['username']);
$password = json_decode($_POST['password']);
echo $username." ".$password;
//echo exec("whoami");

//passthru('python test.py 1 2>&1');


?>