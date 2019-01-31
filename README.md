# audio-mnist-with-person-detection
### MNIST audio classification project is able to recognise the person speaking along with the digit spoken! 
- Data set referred: https://github.com/Jakobovski/free-spoken-digit-dataset/tree/master/recordings

### Code Description:

`data_accumulator.ipynb`: This jupyter notebook is responsible for the processing the .wav files located in the directory recordings/. Files are named in the following format: {digitLabel}_{speakerName}_{index}.wav Example: 7_jackson_32.wav. The project uses librosa to extract MFCC features from a audio clip which are then fed into deep CNN for classification and recognition of the person.

`train.ipynb`: This jupyter notebook stratigically split the whole dataset from data_accumulator.ipynb into training and testing set. It uses a relatively shallow CNN architecture written with Keras on top of Tensorflow to classify not only the digits spoken correctly but also recognize the person speaking the digit at the same time! Achieved accuracy of 96.25% on the unseen testing data.

### Goal:
Goal of the project was to play around with librosa and audio features extraction in general :)    

