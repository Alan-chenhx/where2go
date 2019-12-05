<?php

include 'includes/db.php';

$uid = $_SESSION['user_id'];
// $uid = 0;
$query = mysqli_query($conn, "SELECT * FROM plans WHERE user_id = '$uid'");

$counter = mysqli_num_rows($query);
for ($x = 0; $x < $counter; $x++) {
    $row = mysqli_fetch_array($query);
    $plan_id = $row["ref_id"];
    $response_array[$plan_id]["start"] = $row["start"];
    $response_array[$plan_id]["end"] = $row["end"];
    $response_array[$plan_id]["dest"] = $row["dest"];
    $response_array[$plan_id]["tag"] = $row["tag"];
    $response_array[$plan_id]["note"] = $row["note"];
    $response_array[$plan_id]["pace"] = $row["pace"];
    
}


echo json_encode($response_array);