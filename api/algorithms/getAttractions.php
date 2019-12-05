<?php
$_POST = json_decode(file_get_contents("php://input"), true);
$city = $_POST['city'];
$city = "Los Angeles";
$tmp = str_replace(" ", "-", $city);
$to_exec = "python3 returnAttractions.py ".$tmp;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
echo json_encode($output);
