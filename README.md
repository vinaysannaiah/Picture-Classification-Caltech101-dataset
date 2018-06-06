# Picture-Classification-Caltech101-dataset

Caltech 101 is a dataset having 101 classes of various objects. Every class has images ranging from 40 to 800, with most classes having about 50 images. The size if the images are not standard, it is roughly 300 x 200.

The images were collected in September 2003 by Fei-Fei Li, Marco Andreetto, and Marc 'Aurelio Ranzato.

#### Please download the dataset from: http://www.vision.caltech.edu/Image_Datasets/Caltech101/

This problem is solved in several ways in this repository. Before that the data must be stored in the currect working folder as,

dataset

  -->accordion

  -->airplanes etc.
  
  
### Approach 1: 
#### Features: HOG Features

#### Classification Technique : Linear SVC

#### Method: 10 fold cross validation 
i.e. the images in every class of the dataset is divided into 10 parts, in the first iteration 1st part is used for testing and the remaining 10 parts are used for training. For the second iteration 2ndpart is used for testing and the remaining parts along with the 1st part is used for training, this step goes on until 10 iterations.

Please look into the http://statweb.stanford.edu/~tibs/sta306bfiles/cvwrong.pdf for better understanding.
#### IDE used: Spyder

Here we can observe that as we make use of a single feature and as we have very few images in few of the classes we wont be able to achieve a high accuracy. we can even observe the confusion matrix which signifies how well a class is classified. The classes with more number of images is classifed better than the one in which there are few images.


### Approach 2: 
Here lets try to improve our accuracy and also let us try to validate the classification technique that best suits our problem.
uploading soon .. .. ..


