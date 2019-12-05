<?php

include '../includes/db.php';
$_POST = json_decode(file_get_contents("php://input"), true);
$start = $_POST["start"];
$end = $_POST["end"];
$dest = $_POST["dest"];
$tag = $_POST["tag"];
$note = $_POST["note"];
$pace = $_POST["pace"];
$name = $_POST["name"];
$ref_id = $_POST["planId"];
// $start = "2019-02-06";
// $end = "2019-02-06";
// $dest = "[*Los Angeles*,*Mountain View*]";
// $tag = "[*wildlife*,*shopping*]";
// $note = "zasdasdasdj";
// $pace = "high";
$name = "zmj";

$ref_id = 123;
$start = '2019-02-01';
$end = '2019-02-06';
$tag = ["wildlife", "shopping"];
$dest = ["Los Angeles", "Mountain View"];
$days = 1;
$pace = "medium";
$user_id = $_SESSION['user_id'];

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
$new_dest = str_replace('"', '*', json_encode($dest));
$new_tag = str_replace('"', '*', json_encode($tag));

mysqli_query($conn,"UPDATE plans SET start='$start',end='$end',dest='$dest',tag='$tag',note='$note',pace='$pace',name='$name',ref_id='$output' where ref_id='$ref_id';");