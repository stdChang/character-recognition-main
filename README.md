
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">OCR-On-The-Go AI Character Recognition App</h3>

  <p align="center">
OCR-On-The-Go Application created under the supervision of UC Davis NLP researcher Gabe Simmons for the ECS 170 course. The main goal is to allow for users to be able to upload pictures or physically draw characters to be recognized. This can go beyond and in be integrated with dictionary apps or run in greater capacities for other non-latin languages (Chinese, Arabic, etc.) and full sentences.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#the-model">The Model</a></li>
    <li><a href="#challenges">Challenges</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This is a web application that leverages machine learning methods in
order to predict handwritten text. The application itself is built
using Next.js, TypeScript, and Material UI on the frontend with Flask
on the backend. The machine learning model itself is created using
TensorFlow and Keras. This application is deployed on Vercel. The
overall goal of this application is to provide users an ease of access
to character recognition with interactive features similar to Google
Translate features. Draw your words or submit images of your own on
the go, this handy tool can be a place to quickly jot things down. 
While we trained it on English for the scope of this project, foreign 
non-Latin characters could potentially be predicted if given additional 
resources like time and comprehensive datasets of other languages. 




### Built With

* [![HTML][HTML]][HTML-url]
* [![CSS][CSS]][CSS-url]
* [![JS][JS]][JS-url]
* [![Node][Node]][Node-url]
* [![React][React.js]][React-url]

* [![Next][Next.js]][Next-url]
* [![TS][TS]][TS-url]
* [![MUI][MUI]][MUI-url]
* [![Flask][Flask]][Flask-url]
* [![Keras][Keras]][Keras-url]
* [![TensorFlow][TensorFlow]][TensorFlow-url]

## The Model (ONNX)


Our model utilizes a combination of Convolutional Neural Network (CNN)
layers and Recurrent Neural Network (RNN) layers. The purpose of the
CNN layers are to extract features of characters from the images,
while the RNN layers predict the sequences of characters since
previous characters can help predict the following characters. Our
model is then compiled using the CTC loss function and the Adam optimizer.
Initially, the scope of the project was to create an AI model trained
on the MNIST dataset to create a web application that can read and
predict a handwritten digit. However, we decided to broaden the scope
of the project to allow for handwritten words and sentences as well.
After some research, it became clear that we would be able to run a
more complex model. We ultimately decided on creating an AI model
trained on the IAM handwriting database: 
<a href="https://fki.tic.heia-fr.ch/databases/iam-handwriting-database"> IAM-Handwriting Database</a>.
For our sentence recognition model, we had both convolutional neural
network and recurrent neural network parts. The CNN component is built
using residual blocks which makes training easier. This component is
used to extract features from the input images, with each convolution
layer focusing on certain features for the model to process. The nature
of the residual blocks allows for skip connections which combine the
input with the output of the convolutional layers as the total output.
Residual blocks also help reduce the vanishing gradient problem.
The RNN component is built using bidirectional long short term memory layers.
This part is responsible for taking the output of CNN layers and processing
it to predict characters or elements in the text sequence. It is able to process
sequences of features extracted from the images in both forward and
backward directions, capturing dependencies from both directions.
Dropout regularization is applied after each layer to reduce overfitting.
It does this by randomly setting a fraction of inputs to 0 during training.
The output of the model is the predicted text sequence. For the activation function,
we used leaky relu. The difference between this and standard relu
is that instead of the output being 0 when x is negative, the
output is a small non-zero value. This helps to prevent the dying
relu problem so that neurons can still learn during backpropagation
even if the input was negative.
Our model was initially trained on 50 Epochs, but we decided to train
it again for 100 epochs to increase the accuracy of the model. The Adam
optimizer is used during training because it is the commonly used optimization
algorithm for optical character recognition tasks. It is characterized
by its adaptive learning rate mechanism that helps the algorithm converge
efficiently. The loss function is CTC (Connectionist Temporal Classification)
which has been noted to be good for sequence modeling problems such as text
and speech recognition.

## Challenges


