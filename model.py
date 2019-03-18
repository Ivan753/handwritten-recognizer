from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.models import load_model

class Model(object):

    FILE_PATH = 'model70.h5'

    def __init__(self):
        self.model = None

    def build_model(self, X_train, nb_classes=62):
        self.model = Sequential()

        self.model.add(Conv2D(64, (5, 5), padding='same', data_format='channels_last', input_shape=(50, 66, 1)))
        self.model.add(Activation('relu'))
        self.model.add(Conv2D(64, (4, 4)))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(64, (4, 4), padding='same'))
        self.model.add(Activation('relu'))
        self.model.add(Conv2D(128, (4, 4)))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(1512))
        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.25))
        self.model.add(Dense(nb_classes))
        self.model.add(Activation('softmax'))

        self.model.summary()


    def train(self, X_train, Y_train, batch_size=32, nb_epoch=10):
        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy',
                           optimizer=sgd,
                           metrics=['accuracy'])
        
        self.model.fit(X_train, Y_train,
                       batch_size=batch_size,
                       epochs=nb_epoch,
                       validation_split=0.3,
                       shuffle=True
                       )
        

    def save(self, file_path=FILE_PATH):
        print('Model Saved.')
        self.model.save(file_path)

    def load(self, file_path=FILE_PATH):
        print('Model Loaded.')
        self.model = load_model(file_path)

    def predict(self, image):
        result = self.model.predict_proba(image)
        print(result)
        result = self.model.predict_classes(image)
        print(result)
        return result[0]

    def evaluate(self, X_test, Y_test):
        score = self.model.evaluate(X_test, Y_test, verbose=0)
        print("%s: %.2f%%" % (self.model.metrics_names[1], score[1]*100))

