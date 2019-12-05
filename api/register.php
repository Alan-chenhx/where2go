<?php

include 'includes/db.php';

$_POST = json_decode(file_get_contents("php://input"),true);

$username = $_POST['username'];
$password = $_POST['password'];
// $username = 'ggg';
// $password = 'ggg';
$email = $_POST['email'];
// $email = 'fuck123123123131231232131321';
$description = '123213213213213123213123213';
$avatar = '1123213213213213213213221';
$name = 'Anonymous';
$query = mysqli_query($conn, "INSERT INTO profiles (email, description, avatar, name) 
                              VALUES ('$email','$description', '$avatar', '$name') 
                              ON DUPLICATE KEY UPDATE email = '$email', 
                                                      description = '$description',
                                                      name = '$name', 
                                                      avatar = '$avatar';");



$query = mysqli_query($conn, "INSERT INTO users (username, password) VALUES ('$username', '$password');");


$query = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
$counter = mysqli_num_rows($query);
$response = array();
if ($counter == 0) {
    header('HTTP/1.1 401 Internal Server Booboo');
    header('Content-Type: application/json; charset=UTF-8');
    die(json_encode(array('message' => 'ERROR', 'code' => 1337)));
} else {
    $row = mysqli_fetch_array($query);
    $user_id = $row['user_id'];
    $_SESSION["user_id"] = $user_id;
    $_SESSION["username"] = $username;
    $response_array['success'] = 1;
    $response_array['currUserId'] = $user_id;
    echo json_encode($response_array);
}
