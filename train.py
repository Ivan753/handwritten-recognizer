import numpy as np
from model import Model
from utils import get_samples


if __name__ == '__main__':
    
    X_train, X_test, Y_train, Y_test = get_samples()
    
    X_train = np.array(X_train)
    Y_train = np.array(Y_train)
    X_test = np.array(X_test)
    Y_test = np.array(Y_test)
    
    model = Model()
    model.build_model(X_train)
    model.train(X_train, Y_train, nb_epoch=15)
    model.save()

    model = Model()
    model.load()
    model.evaluate(X_test, Y_test)