# NROL-76_Launch

 Data scraped from SpaceX's [NROL-76 launch YouTube video](https://youtu.be/EzQpkQ1etdA?t=707) using a convolutional neural network built x	using TensorFlow to classify digits from the individual still frames which are pre-processed using OpenCV. The altitude, velocity, and acceleration are tracked from launch to landing. During periods where the engines are not firing the vertical component of acceleration is found to be consistent with expectations due to gravity, thereby confirming that this launch did in fact occur on Earth.

# The Process

The speed and altitude digits are manually identified on the frame and cropped out.

<img src="/Images/NROL-76_Frame.jpeg" alt="drawing" class="aligncenter" width="500"/>

From here they are processed using OpenCV in Python. The image is converted to greyscale then the background is removed using thresholding. The result is taking this

<img src="/Images/NROL-76_Velocity.jpeg" alt="drawing" class="aligncenter" width="200"/>

and returning this

<img src="/Images/NROL-76_Velocity_Processed.jpeg" alt="drawing" class="aligncenter" width="200"/>

as four separate images. 

# The Classifier

A convolutional neural network was built using the Python package Keras to interface with TensorFlow. Originally it was trained on the MNIST data set of handwritten digits, however it was found that this resulted in a significant mis-classification of 1's as 7's. This is due to the tendency for a handwritten 1 to consist of only a single vertical stroke, whereas the font used by SpaceX in their video has a "hat" ontop of the 1. 

To get around this I selected 60 frames at random, extracted the 7 useful digits from each, and manually labeled them. Since there tends to be many more zeros and ones than any other digit I re-balanced the classes before passing them to the neural network for training. Considering the small dataset of labeled values, this training takes only a few seconds and leads to a classifier with a 100% accuracy on the testing data (using a train/test split of 80/20). 

The classifier then iterates through all 2300 frames of the video where the rocket is in the air (I pulled only every sixth frame from the video to reduce size). There were no obvious outliers in the resulting data, indicating a near-perfect classification of the 16,100 digits.

# The Result

The data, exactly as scraped from the video after being smooth via a Savitzky–Golay filter.

<img src="/Images/NROL-76_Telemetry_Information.jpeg" alt="drawing" width="500"/>

From this data, using a finite difference scheme to take derivatives, the individual components of the velocity and acceleration can be computed, again smoothing at every step due to the increase in noise due to the finite difference method.

<img src="/Images/NROL-76_Speed_and_Accel.jpeg" alt="drawing" width="500"/>


The red dashed line corresponds to a value of 9.8 m/s/s - the acceleration due to gravity in free-fall for an object near the Earth's surface. Clearly air resistance was not a major factor in this process as the rocket's acceleration matches nicely with the red-dashed line.





