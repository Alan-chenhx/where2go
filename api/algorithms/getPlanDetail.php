<?php

$_POST = json_decode(file_get_contents("php://input"), true);
$planId = $_POST['planId'];

$to_exec = "python returnPlan.py ".$planId;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
$file = json_decode(file_get_contents("test.json"), true);
header('Content-Type: application/json');
echo json_encode($file);
