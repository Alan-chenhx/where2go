<?php

$_POST = json_decode(file_get_contents("php://input"), true);

$city = $_POST['city'];
$duration = $_POST['duration'];
$oldname = $_POST['oldname'];
$name = $_POST['name'];
$planId = $_POST['planId'];

$city = "Mountain View";
$oldname = "17-Mile Drive";
$name = "Pacific Grove Certified Farmers' Market";
$duration = 233;
$planId = 13458;

$command = "python3 updateIter.py "."\"$city\"".' '."\"$oldname\"".' '."\"$name\"".' '.$duration.' '.$planId;
$to_exec = escapeshellcmd($command);
$output = shell_exec($to_exec);

echo $output;
