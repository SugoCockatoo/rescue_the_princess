# Juego de Plataformas: Rescata a la Princesa

Un juego de plataformas donde debes llegar hasta la princesa esquivando enemigos y bombas.

---

## Como se juega

- **Flecha izquierda / derecha** — mover al heroe
- **Flecha arriba** — saltar
- **Cierra la ventana** — salir del juego

**Ganas** si llegas a tocar a la princesa.
**Pierdes** si un enemigo te toca, pisas una bomba, o caes al vacio.

---

## Historias de usuario — construye el juego paso a paso

Cada historia es una tarea pequena. Completalas en orden y al final tendras el juego funcionando.

---

### Historia 1 — Abrir una ventana

> **Como jugador, quiero ver una ventana en la pantalla para que el juego tenga un lugar donde mostrarse.**

**Que hay que hacer:**
1. Preparar el programa para usar la libreria de videojuegos.
2. Crear una ventana de 800 x 600 pixeles.
3. Ponerle un titulo a la ventana.
4. Hacer que el programa se mantenga abierto hasta que el usuario cierre la ventana.

**Como saber que funciona:** Se abre una ventana y no se cierra sola.

---

### Historia 2 — Dibujar el fondo

> **Como jugador, quiero ver un fondo de cueva para que el juego se vea bonito.**

**Que hay que hacer:**
1. Cargar la imagen de la cueva.
2. Ajustarla para que cubra toda la ventana.
3. Dibujarla en la ventana cada vez que el juego se actualiza.

**Como saber que funciona:** La ventana muestra la imagen de la cueva.

---

### Historia 3 — Crear al heroe

> **Como jugador, quiero ver a mi personaje en la pantalla para saber donde estoy.**

**Que hay que hacer:**
1. Crear un personaje heroe con su imagen.
2. Colocarlo en la esquina superior izquierda de la pantalla.
3. Mostrarlo sobre el fondo de la cueva.

**Como saber que funciona:** Se ve el heroe sobre el fondo de cueva.

---

### Historia 4 — Mover al heroe con el teclado

> **Como jugador, quiero mover a mi personaje con las flechas del teclado para poder jugar.**

**Que hay que hacer:**
1. Hacer que el heroe tenga una velocidad horizontal que empieza en cero.
2. Cuando se presiona la flecha derecha, el heroe se mueve hacia la derecha.
3. Cuando se presiona la flecha izquierda, el heroe se mueve hacia la izquierda.
4. Cuando se suelta la tecla, el heroe se detiene.

**Como saber que funciona:** El heroe se mueve a izquierda y derecha con las flechas.

---

### Historia 5 — Agregar gravedad y salto

> **Como jugador, quiero que mi personaje caiga y pueda saltar para que el juego sea un plataformero.**

**Que hay que hacer:**
1. Hacer que el heroe caiga hacia abajo poco a poco, como si hubiera gravedad.
2. Al presionar la flecha arriba, el heroe salta hacia arriba.
3. El heroe solo puede saltar si esta parado sobre algo, no en el aire.

**Como saber que funciona:** El heroe cae hacia abajo y al presionar arriba salta, pero atraviesa todo porque aun no hay plataformas.

---

### Historia 6 — Crear plataformas y paredes

> **Como jugador, quiero que haya plataformas para poder caminar sobre ellas y no caer al vacio.**

**Que hay que hacer:**
1. Crear un tipo de objeto que representa una plataforma o pared, dibujada como un rectangulo de color.
2. Colocar un piso largo en la parte de abajo de la pantalla.
3. Colocar dos plataformas flotantes a distintas alturas.
4. Colocar una pared vertical en la parte derecha.

**Como saber que funciona:** Aparecen rectangulos de color en la pantalla.

---

### Historia 7 — Detectar colisiones con plataformas

> **Como jugador, quiero que mi personaje se detenga al pisar una plataforma para poder caminar sobre ella.**

