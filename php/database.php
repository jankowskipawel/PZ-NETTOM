<?php
try {
    $config = require_once 'config.php';

    $connection = new mysqli($config['host'], $config['user'], $config['password'], $config['database']);

    if($connection->connect_errno != 0) {
        throw new Exception(mysqli_connect_errno());
    }
} catch (Exception $e) {
    echo "Connection error: ".$e;
    exit();
}