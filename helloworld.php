<?php
echo "Hello World <br/>";

echo exec("whoami");

passthru('python test.py 1 2>&1');


?>