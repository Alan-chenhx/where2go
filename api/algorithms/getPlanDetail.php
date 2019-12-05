<?php

$_POST = json_decode(file_get_contents("php://input"), true);
$planId = $_POST['planId'];

$to_exec = "python returnPlan.py 22212";
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
$file = file_get_contents("test.json");
header('Content-Type: application/json');
echo $file;
