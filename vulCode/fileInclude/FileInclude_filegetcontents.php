<?php
$URI = $_GET['uri'];
//print $URI."<br/>";
//$i = strpos($URI,'..');
//print $i."<br/>";
if (strpos($URI,'..'))exit('That is not a valid URI.');
$contents = file_get_contents($URI);
print $contents;
print "<br/>";
?>
