<?php
include 'includes/db.php';
$_POST = json_decode(file_get_contents("php://input"), true);
$ref_id = $_POST['plan_id'];
// $ref_id=123;
mysqli_query($conn,"DELETE FROM plans WHERE ref_id=$ref_id");