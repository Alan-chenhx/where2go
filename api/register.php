<?php

include 'includes/db.php';

$_POST = json_decode(file_get_contents("php://input"),true);

$username = $_POST['username'];
$password = $_POST['password'];
// $username = 'ggg';
// $password = 'ggg';
$email = 'not set';
$phone = 'not set';
$tag = '000';
$portrait = '1';
$query = mysqli_query($conn, "INSERT INTO profiles (email, phone, tag, portrait) 
                              VALUES ('$email', '$phone', '$tag', '$portrait') 
                              ON DUPLICATE KEY UPDATE email = '$email', 
                                                      phone = '$phone', 
                                                      tag = '$tag', 
                                                      portrait = '$portrait';");
$query = mysqli_query($conn, "INSERT INTO users (username, password) VALUES ('$username', '$password');");
