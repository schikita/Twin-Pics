class SceneManager:
    def __init__(self, screen, initial_scene):
        self.screen = screen
        self.scene = initial_scene
        self.scene.manager = self

    def change_scene(self, new_scene):
        self.scene = new_scene
        self.scene.manager = self

    def handle_events(self):
        for event in self.scene.get_events():
            if event.type == event.QUIT:
                exit()
            self.scene.handle_event(event)

    def update(self, dt):
        self.scene.update(dt)

    def draw(self, screen):
        self.scene.draw(screen)
