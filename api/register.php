<?php

include 'includes/db.php';

$_POST = json_decode(file_get_contents("php://input"),true);

$username = $_POST['username'];
$password = $_POST['password'];
// $username = 'ggg';
// $password = 'ggg';
$email = $_POST['email'];
$description = '';
$avatar = '1';
$name = 'Anonymous';
$query = mysqli_query($conn, "INSERT INTO profiles (email, description, avatar, name) 
                              VALUES ('$email','$description', '$avatar', '$name') 
                              ON DUPLICATE KEY UPDATE email = '$email', , 
                                                      description = '$description',
                                                      name = '$name', 
                                                      avatar = '$avatar';");
$query = mysqli_query($conn, "INSERT INTO users (username, password) VALUES ('$username', '$password');");
