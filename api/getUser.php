<?php

session_start();

include 'includes/db.php';

$uid = $_SESSION['user_id'];

$query = mysqli_query($conn, "SELECT * FROM profiles WHERE user_id = '$uid'");
$row = mysqli_fetch_array($query);


$response_array["uname"] = $_SESSION["username"];
$response_array["usid"] = $_SESSION["user_id"];
$response_array["email"] = $row["email"];
$response_array["name"] = $row["name"];
$response_array["description"] = $row["description"];
$response_array["avatar"] = $row["avatar"];

echo json_encode($response_array);
