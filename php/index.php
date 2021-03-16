<?php

require_once 'database.php';

$startTime = new DateTime();
echo "Czas rozpoczęcia: ".$startTime->format('H:i:s:u')."<br><br>";

$result = $connection->query("SELECT * FROM covid ORDER BY location ASC");
if($result==false) {
    throw new Exception($connection->error);
}

echo 'Wczytano rekordów: '.mysqli_num_rows($result).'<br><br>';

for($i = 0; $i < mysqli_num_rows($result); $i++)
{
    $row= $result->fetch_assoc();
}

$stopTime = new DateTime();
echo "Czas zakończenia: ".$stopTime->format('H:i:s:u')."<br><br>";

$difference = $startTime->diff($stopTime);
echo "Czas trwania: ".$difference->format('%Im %Ss %Fms');

die();