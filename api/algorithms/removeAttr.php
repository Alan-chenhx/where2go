<?php

$_POST = json_decode(file_get_contents("php://input"), true);

$planId = $_POST['planId'];
$name = $_POST['name'];

$command = "python removeIter.py "."\"$name\"".' '.$planId;
$to_exec = escapeshellcmd($command);
$output = shell_exec($to_exec);
