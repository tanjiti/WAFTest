<?php
$evil_callback=$_GET['callback'];
$some_array = array(0,1,2,3);
$new_array = array_map($evil_callback,$some_array);
?>
