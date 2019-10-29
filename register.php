<?php

include 'includes/db.php';

$_POST = json_decode(file_get_contents("php://input"),true);

$username = $_POST['username'];
$email = $_POST['email'];
$password = $_POST['password'];
$query = mysqli_query($conn, "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')");