<?php
// $username = json_decode($_POST['username']);
// $password = json_decode($_POST['password']);

foreach (getallheaders() as $name => $value){
	echo "$name: $value\n";
}
print_r($_POST['Array[0]']);
//echo $username." ".$password;
//echo exec("whoami");

//passthru('python test.py 1 2>&1');


?>