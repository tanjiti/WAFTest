<?php
$myvar = "varname";
if(isset($_GET["arg"]))
{
$arg = $_GET["arg"];
eval("\$myvar = $arg;");

}
echo "\$myvar = ".$myvar;
?>
