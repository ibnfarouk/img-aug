import imageio
import imgaug.augmenters as iaa
import ipyplot

input_img = imageio.v3.imread('images/bird.jpg')

#Horizontal Flip
hflip= iaa.Fliplr(p=1.0)
input_hf= hflip.augment_image(input_img)

#Vertical Flip
vflip= iaa.Flipud(p=1.0)
input_vf= vflip.augment_image(input_img)
images_list=[input_img, input_hf, input_vf]
labels = ['Original', 'Horizontally flipped', 'Vertically flipped']
ipyplot.plot_images(images_list,labels=labels,img_width=180)