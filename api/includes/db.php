<?php

require_once('config.php');

$conn = mysqli_connect($databaseHost, $databaseUser, $databasePwd, $databaseName);

if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

?>