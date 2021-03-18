<?php

require_once 'database.php';
ini_set('memory_limit', '1000M');
$ram="1GB";
echo '<div style="width: 100%; font-weight: bold; font-size: 16pt;">';
echo "PHP (RAM: ".$ram.")<br><br>";
echo '</div>';

//Lodaing database test - start
$startTime = new DateTime();
$totalTime = new DateTime('00:00');

echo "Loading database...<br>";

$result = $connection->query("SELECT location, new_cases FROM covid");
if($result==false) {
    throw new Exception($connection->error);
}

$database = array();
while($rows = $result->fetch_row()) {
    $database[] = $rows;
}
echo 'Loaded '.count($database).' rows ('.count($database[0]).' columns each).<br>';

$stopTime = new DateTime();
$difference = $startTime->diff($stopTime);
$totalTime->add($difference);
echo 'Elapsed time (database load): '.$difference->format('%Im %Ss %Fms').' (Started: '.$startTime->format('H:i:s:u').', Finished: '.$stopTime->format('H:i:s:u').')<br><br>';
//Lodaing database test - stop

//Executing script test - start
echo "Executing script...<br>";
$startTime = new DateTime();

//----------------------------------------------------------------------------------------------------
$dataSet = array();
foreach ($database as $row) {
    $location = $row[0];
    $new_cases = (float)$row[1];

    if(array_key_exists($location, $dataSet)) {
        $dataSet[$location][0] += $new_cases;
        $dataSet[$location][1] += 1;
    }
    else {
        $dataSet[$location] = array($new_cases, 1);
    }
}

echo "<br>";
foreach ($dataSet as $locationName => $locationData){
    echo $locationName.": ".$locationData[0] / $locationData[1]."<br>";
}
//----------------------------------------------------------------------------------------------------

$stopTime = new DateTime();
$difference = $startTime->diff($stopTime);
$totalTime->add($difference);
echo 'Elapsed time (script execution): '.$difference->format('%Im %Ss %Fms').' (Started: '.$startTime->format('H:i:s:u').', Finished: '.$stopTime->format('H:i:s:u').')<br><br>';
//Executing script test - stop

echo 'Total time elapsed: '.$totalTime->format('H:i:s:u').' ';

die();