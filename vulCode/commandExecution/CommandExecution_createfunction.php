<?php
$foobar =$_GET['foo'];
$dyn_func = create_function('$foobar',"echo $foobar;");
$dyn_func('');
?>
