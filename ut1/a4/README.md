# Sitio Web 1

Descargamos el Zip necesario para la práctica y lo compartimos con la máquina de producción mediante ssh.

![01](img/01.png)

Descomprimimos.

![02](img/02.png)

Creamos el Virtual Host, lo configuramos para que lea el index indicado y un location que todo lo parecido a la extensión php, sea leido por un socket específico que indicaremos. Este Virtual Host fue creado en sites-available y enlazado a sites-enabled con un enlace simbólico (ln -s).

![04](img/05.png)

![03](img/03.png)

Recargamos nginx y comprobamos.

![05](img/04.png)

![06](img/06.png)

# Sitio Web 2

Creamos el directorio donde alojaremos un entorno virtual con algunas aplicaciones extra como flask y pytz.

![07](img/07.png)

Creamos y configuramos un fichero específico para nuestro Virtual Host.

![08](img/08.png)

Comprobamos el estado del supervisor e iniciamos el proceso "now".

![09](img/09.png)

Creamos un script en python que ejecute el comando asignado para que lea el archivo python (en este caso, main.py).

![10](img/10.png)

Creamos el Virtual Host y lo configuramos.

![11](img/11.png)

Enlazamos con sites-enabled.

![12](img/12.png)

Recargamos nginx y comprobamos.

![13](img/04.png)

![14](img/13.png)
