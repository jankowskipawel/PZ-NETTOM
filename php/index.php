<?php

require_once 'database.php';
ini_set('memory_limit', '1000M');
$startTime = new DateTime();
echo "Czas rozpoczęcia: ".$startTime->format('H:i:s:u')."<br><br>";

$result = $connection->query("SELECT * FROM covid ORDER BY location ASC");
if($result==false) {
    throw new Exception($connection->error);
}

echo 'Wczytano rekordów: '.mysqli_num_rows($result).'<br><br>';
//database - variable with whole database
$database = array();
while($rows = $result->fetch_row()) {

    $database[] = $rows;
}
echo $database[0][3];

$stopTime = new DateTime();
echo "Czas zakończenia: ".$stopTime->format('H:i:s:u')."<br><br>";

$difference = $startTime->diff($stopTime);
echo "Czas trwania: ".$difference->format('%Im %Ss %Fms');

die();
