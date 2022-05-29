from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam
from tensorflow import keras

def generateNetwork(
        input_shape,
        output_shape,
        loss_function,
        learning_rate):
        ''' 
        generates a neural network using keras
        based on the arguments provided by the
        constructor.
        '''
        model = Sequential()
        model.add(Dense(512, activation=relu, input_dim=input_shape))
        model.add(Dense(256, activation=relu))
        model.add(Dense(128, activation=relu))
        model.add(Dense(64, activation=relu))
        model.add(Dense(32, activation=relu))
        model.add(Dense(output_shape, activation=linear))
        model.summary()
        model.compile(loss=loss_function, optimizer=Adam(learning_rate=learning_rate))
        return model

def saveModel(model, algorithm="deep", path="lunar-lander"):
        '''
        saves a given keras model to the data path
        '''
        model.save("src/data/{1}/{0}".format(algorithm, path))

def loadModel(path="lunar-lander", algorithm="deep"):
        return keras.models.load_model("src/data/{1}/{0}".format(algorithm, path), compile=False)