class Model:

    def __init__(self):
        self.built = False
        self.loaded = False
        self.build()
        self.load()

    def build(self):
        # once built, make self.built = True
        pass

    def load(self):
        # if not self.built:
        #     raise RuntimeError("Model is not built.")
        pass

    def predict(self, input_X):
        # if not self.built:
        #     raise RuntimeError("Model is not built.")
        # if not self.loaded:
        #     raise RuntimeError("Model is not loaded.")
        # self.model.predict(input_X)
        pass
