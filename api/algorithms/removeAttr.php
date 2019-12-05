<?php

$_POST = json_decode(file_get_contents("php://input"), true);

$planId = $_POST['planId'];
$name = $_POST['name'];
