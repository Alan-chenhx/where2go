<?php

$_POST = json_decode(file_get_contents("php://input"), true);
$planId = $_POST['planId'];

$to_exec = "python returnPlan.py ".$planId;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
$fname = "test_".$planId.".json"
$file = json_decode(file_get_contents($fname), true);
header('Content-Type: application/json');
echo json_encode($file);
