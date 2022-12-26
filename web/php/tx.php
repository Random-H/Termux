<?php
$to = "1092444593@qq.com";
$subject = "Test mail";
$message = "Hello! This is a simple email message.";
$from = $_GET["email"];
$headers = "From: $from";
mail($to,$subject,$message,$headers);
echo "Mail Sent.";
?>