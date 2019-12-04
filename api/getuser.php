<?php

session_start();

include 'includes/db.php';

$uid = $_SESSION['user_id'];

$query = mysqli_query($conn, "SELECT * FROM profiles WHERE user_id = '$uid'");
$row = mysqli_fetch_array($query);


$response_array["uname"] = $_SESSION["username"];
$response_array["usid"] = $_SESSION["user_id"];
$response_array["email"] = $row["email"];
$response_array["phone"] = $row["phone"];
$response_array["tag"] = $row["tag"];
$response_array["portrait"] = $row["portrait"];

echo json_encode($response_array);
