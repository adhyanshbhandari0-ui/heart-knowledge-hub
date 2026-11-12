from __future__ import print_function
import numpy as np
np.random.seed(123)
import numpy as np
np.random.seed(123)
import itertools
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import io
import numpy as np
np.random.seed(123)  # for reproducibility
from keras.layers.convolutional import Conv2D
from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import MaxPooling2D
from skimage import io
import matplotlib
matplotlib.use('Agg')
import matplotlib
matplotlib.use('Agg')
import numpy as np

def convert_spectrogram_to_numpy(path_to_spectrogram):
    img = io.imread(path_to_spectrogram)
    return img

def create_model(weights_path=None):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(3, 640, 480)))
    print("fail")
    model.add(Conv2D(64, (3, 3), activation='relu', dim_ordering="th"))
    print("fail2")

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))
    if weights_path:
        model.load_weights(weights_path)
    return model

model = create_model('/Users/sreeharirammohan/Desktop/check_point_models/weights-best-031-0.88735.hdf5')
print("Created model")

print("Finished import statements")
pickle_filepath_X = "/Users/sreeharirammohan/Desktop/all_data/allMelNumpyImages.npy"
pickle_filepath_Y = "/Users/sreeharirammohan/Desktop/all_data/allMelNumpyLabels.npy"

X = np.load(pickle_filepath_X)
Y = np.load(pickle_filepath_Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#X_train = numpy.swapaxes(X_train, 2, 3)
#X_test = numpy.swapaxes(X_test, 2, 3)
print("X_train shape: ")
print(X_train.shape)
print("-----")
print("X_test shape")
print(X_test.shape)
print("-----")
print("Y_train.shape")
print(Y_train.shape)
print("-----")
print("Y_test shape")
print(Y_test.shape)

Y_train.reshape(2592, 2)
Y_test.reshape(648, 2)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')


'''
basic example of plotting a confusion matrix is below
'''
y_pred = model.predict_classes(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix([ np.where(r==1)[0][0] for r in Y_test], y_pred)
print(cm)

'''
A more complex example of plotting a confusion matrix is below
'''
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Compute confusion matrix

###already did the below 2 lines above
#y_pred = model.predict_classes(X_test)
#cm = confusion_matrix([ np.where(r==1)[0][0] for r in Y_test], y_pred)

#set class names
class_names = ['normal', 'abnormal']

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cm, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cm, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()