# Spicy-Raman

### Background
Microplastic ingestion has been considered to be a serious detriment to marine organisms, from oysters to orca whales. The majority of these samples have been identified to be one of four categories: polyethylene, nylon, polyamides, and fluorescents. Although comprising only about 20 - 25% of the total samples, this still represents about 10+ hours of analysis per study. By categorizing and filtering out these major classes of spectra, researchers will be able to focus on identifying novel groups of microparticles.

### About project
This model will use TensorFlow (and the keras API because we are beginners) to create a model to classify the raman spectrum from orca whale samples. 

The accuiredraman spectrum will be imported as .txt files in order to eliminate dependence on the renishaw software, which is licensed and requires purchase. 

Because Tensorflow is known to be especially good at image processing, the text files will be graphed, then converted into .jpeg (or .png) files to be processed. 

In this specific model, 3 levels of neurons were used in order to optimize adequate complexity with ease of model creation and speed. 


### Future work
As the number of identified particles increases, the hope is to increase the capability of the model in identifying an increasing category of raman spectrum. This will enable future researchers to save more time when analyzing the raman spectrum of orca (and other) microplastic pollution.

### Thanks and Acknowledgements
Special thanks to Dave Beck, Ting Cao and the TAs of the University of Washington Direct Program for help and guidance in learning python and machine learning.

Also many thank yous to freeCodeCamp.org, for free Tensorflow tutorials.

Lastly, thank you so much to the Luscombe Lab and especially Samantha Phan for access to the raman spectrum data, sorry to increase your workflow in your already busy schedule :)

