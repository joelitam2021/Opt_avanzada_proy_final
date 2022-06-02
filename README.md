<p align = "center">
    <img src="img/cinta.png" />
</p>
<p align = "center">
    <img src="img/logo_itam.png" />
</p>

## **Maestría en Ciencia de Datos**
### Temas Selectos de Modelado. Primavera 2022.

#### **Equipo 1** 

- Nyrma Paulina Hernández Trejo
- Aide Jazmín González Cruz
- Joel Jaramillo Pacheco
- Jesús Enrique Miranda Blanco

<br>

<div align="center"><h1>Proyecto final</h1><br><h1>Arbitrage Identification Cycle in Crypto Trading</h1></div>
<p align = "center">
    <img src="img/crypto.png" />
</p>


## Objetivo

Resolver el tema de *Arbitrage Identification Cycle in Crypto Trading*, a través de encontrar  el camino más corto en un grafo dirigido ponderado, usando el método de *Bellman Ford*.

## Introducción

El trading consiste en la compra-venta de activos cotizados con mucha liquidez en un mercado que puede ser de acciones, divisas e inversiones. Este mercado financiero es electrónico y está regulado. Su objetivo es obtener un beneficio económico cuando la operación genera una plusvalía.

En esté proyecto se usará el método *Bellman Ford* el cuál calcula la ruta más corta desde un nodo origen hacia los demás nodos en un grafo dirigido con pesos en las aristas. La ventaja de este algoritmo es que los pesos pueden tomar valores negativos. Con ello se logrará identificar un ciclo que nos de la mayor plusvalía en la compra de criptomonedas.

## Documentación

- La documentación referente al proyecto lo encontrará en la siguiente liga: [Trabajo escrito](https://docs.google.com/document/d/1opfXYOtYeJna6cKLmkjdhPulqXCVLCwB1ScKlEkqVE8/edit#heading=h.35nkun2)


- La documentación del métiodo esta disponible en: [Algortimo Bellman Ford](https://joelitam2021.github.io/Opt_avanzada_proy_final/)



## Descripción de archivos

- Carpeta [.github/workflows](.github/workflows): Contiene los archivos *.yml* encargados de lanzar la construcción del *docker*, la documentación del paquete y el lanzamiento de los *tests*

- Carpeta [aws](aws): Contiene evidencia del uso de la infraestructura de aws, con las herramientas de *Kale* y *KUbeflow*.

- Carpeta [data](data): Contiene los datos que se utilizaron para alimentar las corridas del método, consiten en un histórico diario de días del mes de mayo, referntes a precios de diferentes criptomonedas.

- Carpeta [docs](docs): Contiene el trabajo escrito del presente proyecto, así como la presentación del mismo.

- Carpeta [notebooks](notebooks): Contiene *notebooks* trabajados a lo largo del desarrollo del proyecto .

- Carpeta [src](src): Contiene el código del paquete *bellman ford*, y funciones auxiliares para la carga de datos y trasformación, así como documentación.

- Archivo [pipeline_bellman_ford.ipynb](pipeline_bellman_ford.ipynb): es el pipeline final con dos casos ejemplo de corrida, es un pipeline tagueado para correr con el *docker* generado y herramientas como  *Kale* y *KUbeflow*.

- Archivo [requirements.txt](requirements.txt): listado de paqueterías necesarias para el paquete y test.

- Archivo [setup.py](setup.py): instalador del paquete.

- Archivo [test.py](test.py): archivo que contiene los test al paquete.


## Dokerfile
Se cuenta con una imagen de docker que contiene preisntalado la nueva version del paquete creado para ejecutar el método de Bellman Ford, en este link se puede ver el [Dockerfile](dockerfiles/pkg/Dockerfile)

Para ejecutar el docker se usa la siguiente instrucción:

```
docker run --rm -v \<ruta a mi directorio\> :/datos --name jupyterlab_practica2 -p 8888:8888 -d joelitam2021/pkg_proy_final:0.1
```
donde ***\<ruta a mi directorio\>*** deberá sustituirse por la ruta local donde desee clonar este *docker*.

Después de correr la imagen de docker en su computadora, podrá acceder al *jupyterlab* a través de un *browser* usando la siguiente dirección:

http://localhost:8888

Le pedirá una contraseña, que por default es ***qwerty***.

## Binder

Se cuenta con la opción de correr el paquete usando la herramienta de Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/joelitam2021/Opt_avanzada_proy_final/main)


## Referencias

1 [¿Qué es el 'trading'?. BBVA. INVERSIONES Act. 17 feb 2021.](https://www.bbva.com/es/que-es-trading-que-hace-falta-para-operar/)

2 [¿Qué es y para qué sirve la tecnología blockchain?](https://www.solunion.cl/blog/que-es-y-para-que-sirve-la-tecnologia-blockchain/)

3 [¿Qué es el Trading de Criptomonedas?. Plus500.](https://www.plus500.com/es-ES/Trading/CryptoCurrencies/What-Is-Cryptocurrency-Trading~3)

4 [CoinMarketCap](https://coinmarketcap.com/es/all/views/all/)

5 [Algoritmo Bellman Ford](https://www.programiz.com/dsa/bellman-ford-algorithm)

6 [6.Minikube y AWS](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)

7 [Minikube, Kubeflow y Kale 2022](https://www.youtube.com/watch?v=SusT5xQN1ro)

