<?php

include '../includes/db.php';
$_POST = json_decode(file_get_contents("php://input"), true);
$start = $_POST['start'];
$end = $_POST['end'];
$dest = $_POST['dest'];
$tag = $_POST['tag'];
$days = $_POST['days'];
$pace = $_POST['pace'];
$cover = '';
$note = '';


$tag = ["wildlife", "shopping"];
$dest = ["Los Angeles", "Mountain View"];
$days = 5;
$pace = "medium";

//$query = mysqli_query($conn, "INSERT INTO plans (start, end, dest, tag, cover, note, pace)
//                              VALUES ($start, $end, $dest, $tag, $cover, $note, $pace);");

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
$to_exec = "python add_iter.py ".$str." ".$str1." ".$days." ".$pace;
echo $to_exec;
$command = escapeshellcmd($to_exec);
$output = shell_exec($command);
echo $output;
