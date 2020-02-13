<html>

  <head>
    <meta charset="utf-8">
  </head>

  <body>


      <?php
          if (isset($_GET["filas"]) and isset($_GET["columnas"])) {
            $columnas = (int) $_POST["columnas"];
            $filas = (int) $_POST["filas"];
          }
      ?>
        <table border = "2px solid black">
          <?php
            if (($filas < 1) or ($columnas < 1)) {
              echo ("Entrada erronea");
            }

            else {
              for ($c=1; $c<=$columnas; $c++) {
                echo ("<tr>");
                for ($f=1, $f<=$filas; $f++){
                echo ("<td></td>");
                }
                echo ("</tr>");
             }
           }
          ?>
      </table>
    </body>
</html>
