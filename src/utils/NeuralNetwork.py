from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam

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
        model.add(Dense(output_shape, activation=linear))
        model.summary()
        model.compile(loss=loss_function, optimizer=Adam(learning_rate=learning_rate))
        return model