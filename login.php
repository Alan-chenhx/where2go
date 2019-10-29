<?php session_start();

include 'includes/db.php';

$_POST = json_decode(file_get_contents("php://input"),true);

$username = $_POST['username'];
$pwd = $_POST['password'];
$query = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$pwd'");
$counter = mysqli_num_rows($query);
$response = array();
if ($counter == 0) {
    echo "Invalid username or password."
} else {
    $row = mysqli_fetch_array($query);
    $user_id = $row['user_id'];
    $_SESSION['user_id'] = $user_id;
    $_SESSION['username'] = $username;
    echo json_encode(1)
    echo "<script>document.location='/index';</script>";
}