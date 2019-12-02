<?php

session_start();

include 'includes/db.php';

$uid = $_SESSION['user_id'];

$query = mysqli_query($conn, "DELETE FROM profiles WHERE user_id = '$uid'");
$query = mysqli_query($conn, "DELETE FROM users WHERE user_id = '$uid'");

session_destroy();