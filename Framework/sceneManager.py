class Scene() :
    def update(self) :
        pass

class SceneManager(Scene) :
    _instance = None

    @classmethod
    def getInstance(cls) :
        if cls._instance is None :
            cls._instance = SceneManager()
        return cls._instance

    def changeScene(self, _scene) :
        self._scene = _scene

    def update(self) :
        self._scene.update()
