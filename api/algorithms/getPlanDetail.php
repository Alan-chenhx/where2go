<?php

$_POST = json_decode(file_get_contents("php://input"), true);
$planId = $_POST['planId'];

// $to_exec = "python3 returnPlan.py ".$planId;
$to_exec = "python3 returnPlan.py 22471";
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
// $file = file_get_contents("test.json");
header('Content-Type: application/json');
$output = str_replace("\'", "'", $output);
// $output=[];
echo $output;
