<?php
function getQuote()
{
    $file = 'parse/data.txt';
    $line = file_get_contents($file, true);
    $line = explode(';', $line);
    array_pop($line);

    $num = mt_rand(0, count($line) - 1);

    return $line[$num];
}

if (isset($_GET)) {
    $data = getQuote();
    echo json_encode($data);
}