The model sometimes had inaccuracies with predicting the letters yet
succeeding with predicting words. The model was gradually tweaked and
trained over different amounts of epochs. In addition to this, our
config files were misconfigured in some cases and we updated them
accordingly. We noticed that drawing large on canvas would net more
accurate predictions which means our canvas could be improved by normalizing
what is drawn on there. Certain letters remained elusive and easily confused
like: j, i, t, l, s, and more.
Each member had slightly different backend servers to allow 
them test locally as keeping the true server online costed money. Inconsistency
in this area was settled once more developers stuck with the Flask implementation.
While connecting our backend with frontend, we dealt with
trying to convert the image to a Blob then appended to a FormData.
After trial and error this multipart request was eventually reworked
to be a JSON request. JSONs are more familiar to handle and we
implemented straightforward methods of packaging it, either with
Base64 encoding or converting it to a dataURL. Image uploading was
also implemented in hopes to remedy the lack of precision our canvas
delivers. This gives the user free reign to submit images of
handwriting that are higher-quality or styled closer in regards to the
data set that the model learned on.
Deploying our machine learning model on AWS using SageMaker presented us 
with some initial challenges. Specifically, we encountered issues related 
to SageMaker ability to load our model. Despite our efforts to resolve the 
error by consulting AWS documentation, we were unable to achieve a successful 
deployment using SageMaker.
As a solution, we decided to take a different approach. We developed custom code to 
load our machine learning model and perform predictions on input images. To facilitate 
communication between the front-end and the back-end, we implemented a Flask application.
This application would respond to POST requests from the front-end by executing the necessary
model inference code.
To host our back-end application, we provisioned an Amazon Elastic Compute Cloud (EC2) instance. 
On this EC2 instance, we installed Gunicorn to run our back-end server efficiently. Additionally, 
we set up another EC2 instance to host our front-end. On this second EC2 instance, we installed an
Apache web server to serve the front-end user interface.
To ensure seamless user access, we established a DNS record for our website. 
This allowed users to access our application through a single, user-friendly URL. 
In summary, while our initial attempts with SageMaker encountered challenges, our alternative
approach utilizing custom code, Flask, EC2 instances, Gunicorn, Apache, and DNS configuration 
ultimately resulted in a successfully deployed and accessible machine learning application.

## References
Since none of us had significant experience with AI and machine learning before 
          taking this class, we decided to take inspiration from a tutorial we found from 
          pylessons. We learned and scaffolded code from the tutorial because we had not reached 
          the neural network section of the class by the time we started working on the project.
          <br></br> 
          The tutorial is linked here: <a href="https://pylessons.com/handwritten-sentence-recognition">https://pylessons.com/handwritten-sentence-recognition</a>
          <br></br>
          We used Next.js to streamline the environment for frontend. <a href="https://nextjs.org/docs">Next.js and Vercel</a>
          <br></br>
          Material UI library was also used in development <a href="https://mui.com/material-ui/getting-started/">Material UI</a>
          <br></br>
          For more information on the timeline and results of our development, please visit the final presentation slides <a href="https://docs.google.com/presentation/d/1WYvEOhrlwOHoHyqLw9ayek6N3k5ojSqqLdyzZN91wGM/edit?usp=sharing">here.</a>
          <br></br>
          We thank you for reading about our project.


### Contributors
  <a href="https://github.com/aosmani38"> Ali Osmani - Model, Backend, Deployment </a>

  <a href="https://github.com/takeuchi-masaki">Masaki Takeuchi - Model, Frontend</a>

  <a href="https://github.com/danderekma">Derek Ma - Frontend, Backend</a>

  <a href="https://github.com/Carsontheboss909">Carson Chiem - Frontend, Backend</a>
  
  <a href="https://github.com/stdChang">Steven Chang - Frontend, Backend, Report</a>

<br/>



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Node]: https://img.shields.io/badge/Node%20js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white
[Node-url]: https://nodejs.org/en
[HTML]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[CSS]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[JS]: https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E
[JS-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Next.js]: https://img.shields.io/badge/next%20js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[TS]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[TS-url]: https://www.typescriptlang.org/
[MUI]: https://img.shields.io/badge/Material%20UI-007FFF?style=for-the-badge&logo=mui&logoColor=white
[MUI-url]: https://mui.com/material-ui/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[Keras]: https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white
[Keras-url]: https://keras.io/
[TensorFlow]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/


