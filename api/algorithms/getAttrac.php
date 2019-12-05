<?php
$_POST = json_decode(file_get_contents("php://input"), true);
$city = $_POST['city'];
$attrac = $_POST['city'];
$city = "Los Angeles";
$attrac = "Greenbar Distillery";
$tmpc = str_replace(" ", "-", $city);
$tmpa = str_replace(" ", "-", $attrac);
$to_exec = "python returnAttrac.py ".$tmpc." ".$tmpa;
// echo $to_exec;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
$output = str_replace("\'", "'", $output);
echo $output;
