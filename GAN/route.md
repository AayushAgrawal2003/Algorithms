## What is a GAN 
Generative adversarial networks
### Elements of a GAN
- Generator Model: Used to generate images
- Discriminator Model: Used to classify images into real and fake

![](https://editor.analyticsvidhya.com/uploads/68909architecture.PNG)

- The Geeretor model takes an input vector z as an input and generates the images G(z)
- These images then get sent to the Discriminator Model to be classifed fake or real  
- Then we measure the loss and this loss is backpropogated through the network to update the weights 
- When we are training the Discriminator, we have to freeze the Generator and back propagate errors to only update the Discriminator.
-  Both models are improved after each epoch. To stop training we use a concept called Nash Equillibrium, When we can say all generated images look simmilar to the orignal.

#### Introducings constants to understand loss


