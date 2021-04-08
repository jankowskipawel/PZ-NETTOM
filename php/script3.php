<?php

require_once 'database.php';
ini_set('memory_limit', '1000M');
$ram="1GB";
echo '<div style="width: 100%; font-weight: bold; font-size: 16pt;">';
echo "PHP (RAM:".$ram.")<br><br>";
echo '</div>';

//Lodaing database test - start
$startTime = new DateTime();
$totalTime = new DateTime('00:00');

echo "Loading database...<br>";

$result = $connection->query("SELECT * FROM covid");
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
echo "script executing...<br>";
$startTime = new DateTime();

//----------------------------------------------------------------------------------------------------
function multiplyRecords($dataset, $multiplier)
{
    $multipliedDataset = $dataset;
    for($i = 1; $i < $multiplier; $i++) {
        $multipliedDataset = array_merge($multipliedDataset, $dataset);
    }

    return $multipliedDataset;
}

function emptyToPi(&$dataset)
{
    for ($row = 0; $row < count($dataset); $row++) {
        for($col = 4; $col < count($dataset[$row]); $col++) {
            if(is_numeric($dataset[$row][$col])) {
                $dataset[$row][$col] = (float)$dataset[$row][$col];
            }
            else {
                $dataset[$row][$col] = M_PI;
            }
        }
    }
}

function emptyToRandom(&$dataset, $minRandom, $maxRandom)
{
    for ($row = 0; $row < count($dataset); $row++) {
        for($col = 4; $col < count($dataset[$row]); $col++) {
            if(is_numeric($dataset[$row][$col])) {
                $dataset[$row][$col] = (float)$dataset[$row][$col];
                #$dataset[$row][$col] = (int)$dataset[$row][$col];
            }
            else {
                $dataset[$row][$col] = (float)rand($minRandom, $maxRandom);
                #$dataset[$row][$col] = (int)rand($minRandom, $maxRandom);
            }
        }
    }
}

function ciezkiSkrypt(&$dataset)
{
    for ($row = 0; $row < count($dataset); $row++) {
        for($col = 4; $col < count($dataset[$row]); $col++) {
            if(is_numeric($dataset[$row][$col])) {
                $dataset[$row][$col] = log(
                    pow(pow($dataset[$row][$col], 1 / 3) + pow($dataset[$row][$col], 1 / 2), 50) /
                    (round((pow(pow($dataset[$row][$col], 1 / 3) - pow($dataset[$row][$col], 1 / 2), 50)), 2) + 1)
                );
            }
        }
    }
}

$database = multiplyRecords($database, 2);
emptyToPi($database);
#emptyToRandom($database, 1, 10);
ciezkiSkrypt($database);


echo 'Script executed for '.count($database).' rows ('.count($database[0]).' columns each).<br>';
/*  wypisanie całej bazy

  foreach ($database as $row) {
    foreach ($row as $value) {
        echo " | ".$value;
    }
    echo " |<br><br>";
} */
//----------------------------------------------------------------------------------------------------

$stopTime = new DateTime();
$difference = $startTime->diff($stopTime);
$totalTime->add($difference);
echo '<br>Elapsed time (script execution): '.$difference->format('%Im %Ss %Fms').' (Started: '.$startTime->format('H:i:s:u').', Finished: '.$stopTime->format('H:i:s:u').')<br><br>';
//Executing script test - stop

echo 'Total time elapsed: '.$totalTime->format('H:i:s:u').' ';

$ram = null;
$database = null;
$startTime = null;
$stopTime = null;
$totalTime = null;
unset($ram);
unset($database);
unset($startTime);
unset($stopTime);
unset($totalTime);
die();