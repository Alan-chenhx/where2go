<?php

session_start();

include '../includes/db.php';
$_POST = json_decode(file_get_contents("php://input"), true);
$start = $_POST['start'];
$end = $_POST['end'];
$dest = $_POST['dest'];
$tag = $_POST['tags'];
$days = $_POST['days'];
$pace = $_POST['pace'];
$name = $_POST['name'];
$cover = '';
$note = '';


// $start = '2019-02-01';
// $end = '2019-02-06';
// $tag = ["wildlife", "shopping"];
// $dest = ["Los Angeles", "Mountain View"];
// $days = 1;
// $pace = "medium";
$user_id = $_SESSION['user_id'];
// $user_id=1;
// $name = "asdkjsa";

$str = "*";
foreach ($dest as &$d) {
    $tmp = str_replace(" ", "-", $d);
    $str = $str.",".$tmp;
}
$str = str_replace("*,", "", $str);

$str1 = "*";
foreach ($tag as &$t) {
    $tmp = str_replace(" ", "-", $t);
    $str1 = $str1.",".$tmp;
}
$str1 = str_replace("*,", "", $str1);
$to_exec = "python3 add_iter.py ".$str." ".$str1." ".$days." ".$pace;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
$output=json_decode($output);
// echo $output;

$cover=$output[1];
$output=$output[0];
$new_dest = str_replace('"', '*', json_encode($dest));
$new_tag = str_replace('"', '*', json_encode($tag));

$query = mysqli_query($conn, "INSERT INTO plans (user_id, name, start, end, dest, tag, cover, note, pace, ref_id)
                              VALUES ($user_id, '$name', '$start', '$end', '$new_dest', '$new_tag', '$cover', '$note', '$pace', $output);");
echo $output;
// echo $cover;
