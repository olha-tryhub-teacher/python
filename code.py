    def animate(self):
        self.img_number += self.anim_speed
        if self.img_number >= len(self.imgs):
            self.img_number = 0
        self.img = self.imgs[int(self.img_number)]
