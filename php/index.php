<?php

require_once 'database.php';
ini_set('memory_limit', '1000M');
$ram="1GB";
echo '<div style="width: 100%; font-weight: bold; font-size: 16pt;">';
echo "PHP (RAM: ".$ram.")<br><br>";
echo '</div>';
$startTime = new DateTime();
$totalTime = new DateTime('00:00');
// echo "Czas rozpoczęcia: ".$startTime->format('H:i:s:u')."<br><br>";
echo "Loading database...<br>";
$result = $connection->query("SELECT * FROM covid ORDER BY location ASC");
if($result==false) {
    throw new Exception($connection->error);
}

//database - array[array[str]]
$database = array();
while($rows = $result->fetch_row()) {
    
    $database[] = $rows;
}
echo 'Loaded '.count($database).' rows ('.count($database[0]).' columns each).<br>';
// echo $database[0][3];

$stopTime = new DateTime();

$difference = $startTime->diff($stopTime);
$totalTime->add($difference);
echo 'Elapsed time (database load): '.$difference->format('%Im %Ss %Fms').' (Started: '.$startTime->format('H:i:s:u').', Finished: '.$stopTime->format('H:i:s:u').')<br><br>';

echo "Executing script...<br>";
$startTime = new DateTime();

//############insert script here############


$stopTime = new DateTime();
$difference = $startTime->diff($stopTime);
$totalTime->add($difference);
echo 'Elapsed time (script execution): '.$difference->format('%Im %Ss %Fms').' (Started: '.$startTime->format('H:i:s:u').', Finished: '.$stopTime->format('H:i:s:u').')<br><br>';
echo 'Total time elapsed: '.$totalTime->format('H:i:s:u').' ';
die();
