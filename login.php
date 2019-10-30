<?php session_start();

include 'includes/db.php';
$_POST = json_decode(file_get_contents("php://input"),true);
$username = $_POST['username'];
// $email = $_POST['email'];
$password = $_POST['password'];

// $pwd = $_POST['password'];
$query = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
$counter = mysqli_num_rows($query);
$response = array();
if ($counter == 0) {
    die("Invalid username or password.");
} else {
    $row = mysqli_fetch_array($query);
    $user_id = $row['user_id'];
    $email = $row['email'];
    $phone = $row['phone'];
    $tag = $row['tag'];
    $_SESSION["username"] = $username;
    $_SESSION["user_id"] = $user_id;
    $_SESSION["email"] = $email;
    $_SESSION["phone"] = $phone;
    $_SESSION["tag"] = $tag;
    $response_array['success'] = 1;
    echo json_encode($response_array);
}

// include 'includes/db.php';
//
// $_POST = json_decode(file_get_contents("php://input"),true);
// var_dump($_POST);
// $username = $_POST['username'];
// $email = $_POST['email'];
// $password = $_POST['password'];
// echo $username;
// $query = mysqli_query($conn, "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')");
// $query = mysqli_query($conn, "INSERT INTO users (username, password, email) VALUES ('username', 'assword', 'mail')");
