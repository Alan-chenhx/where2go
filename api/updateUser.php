<?php

session_start();

include 'includes/db.php';

$uid = $_SESSION['user_id'];

$_POST = json_decode(file_get_contents("php://input"), true);
// $uid = 1;
$email = $_POST['email'];
$phone = $_POST['phone'];
$tag = $_POST['tag'];
// $email = "shuhanw2@illinois.edu";
// $phone = "2179793386";
// $tag = "110";
$portrait = $_POST['portrait'];

$query = mysqli_query($conn, "INSERT INTO profiles (user_id, email, phone, tag, portrait) 
                              VALUES ('$uid', '$email', '$name', '$avatar', '$description') 
                              ON DUPLICATE KEY UPDATE email = '$email', 
                              name = $name,
                              description = $description,
                              avatar = '$avatar';");