<?php

$nombre = $_POST["nombre"];
$años = (int)($_POST["años"]);
$salario = (float)($_POST["salario"]);


if ($salario > 1000 and $salario <= 2000) {
  if ($años > 45) {
    $salario = $salario + ($salario * 3 / 100);
  }
  elseif ($años <= 45)  {
    $salario = $salario + ($salario * 10 / 100);
  }
}
elseif ($salario < 1000) {
  if ($años < 30) {
    $salario = 1100;
  }
  elseif ($años > 30 and $años < 45) {
    $salario = $salario + ($salario * 3 / 100);
  }
  elseif ($años > 45) {
    $salario = $salario + ($salario * 15 / 100);
  }
}
echo "El nuevo salario de $nombre es $salario";
 ?>
