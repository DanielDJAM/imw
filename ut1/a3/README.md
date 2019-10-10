# Trabajo con Virtual Hosts

## Sitio web 1

Creamos dentro de ***/etc/nginx/sites-available/*** el fichero imw.alu5894.me y lo configuramos correctamente para crear el Virtual Host junto al location ***mec***.

![01](img/01.png)

En el directorio ***webapps*** creamos la carpeta que contenga todo lo relacionado al Virtual Host y como especificamos al configurarla previamente.

> Tanto el directorio como *imw* como *mec* tendrán sus propios indexs.

![02](img/02.png)

Descargamos la imagen del **Diagrama de unidades de trabajo** en la máquina de desarrollo y la enviamos mediante ssh a la máquina de producción.

![03](img/03.png)

A continuación, creamos un index.html en el directorio ***imw*** y añadimos la imagen.

> Previamente movemos la imagen de Documentos a /webapps/imw/img.

![04](img/04.png)

Recargamos el nginx y comprobamos.

![05](img/reload.png)
![06](img/05.png)

Ya tenemos creado todo lo relacionado con imw, por lo que vamos a trabajar con ***mec***. Creamos un index y añadimos un enlace que nos lleve al Real Decreto del título de administración de Sistemas informáticos en Red mediante.

![07](img/06.png)

Recargamos el nginx y comprobamos.

![08](img/reload.png)
![09](img/07.png)

## Sitio web 2

Esta vez crearemos un Virtual Host que esté escuchando mediante el puerto 9000 y que muestre un listado de ficheros mediante enlaces simbólicos.

Comenzamos creando el Virtual Host ***varlib*** y configurandolo para que escuche por el puerto 9000 y añadimos autoindex para que reconozca todo el contenido del directorio deseado, en este caso, varlib.

![10](img/08.png)

En webapps, creamos el directorio correspondiente al Virtual Host y dentro de éste, creamos un enlace simbólico a ***/var/lib/***.

![11](img/09.png)

Recargamos el servicio nginx y comprobamos.

![12](img/reload.png)
![13](img/10.png)

## Sitio web 3

Creamos el Virtual Host correspondiente y lo configuramos para que su acceso sea restringido y se requiera de un usuario y contraseña. También vamos a restringir el paso al fichero donde se guarda esta información confidencial y crearemos eel location ***/students***.

> El location para /.htpasswd hace que retorne un error 403 si intentan acceder a él.

![14](img/12.png)

Creamos una contraseña, la "encriptamos" y la metemos en el fichero ***.htpasswd***.

![15](img/13.png)

![16](img/14.png)

Creamos el fichero index, recargamos el nginx y comprobamos.

![17](img/15.png)

![18](img/reload.png)

![19](img/17.png)

![20](img/403.png)

Para obtener un certificado de seguridad y conseguir que nuestra web sea https, tenemos que instalar certbot.

![21](img/18.png)

![22](img/19.png)

Después de instalarlo, nos hará una serie de preguntas:

```bash
alu5894@cloud:~$ sudo certbot --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx
Enter email address (used for urgent renewal and security notices) (Enter 'c' to
cancel): alu5894@iespuertodelacruz.es

-------------------------------------------------------------------------------
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server at
https://acme-v01.api.letsencrypt.org/directory
-------------------------------------------------------------------------------
(A)gree/(C)ancel: a

-------------------------------------------------------------------------------
Would you be willing to share your email address with the Electronic Frontier
Foundation, a founding partner of the Let's Encrypt project and the non-profit
organization that develops Certbot? We'd like to send you email about EFF and
our work to encrypt the web, protect its users and defend digital rights.
-------------------------------------------------------------------------------
(Y)es/(N)o: n

Which names would you like to activate HTTPS for?
-------------------------------------------------------------------------------
1: alu5894.me
2: hello.alu5894.me
3: imw.alu5894.me
4: ssl.alu5894.me
5: varlib.alu5894.me
-------------------------------------------------------------------------------
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel): 4
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for ssl.alu5894.me
Waiting for verification...
Cleaning up challenges
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/ssl.alu5894.me

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
-------------------------------------------------------------------------------
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/ssl.alu5894.me

-------------------------------------------------------------------------------
Congratulations! You have successfully enabled https://ssl.alu5894.me

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=ssl.alu5894.me
-------------------------------------------------------------------------------

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/ssl.alu5894.me/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/ssl.alu5894.me/privkey.pem
   Your cert will expire on 2020-01-05. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

alu5894@cloud:~$
```

Visualizamos el fichero del Virtual Host y vemos que certbot lo ha modificado.

![23](img/20.png)

Recargamos el nginx y comprobamos.

![24](img/reload.png)

![25](img/22.png)

![26](img/23.png)

![27](img/24.png)

## Sitio web 4

Creamos los Virtual Hosts requeridos.

![28](img/27.png)

Creamos en ***webapps*** los directorios de los Virtual Hosts

> En la imagen aparece que creamos más directorios pero no influyen en nada.

![29](img/28.png)

Descargamos en la máquina de desarrollo el archivo comprimido ***initializr.zip*** y lo pasamos a la máquina de producción a través de ssh.

![30](img/29.png)

Una vez traspasado el archivo, lo movemos a la ubicación deseada y lo descomprimimos.

> Una vez descomprimido, tendremos otro directorio llamado ***initializr*** y puede dar error en la ruta que configuramos. Por lo que podemos mover todo su contenido a /target o modificar la ruta en el fichero Virtual Host.

![31](img/30.png)


Recargamos y comprobamos.

![32](img/reload.png)

![33](img/31.png)

Modificamos el fichero ***redirect.alu5894.me*** y añadimos que escuche por el puerto 80 (porque es una página HTTP) y que redirija todas las peticiones que le lleguen al dominio de ***target.alu5894.me***. Además, también configuraremos para que los **logs** de acceso y error, de dicho Virtual Host, se guarden en una ruta específica.

![34](img/final.png)

![35](img/33.png)

Una vez terminado todo, recargamos y debería funcionar correctamente.

![36](img/reload.png)
