# Spicy-Raman

<<<<<<< HEAD
### Background
Microplastic ingestion has been considered to be a serious detriment to marine organisms, from oysters to orca whales. The majority of these samples have been identified to be one of four categories: polyethylene, nylon, polyamides, and fluorescents. Although comprising only about 20 - 25% of the total samples, this still represents about 10+ hours of analysis per study. By categorizing and filtering out these major classes of spectra, researchers will be able to focus on identifying novel groups of microparticles.

### About project
We employed **TensorFlow (and the keras API** because we are beginners) to create a model to classify the Raman spectrum from orca whale samples. The goal of our project is to machine learn the pattern of Raman spectra by polymer categories(e.g. polyamide, polyethylene), and let it expect the type a designated material falls into.
In this specific model, 3 levels of neurons were used in order to optimize adequate complexity with ease of model creation and speed.

We **acquired Raman spectra** from Luscombe Lab. We acquired them as .txt files so that we can finally change them into image files that can be used with Tensorflow(or Keras?). We first **plotted those text data and converted them into image files**(.png).

However since the amount of data we could get was less than we expected, we talked to Jimin Qian with this issue, and we decided to do the **data augmentation**.
We first converted images into numpy array(img_to_array), expanded dimension(expand_dims), and created image data augmentation generator(ImageDataGenerator(zoom_range=[0.5,1.0])). We used os.scandir() function to iterate over data not yet augmented and got augmented data.

We then **created image databse** in order to load these image data into codes.

Those augmented data was then **separated by 50/50 into train and validation**,
They were stored in either "trainingdata_Pictures" directory or "validationdata_Pictures".

Each train and validation set were then split into 5 categories: flourescent, nylon, polyamide, polyethylene, and unknown.

![image](/mnt/c/Users/seans/Desktop/CEI_logo_tag.png)


### Use cases
Since Raman spectroscopy offers key information of substances both quantitatively and qualitatively and is non-destructive, it is heavily used by different users in industry and laboratories. Users arrange from cosmetic makers, pharmaceutical suppliers, life scientists, product manufacturers to geologists.
Specifically with our method we expect cosmetics makers can test bio-compatibilitiy, for example, before they want to launch a new product. They can machine-learn patterns of Raman spectra of substances that are already proven to be dangerous and use that pattern to predict whether or not a new substance they're trying to develop is safe to human body. Or they can choose "good" ingredients to be pattern-read and use them as a standard in developing new substances. Same mechanism can also be applied to pharmaceuticals. For product manufacturers we expect this method to be used as a tool for detecting substances, that are created during a certain manufacturing process, that causes a product failure(e.g. mechanical failure in a car chassis) by reading out chemicals inside and their Raman spectra. Likewise we hope this method can be used as an investigation tool in earth science, life science, and many more.


### Future work
As the number of identified particles increases, the hope is to increase the capability of the model in identifying an increasing category of Raman spectrum. This will enable future researchers to save more time when analyzing the Raman spectrum of orca (and other) microplastic pollution.

### Thanks and Acknowledgements
Special thanks to Dave Beck, Ting Cao and the TAs of the University of Washington Direct Program for help and guidance in learning python and machine learning.

Also many thanks to freeCodeCamp.org, for free Tensorflow tutorials.

Lastly, thank you so much to the Luscombe Lab and especially Samantha Phan for access to the raman spectrum data, sorry to increase your workflow in your already busy schedule :)

=======
