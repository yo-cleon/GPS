# GPS Y RASPBERRY PI

Creación de una aplicación para la lectura de datos gps utilizando una raspberry pi 3, con un módulo GPS <a href="https://www.dx.com/p/gy-neo6mv2-flight-controller-gps-module-blue-232595#.W_P0_ej7SUk" target="_blank">GY-NEO-6Mv2</a>

<h3>Requerimientos</h3>
<ul>
<li> Python 2.7</li>
<li>Es necesario la instalación de la librería <a href= "https://github.com/Knio/pynmea2">pynmea2</a>:
  <pre><code>pip install pynmea2</code></pre></li>
</ul>

<h3>Curiosidades</h3>
<p>El dispositivo está pensado para instalarlo en un vehículo perteneciente a una flota, por lo que, para identificarlo más facilmente se asigna la matrícula del vehículo como hostname de la Raspberry Pi. 
<pre></code>sudo nano /etc/hostname</code></pre>
</p>
<p>Para poder controlar el dispositivo de forma remota podemos utilizar algún servicio de DDNS. En este caso, hemos utilizado NO-IP.: 
</p
