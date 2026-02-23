# Juego de Plataformas: Rescata a la Princesa

Un juego de plataformas creado con Python y Pygame donde debes llegar hasta la princesa esquivando enemigos y bombas.

---

## Como se juega

- **Flecha izquierda / derecha** — mover al heroe
- **Flecha arriba** — saltar
- **Cierra la ventana** — salir del juego

**Ganas** si llegas a tocar a la princesa.
**Pierdes** si un enemigo te toca, pisas una bomba, o caes al vacio.

---

## Imagenes necesarias (carpeta `images2/`)

| Archivo | Descripcion |
|---|---|
| `cave.png` | Fondo de cueva que se repite |
| `m1.png` | Imagen del heroe |
| `enemy.png` | Imagen del enemigo |
| `bomb.png` | Imagen de la bomba |
| `princess.png` | Imagen de la princesa (objetivo final) |

---

## Historias de usuario — construye el juego paso a paso

Cada historia es una tarea pequena. Completaias en orden y al final tendras el juego funcionando.

---

### Historia 1 — Abrir una ventana

> **Como jugador, quiero ver una ventana en la pantalla para que el juego tenga un lugar donde mostrarse.**

**Que hay que hacer:**
1. Importar `pygame`.
2. Llamar a `pygame.init()`.
3. Crear una ventana de 800 x 600 con `pygame.display.set_mode`.
4. Ponerle un titulo con `pygame.display.set_caption`.
5. Hacer un ciclo `while` que mantenga la ventana abierta hasta que el usuario la cierre.

**Como saber que funciona:** Se abre una ventana negra y no se cierra sola.

---

### Historia 2 — Dibujar el fondo

> **Como jugador, quiero ver un fondo de cueva para que el juego se vea bonito.**

**Que hay que hacer:**
1. Cargar la imagen `cave.png` con `pygame.image.load`.
2. Escalarla al tamano de la ventana con `pygame.transform.scale`.
3. Dibujarla en la ventana con `window.blit` dentro del ciclo principal.
4. Actualizar la pantalla con `pygame.display.update()`.

**Como saber que funciona:** La ventana muestra la imagen de la cueva.

---

### Historia 3 — Crear al heroe

> **Como jugador, quiero ver a mi personaje en la pantalla para saber donde estoy.**

**Que hay que hacer:**
1. Crear una clase `Hero` que herede de `pygame.sprite.Sprite`.
2. En el constructor (`__init__`), cargar la imagen del heroe y guardarla en `self.image`.
3. Crear `self.rect` usando `self.image.get_rect()` y ponerlo en una posicion inicial (x=20, y=10).
4. Crear un grupo `all_sprites` y agregar al heroe.
5. Dibujar el grupo con `all_sprites.draw(window)`.

**Como saber que funciona:** Se ve el heroe sobre el fondo de cueva.

---

### Historia 4 — Mover al heroe con el teclado

> **Como jugador, quiero mover a mi personaje con las flechas del teclado para poder jugar.**

**Que hay que hacer:**
1. Agregar las propiedades `self.x_speed` y `self.y_speed` al heroe (empiezan en 0).
2. Crear el metodo `update(self)` en `Hero` que sume la velocidad a la posicion del rectangulo.
3. Detectar eventos `KEYDOWN` y `KEYUP` en el ciclo principal.
4. Al presionar la flecha derecha, poner `x_speed = 5`; al soltarla, `x_speed = 0`.
5. Hacer lo mismo con la flecha izquierda usando `x_speed = -5`.
6. Llamar a `all_sprites.update()` en cada iteracion del ciclo.

**Como saber que funciona:** El heroe se mueve a izquierda y derecha con las flechas.

---

### Historia 5 — Agregar gravedad y salto

> **Como jugador, quiero que mi personaje caiga y pueda saltar para que el juego sea un plataformero.**

**Que hay que hacer:**
1. Crear el metodo `gravitate(self)` en `Hero`: aumenta `y_speed` en 0.25 cada fotograma.
2. Llamar a `gravitate()` dentro de `update()` antes de mover en Y.
3. Crear el metodo `jump(self, y)` que pone `y_speed = y` (usa -7 para saltar hacia arriba).
4. Agregar la propiedad `self.stands_on = False` para saber si el heroe esta en el suelo.
5. Detectar la tecla flecha arriba y llamar `robin.jump(-7)`.

**Como saber que funciona:** El heroe cae hacia abajo y al presionar arriba salta, pero atraviesa todo porque aun no hay plataformas.

---

### Historia 6 — Crear plataformas y paredes

> **Como jugador, quiero que haya plataformas para poder caminar sobre ellas y no caer al vacio.**

**Que hay que hacer:**
1. Crear la clase `Wall` que herede de `pygame.sprite.Sprite`.
2. En el constructor, crear `self.image` como un `pygame.Surface` del tamano indicado y rellenarlo de color verde.
3. Crear `self.rect` y posicionarlo en (x, y).
4. Crear un grupo `barriers` y agregar varias paredes:
   - Piso: `Wall(-200, 590, 1600, 20)` — piso largo
   - Plataforma 1: `Wall(50, 150, 480, 20)`
   - Plataforma 2: `Wall(350, 380, 640, 20)`
   - Pared lateral: `Wall(700, 50, 50, 360)`
5. Agregar todas las paredes a `all_sprites` tambien.

**Como saber que funciona:** Aparecen rectangulos verdes en la pantalla.

---

### Historia 7 — Detectar colisiones con plataformas

> **Como jugador, quiero que mi personaje se detenga al pisar una plataforma para poder caminar sobre ella.**

