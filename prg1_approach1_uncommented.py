#Download the necessary libraries

import os, os.path
import cv2 # important : import Open CV
import numpy as np # Import numpy library 
from sklearn.model_selection import StratifiedKFold #Import stratified kfold as we are using a 10fold cross validation approach
from sklearn.svm import LinearSVC # Import the Linear SVM Classifier
from skimage.feature import hog # Import Hog model to extract features
from sklearn.metrics import confusion_matrix # Import confusion matrix to evaluate the performance

# create the necessary empty lists
imgs = []
y=[]
file_size = []
k=0
path = "/dataset" # Give the dataset path here

folder = os.listdir(path) # from the given path get the file names such as accordion, airplanes etc..
for file in folder: # for every file name in the given path go inseide that directory and get the images
    subpath = os.path.join(path,file)  # Join the name of these files to the previous path 
    
    files = os.listdir(subpath) # Take these image names to a list called files
    j=0
    for i in range(np.size(files)): # now we shall loop through these number of files
        
        im=cv2.imread(subpath+'/'+files[0+j]) # Read the images from this subpath
        
        imgs.append(im) # append all the read images to a list called imgs
        y.append(k) # generate a labe to every file and append it to y

        j+=1
        if (j == (np.size(files))):
            file_size.append(j)
   
    k+=1
     
y=np.array(y).tolist()

ix=[]
for index, item in enumerate(imgs):
    if (np.size(item) == 1):
        ix.append(index)
        del imgs[index]
        
for index, item in enumerate(y):
    for v in range(np.size(ix)):
        if (index == ix[v]):
            del y[index]
        
y=np.array(y).astype(np.float64) 

# Function to convert an image from color to grayscale
def rgb2gray(rgb):
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    return gray

def resize_(image):
    u=cv2.resize(image,(256,256))
    return u

def fd_hog(image):
    fd, hog_image = hog(image, orientations=8, pixels_per_cell=(64, 64),
                    cells_per_block=(1, 1), visualise=True)
    
    return fd

a=[]

for img in imgs:
    
    b=resize_(img)
    c=rgb2gray(b)   
    d=fd_hog(c)
    a.append(d)

a=np.array(a)

score = []
skf = StratifiedKFold(n_splits = 10) # divide the complete dataset in to 10 folds
skf.get_n_splits(a, y)

accuracy = 0

for train_index, test_index in skf.split(a,y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = a[train_index], a[test_index]
    y_train, y_test = y[train_index], y[test_index] 


    clf = LinearSVC(random_state=0)
    
    clf.fit(X_train, y_train)
        
    y_pred = clf.predict(X_test)
    
    scr = clf.score(X_test, y_test)
    print(scr)
    score.append(scr)
    accuracy += scr
    cnf_matrix = confusion_matrix(y_test, y_pred)
    print(cnf_matrix)

score = np.array(score)

fin_accuracy = (accuracy/10)*100

print("Final Accuracy is: {}".format(fin_accuracy))
    
