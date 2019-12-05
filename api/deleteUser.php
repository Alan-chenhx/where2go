<?php
include 'includes/db.php';
session_start();
$uid = $_SESSION['user_id'];
// $uid=114;
$_POST = json_decode(file_get_contents("php://input"),true);
// $uid = $_POST['currUserId'];
mysqli_query($conn,"START TRANSACTION");
$query1 = mysqli_query($conn, "DELETE FROM profiles WHERE user_id = '$uid'");
$query2 = mysqli_query($conn, "DELETE FROM users WHERE user_id = '$uid'");
if ($query1 and $query2) {
    mysqli_query($conn,"COMMIT");
} else {        
    mysqli_query($conn,"ROLLBACK");
}
session_unset();
session_destroy();