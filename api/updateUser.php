<?php

session_start();

include 'includes/db.php';

$uid = $_SESSION['user_id'];

$_POST = json_decode(file_get_contents("php://input"), true);
// $uid = 1;
$email = $_POST['email'];
$description = $_POST['description'];
$name = $_POST['name'];
$avatar = $_POST['avatar'];

$query = mysqli_query($conn, "INSERT INTO profiles (user_id, email, description, name, avatar) 
                              VALUES ($uid, '$email', '$description', '$name', '$avatar') 
                              ON DUPLICATE KEY UPDATE email = '$email', 
                              name = '$name',
                              description = '$description',
                              avatar = '$avatar';");
