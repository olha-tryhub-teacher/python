key_switch_camera = 'c'  # камера прив'язана до героя чи ні
key_switch_mode = 'i'  # можна проходити крізь перешкоди чи ні

key_forward = 'w'  # крок вперед (куди дивиться камера)
key_back = 's'  # крок назад
key_left = 'a'  # крок вліво (вбік від камери)
key_right = 'd'  # крок вправо
key_up = 'space'  # крок вгору
key_down = 'shift'  # крок вниз

key_turn_left = 'q'  # поворот камери праворуч (а світу - ліворуч)
key_turn_right = 'e'  # поворот камери ліворуч (а світу – праворуч)

key_build = 'mouse1'     # побудувати блок перед собою
key_destroy = 'mouse3'   # зруйнувати блок перед собою

step = 1

class Hero():
    def __init__(self, pos, land):
        """Ініціалізація героя:
        - Завантаження моделі героя.
        - Встановлення початкової позиції та кольору.
        - Прив'язка камери до героя.
        - Налаштування управління."""
        self.land = land
        self.mode = True  # режим проходження крізь усе
        self.hero = loader.loadModel('panda')
        self.hero.setColor(1, 0.3, 0.5)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.hero.setScale(0.1, 0.1, 0.1)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        """Перемикання камери в режим вільного огляду:
        - Камера від'єднується від героя."""
        x, y, z = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-x, -y, -z - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        """Зміна режиму камери:
        - Перемикання між прив'язкою до героя і вільним оглядом."""
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        """Поворот героя вліво (зміна кута погляду за годинниковою стрілкою)."""
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        """Поворот героя вправо (зміна кута погляду проти годинникової стрілки)."""
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        """Розрахунок нових координат для руху героя в заданому напрямку.
        Повертає координати (x, y, z), куди переміститься герой."""
        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()
        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        """Переміщення героя до нових координат, незалежно від перешкод."""
        x, y, z = self.look_at(angle)
        if self.mode:
            self.hero.setPos((x, y, z))
            print(f"Герой переміщений на {(x, y, z)}")
        else:
            if not self.land.isBlockAt((round(x), round(y), round(z))):
                # Якщо блоку немає, рухаємо героя
                self.hero.setPos((x, y, z))
                print(f"Герой переміщений на {(x, y, z)}")
            else:
                print(f"Неможливо рухатись, є блок на {(x, y, z)}")

    def check_dir(self, angle):
        """Визначення зміни координат (X, Y) відповідно до кута напрямку.
        Повертає дельту (dx, dy) залежно від кута."""
        if angle >= 0 and angle <= 20:
            return (0, -step)
        elif angle <= 65:
            return (step, -step)
        elif angle <= 110:
            return (step, 0)
        elif angle <= 155:
            return (step, step)
        elif angle <= 200:
            return (0, step)
        elif angle <= 245:
            return (-step, step)
        elif angle <= 290:
            return (-step, 0)
        elif angle <= 335:
            return (-step, -step)
        else:
            return (0, -step)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def forward(self):
        """Рух героя вперед у напрямку, куди він дивиться."""
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        """Рух героя назад (протилежно напрямку, куди він дивиться)."""
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        """Рух героя вліво відносно напрямку його погляду."""
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        """Рух героя вправо відносно напрямку його погляду."""
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def move_up(self):
        """Рух героя вгору по осі Z, якщо висота не перевищує обмеження."""
        if self.mode:
            x, y, z = self.hero.getPos()
            new_pos = (x, y, z + step)
            self.hero.setPos(new_pos)

    def move_down(self):
        """Рух героя вниз по осі Z, якщо він не на найнижчій точці й немає блоку знизу."""
        if self.mode:
            x, y, z = self.hero.getPos()
            new_pos = (x, y, z - step)
            self.hero.setPos(new_pos)

    def try_move(self, angle):
        '''Переміщається, якщо може'''
        pos = self.look_at(angle)
        if not self.land.isBlockAt(pos):
            # Маємо вільно. Можливо, треба впасти вниз:
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # Маємо зайнято. Якщо вийде, заберемося на цей блок:
            pos = pos[0], pos[1], pos[2] + 1
            if not self.land.isBlockAt(pos):
                self.hero.setPos(pos)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def switch_mode(self):
        if self.mode:
            self.mode = False
            print("Тепер неможна проходити крізь перешкоди")
        else:
            self.mode = True
            print("Тепер можна проходити крізь перешкоди")

    def accept_events(self):
        """Прив'язка клавіш управління до методів руху і повороту героя."""
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_down, self.move_down)
        base.accept(key_up, self.move_up)

        base.accept(key_switch_camera, self.changeView)

        base.accept(key_switch_mode, self.switch_mode)
        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept("k", self.land.saveMap)
        base.accept("l", self.land.loadMap)