**Que hay que hacer:**
1. En el metodo `update()` del heroe, despues de mover en X, usar `pygame.sprite.spritecollide(self, barriers, False)` para detectar colisiones.
2. Si va a la derecha, alinear `self.rect.right` con el borde izquierdo de la pared tocada.
3. Si va a la izquierda, alinear `self.rect.left` con el borde derecho de la pared tocada.
4. Despues de mover en Y, hacer lo mismo:
   - Si baja y toca una plataforma: poner `y_speed = 0`, alinear `rect.bottom` con `p.rect.top` y guardar `self.stands_on = p`.
   - Si sube y toca una plataforma: poner `y_speed = 0` y alinear `rect.top` con `p.rect.bottom`.
5. Actualizar `stands_on = False` al subir para que no salte en el aire.

**Como saber que funciona:** El heroe camina sobre las plataformas y puede saltar solo cuando esta parado.

---

### Historia 8 — Hacer que la camara siga al heroe (scroll)

> **Como jugador, quiero que la pantalla se mueva cuando camino para poder explorar el mundo.**

**Que hay que hacer:**
1. Crear las variables `left_bound = 20` y `right_bound = 680` (los limites de movimiento visible).
2. Crear la variable `shift = 0` que guarda cuanto se ha desplazado el mundo.
3. En el ciclo principal, detectar si el heroe salio de los limites.
4. Si salio, mover todos los sprites del grupo `all_sprites` en la direccion opuesta al movimiento del heroe.
5. Para el fondo, calcular `local_shift = shift % win_width` y dibujarlo dos veces para que se repita sin cortes.

**Como saber que funciona:** Cuando el heroe llega al borde derecho o izquierdo, el mundo se desplaza.

---

### Historia 9 — Crear enemigos que se mueven

> **Como jugador, quiero que haya enemigos que se muevan para que el juego sea un reto.**

**Que hay que hacer:**
1. Crear la clase `Enemy` que herede de `pygame.sprite.Sprite`.
2. Cargar la imagen `enemy.png` en el constructor.
3. Crear el metodo `update(self)` que mueve al enemigo de forma aleatoria con `randint(-5, 5)` en X e Y.
4. Crear un grupo `enemies` y agregar dos enemigos en posiciones distintas.
5. Agregar los enemigos a `all_sprites` tambien.

**Como saber que funciona:** Aparecen enemigos que se mueven de forma impredecible.

---

### Historia 10 — Perder al tocar un enemigo

> **Como jugador, quiero que el juego termine si toco un enemigo para que haya consecuencias.**

**Que hay que hacer:**
1. Despues de actualizar los sprites, usar `pygame.sprite.spritecollide(robin, enemies, False)`.
2. Si hay colision, llamar `robin.kill()` para eliminar al heroe del juego.
3. Tambien terminar el juego si el heroe cae fuera de la pantalla (`robin.rect.top > win_height`).
4. Mostrar el texto "JUEGO TERMINADO" en rojo sobre fondo negro usando `font.render`.

**Como saber que funciona:** Al tocar un enemigo o caer al vacio, aparece la pantalla de derrota.

---

### Historia 11 — Agregar bombas

> **Como jugador, quiero que haya bombas en el suelo para tener que esquivarlas.**

**Que hay que hacer:**
1. Crear un objeto `Enemy` pero con la imagen `bomb.png` y tamano 60x60.
2. Crear un grupo separado `bombs` y agregar la bomba (NO agregarla a `all_sprites`).
3. Dibujar el grupo de bombas por separado con `bombs.draw(window)`.
4. Usar `pygame.sprite.groupcollide(bombs, all_sprites, True, True)` para que al tocar cualquier sprite, tanto la bomba como el sprite sean eliminados.

**Como saber que funciona:** Si el heroe toca la bomba, ambos desaparecen y el juego termina.

---

### Historia 12 — Agregar la princesa y ganar el juego

> **Como jugador, quiero poder ganar el juego al llegar a la princesa para tener un objetivo.**

**Que hay que hacer:**
1. Crear la clase `FinalSprite` que herede de `pygame.sprite.Sprite`.
2. Cargar la imagen `princess.png` y posicionarla lejos a la derecha (fuera de la pantalla inicial).
3. Agregar a `all_sprites` para que se mueva con el scroll.
4. Usar `pygame.sprite.collide_rect(robin, pr)` para detectar cuando el heroe la toca.
5. Mostrar el texto "¡GANASTE!" en rojo sobre fondo negro.

**Como saber que funciona:** Al llegar hasta donde esta la princesa, aparece la pantalla de victoria.

---

## Resumen de tareas

| # | Historia | Concepto que aprendes |
|---|---|---|
| 1 | Abrir ventana | Inicializar Pygame, ciclo principal |
| 2 | Dibujar fondo | Cargar y mostrar imagenes |
| 3 | Crear heroe | Clases, Sprites, grupos |
| 4 | Mover con teclado | Eventos, velocidad |
| 5 | Gravedad y salto | Fisica basica, condiciones |
| 6 | Plataformas | Crear formas, grupos de colision |
| 7 | Colisiones | Deteccion y respuesta a colisiones |
| 8 | Camara / scroll | Desplazamiento del mundo |
| 9 | Enemigos | Movimiento aleatorio |
| 10 | Perder | Condiciones de derrota, texto |
| 11 | Bombas | Grupos de colision avanzados |
| 12 | Princesa / ganar | Condicion de victoria |

---

## Tecnologias usadas

- **Python 3**
- **Pygame** — biblioteca para crear videojuegos en Python

### Instalar Pygame

```bash
pip install pygame
```

### Ejecutar el juego

```bash
python juego2.py
```
