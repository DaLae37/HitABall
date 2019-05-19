class Scene() :
    def update(self) :
        pass
    def load_resources(self) :
        pass
    def ui_event(self) :
        pass

class SceneManager(Scene) :
    instance = None

    def __init__(self) :
        self.isQuit = False

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = SceneManager()
        return cls.instance

    def changeScene(self, replaced_scene) :
        self.current_scene = replaced_scene

    def update(self) :
        self.current_scene.update()

    def setQuit(self, isQuit) :
        self.isQuit = isQuit
