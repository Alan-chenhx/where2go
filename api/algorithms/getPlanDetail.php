<?php

$_POST = json_decode(file_get_contents("php://input"), true);
$planId = $_POST['planId'];

$to_exec = "python returnPlan.py ".$planId;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
echo $output;
