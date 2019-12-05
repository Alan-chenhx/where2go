<?php
include 'includes/db.php';
session_start();
$uid = $_SESSION['user_id'];
mysqli_query("START TRANSACTION");
$query1 = mysqli_query($conn, "DELETE FROM profiles WHERE user_id = '$uid'");
$query2 = mysqli_query($conn, "DELETE FROM users WHERE user_id = '$uid'");
if ($query1 and $query2) {
    mysqli_query("COMMIT");
} else {        
    mysqli_query("ROLLBACK");
}
session_unset();
session_destroy();