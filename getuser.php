<?php

session_start();

$response_array["uname"] = $_SESSION["username"];
$response_array["usid"] = $_SESSION["user_id"];
$response_array["email"] = $_SESSION["email"];
$response_array["phone"] = $_SESSION["phone"];
$response_array["tag"] = $_SESSION["tag"];

echo json_encode($response_array);
