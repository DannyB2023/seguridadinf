<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Encriptador César</title>
</head>
<body>
    <form method="post">
        <label for="mensaje">Ingrese el mensaje a encriptar:</label><br>
        <input type="text" id="mensaje" name="mensaje"><br>
        <label for="desplazamiento">Ingrese el desplazamiento:</label><br>
        <input type="number" id="desplazamiento" name="desplazamiento"><br><br>
        <input type="submit" value="Encriptar">
    </form>

    <?php
    function cifrarCesar($mensaje, $desplazamiento) {
        $resultado = '';

        // Recorremos cada carácter del mensaje
        for ($i = 0; $i < strlen($mensaje); $i++) {
            // Obtenemos el código ASCII del carácter actual
            $codigoAscii = ord($mensaje[$i]);
            
            // Aplicamos el desplazamiento al código ASCII
            $nuevoCodigoAscii = $codigoAscii + $desplazamiento;

            // Verificamos si el carácter es una letra mayúscula
            if (ctype_upper($mensaje[$i])) {
                // Aseguramos que el nuevo código ASCII esté dentro del rango de letras mayúsculas
                while ($nuevoCodigoAscii > ord('Z')) {
                    $nuevoCodigoAscii -= 26; // El alfabeto tiene 26 letras
                }
            }
            // Verificamos si el carácter es una letra minúscula
            elseif (ctype_lower($mensaje[$i])) {
                // Aseguramos que el nuevo código ASCII esté dentro del rango de letras minúsculas
                while ($nuevoCodigoAscii > ord('z')) {
                    $nuevoCodigoAscii -= 26; // El alfabeto tiene 26 letras
                }
            }
            // Concatenamos el carácter encriptado al resultado
            $resultado .= chr($nuevoCodigoAscii);
        }

        return $resultado;
    }

    // Verificar si se ha enviado el formulario
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Obtener el mensaje y el desplazamiento desde el formulario
        $mensajeOriginal = $_POST["mensaje"];
        $desplazamiento = (int)$_POST["desplazamiento"];

        // Encriptar el mensaje
        $mensajeEncriptado = cifrarCesar($mensajeOriginal, $desplazamiento);

        echo "<br>Mensaje encriptado: $mensajeEncriptado";
    }
    ?>
</body>
</html>