<?php
$username = ($_POST['username']);
$password = ($_POST['password']);

echo "This is a POST response from the server and your username is: ".$username." and your".
"password is: ".$password;
//echo exec("whoami");

//passthru('python test.py 1 2>&1');


?>