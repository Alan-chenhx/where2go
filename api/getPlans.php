<?php

include 'includes/db.php';
// $_POST = json_decode(file_get_contents("php://input"),true);
// $uid = $_SESSION['user_id'];
$uid = 0;

$query = mysqli_query($conn, "SELECT * FROM plans WHERE user_id = '$uid'");

$counter = mysqli_num_rows($query);
$response = array($counter);
for ($x = 0; $x < $counter; $x++) {
    $row = mysqli_fetch_array($query);
    $response_array["start"] = $row["start"];
    $response_array["end"] = $row["end"];
    $response_array["dest"] = $row["dest"];
    $response_array["tag"] = $row["tag"];
    $response_array["note"] = $row["note"];
    $response_array["pace"] = $row["pace"];
    $response_array["plan_id"] = $row["ref_id"];
    $response_array["cover"] = $row["cover"];
    $response_array["name"] = "Jojo's Bizarre Adventure";
    $response[$x]=$response_array;
}
// $ans["plans"]=$response;


echo json_encode($ans);