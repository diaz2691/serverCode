<?php
$data = json_decode($_POST['myData']);
echo $data;
echo exec("whoami");

passthru('python test.py 1 2>&1');


?>