**Que hay que hacer:**
1. Cuando el heroe choca con una plataforma por el lado, que no pueda atravesarla.
2. Cuando el heroe cae sobre una plataforma, que se detenga encima de ella.
3. Cuando el heroe salta y choca con una plataforma por abajo, que rebote hacia abajo.
4. El heroe solo puede saltar cuando esta parado sobre una plataforma.

**Como saber que funciona:** El heroe camina sobre las plataformas y puede saltar solo cuando esta parado.

---

### Historia 8 — Hacer que la camara siga al heroe

> **Como jugador, quiero que la pantalla se mueva cuando camino para poder explorar el mundo.**

**Que hay que hacer:**
1. Definir una zona central donde el heroe se mueve libremente.
2. Cuando el heroe llega al borde de esa zona, todo el mundo se desplaza en vez de seguir moviendose el heroe.
3. El fondo de cueva debe repetirse sin cortes al desplazarse.

**Como saber que funciona:** Cuando el heroe llega al borde, el mundo se desplaza y aparecen nuevas areas.

---

### Historia 9 — Crear enemigos que se mueven

> **Como jugador, quiero que haya enemigos que se muevan para que el juego sea un reto.**

**Que hay que hacer:**
1. Crear un tipo de objeto enemigo con su imagen.
2. Hacer que el enemigo se mueva de forma impredecible en todas direcciones.
3. Colocar dos enemigos en distintas zonas del nivel.

**Como saber que funciona:** Aparecen enemigos que se mueven de forma impredecible.

---

### Historia 10 — Perder al tocar un enemigo

> **Como jugador, quiero que el juego termine si toco un enemigo para que haya consecuencias.**

**Que hay que hacer:**
1. Detectar cuando el heroe toca a un enemigo y eliminarlo de la pantalla.
2. Tambien terminar el juego si el heroe cae fuera de la pantalla por abajo.
3. Mostrar el mensaje "JUEGO TERMINADO" en letras rojas sobre fondo negro.

**Como saber que funciona:** Al tocar un enemigo o caer al vacio, aparece la pantalla de derrota.

---

### Historia 11 — Agregar bombas

> **Como jugador, quiero que haya bombas en el suelo para tener que esquivarlas.**

**Que hay que hacer:**
1. Colocar una bomba en el nivel usando su imagen.
2. La bomba no se mueve, solo espera que alguien la toque.
3. Si el heroe u otro personaje toca la bomba, ambos desaparecen.

**Como saber que funciona:** Si el heroe toca la bomba, ambos desaparecen y el juego termina.

---

### Historia 12 — Agregar la princesa y ganar el juego

> **Como jugador, quiero poder ganar el juego al llegar a la princesa para tener un objetivo.**

**Que hay que hacer:**
1. Colocar a la princesa muy lejos a la derecha, fuera de la pantalla inicial.
2. La princesa se desplaza junto con el mundo al moverse la camara.
3. Cuando el heroe la toca, mostrar el mensaje "GANASTE" en letras rojas sobre fondo negro.

**Como saber que funciona:** Al llegar hasta donde esta la princesa, aparece la pantalla de victoria.

---

## Resumen de tareas

| # | Historia | Que aprendes |
|---|---|---|
| 1 | Abrir ventana | Iniciar el juego y mantenerlo abierto |
| 2 | Dibujar fondo | Mostrar imagenes en pantalla |
| 3 | Crear heroe | Personajes y su posicion |
| 4 | Mover con teclado | Responder a las teclas del jugador |
| 5 | Gravedad y salto | Simular fisica basica |
| 6 | Plataformas | Crear el escenario del juego |
| 7 | Colisiones | Detectar cuando dos cosas se tocan |
| 8 | Camara | Hacer que el mundo sea mas grande que la pantalla |
| 9 | Enemigos | Movimiento automatico de personajes |
| 10 | Perder | Condiciones de derrota |
| 11 | Bombas | Objetos peligrosos estaticos |
| 12 | Princesa y victoria | Condicion de victoria y fin del juego |
