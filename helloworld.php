<?php
$username = $_POST['username'];
$password = $_POST['password'];
$check = passthru('python seleniumtestloginDani.py 1 2>&1' .$username." ".$password);
echo $check;
?>


