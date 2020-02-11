<!doctype html>
<html lang="es">
	<head>
		<meta charset="utf-8">
		<title>Probando PHP!!</title>
	</head>
	<body>
      <form action="index.php" method="get">
        <label for="msg">Mensaje:</label>
        <input type="text" name="msg" /><br>
        <input type="submit" value="echo!" />
      </form>
      <?php
          if (isset ($_GET["msg"])) {
            $msg = $_GET["msg"];
            echo ("<p>$msg</p>");
          }
       ?>
	</body>
</html>
