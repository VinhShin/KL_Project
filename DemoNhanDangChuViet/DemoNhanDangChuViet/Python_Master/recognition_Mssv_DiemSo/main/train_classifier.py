from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np

dataset = datasets.fetch_mldata("MNIST Original")

imagini = np.array(dataset.data, 'int16')
etichete = np.array(dataset.target, 'int')

print '=> Creare lista de trasaturi din fiecare imagine...'
list_hog_fd = []
for imagine in imagini:
    fd = hog(imagine.reshape(28, 28), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    list_hog_fd.append(fd)

computed_features = np.array(list_hog_fd, 'float64')
clf = LinearSVC()

print '=> Antrenare clasificator...'
clf.fit(computed_features, etichete)
joblib.dump(clf, "./model/digits_clf.pkl", compress=3)

print '=> Am terminat!'