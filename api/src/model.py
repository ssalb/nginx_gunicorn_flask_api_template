# from keras.models import Model
#from keras.layers import Input, ...

class PreTrainedModel:

    def __init__(self):
        self.built = False
        self.loaded = False
        self.model = None
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
        # preds = self.model.predict(input_X)
        #return preds
        pass
