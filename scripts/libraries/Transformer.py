import os
import random
from PIL import Image, ImageFilter
class Transformer:
  def zoom(image):

    width, height = image.size

    # Zoom factor random
    zoom = random.uniform(1.3, 1.6)
    zoomedWidth = int(width / zoom)
    zoomedHeight = int(height / zoom)

    # Random position
    x = random.randint(0, width - zoomedWidth)
    y = random.randint(0, height - zoomedHeight)

    # Crop and resize
    zoomedImg = image.crop((x, y, x+zoomedWidth, y+zoomedHeight))
    zoomedImg = zoomedImg.resize((width, height))

    # Save the resulting image
    return zoomedImg
  
  def downscale(image):
    width, height = image.size

    factor = random.uniform(0.05, 0.15)
    new_width = int(width * factor)
    new_height = int(height * factor)
    downscaledImage = image.resize((new_width, new_height))
    reUpscaledImage = downscaledImage.resize((width, height))

    #zoom in the image to have the same size as the original image

    return reUpscaledImage
  
  def horflip(image):
    newImage = image.transpose(Image.FLIP_LEFT_RIGHT)
    return newImage
  
  def verflip(image):
    newImage = image.transpose(Image.FLIP_TOP_BOTTOM)
    return newImage

  def gNoise(image):
    copy = image.copy()
    # Apply noise to the image
    pixels = copy.load()
    width, height = copy.size
    for x in range(width):
      for y in range(height):
        r, g, b = pixels[x, y]
        noise = random.randint(-50, 50)
        r += noise
        g += noise
        b += noise
        pixels[x, y] = (r, g, b)
    
    # Return the noisy image
    return copy
  
  def gBlur(image):
    newImage = image.filter(ImageFilter.GaussianBlur(radius=(random.randint(1, 3))))
    return newImage

  def combined(originalImage, imgName):
    imgArr = []
    for it in range(10):
      image = originalImage
      fncArr = [Transformer.zoom, Transformer.downscale, Transformer.horflip, Transformer.verflip, Transformer.gNoise, Transformer.gBlur]
      fncNum = random.randint(0, 5)
      image = fncArr[fncNum](image)
      op = fncArr[fncNum].__name__[0].upper() + fncArr[fncNum].__name__[1].lower()
      fncArr.pop(fncNum)
      for fnc in fncArr:
        if random.uniform(0,1) <= 0.3:
          image = fnc(image)
          op += fnc.__name__[0].upper() + fnc.__name__[1].lower()

      newName = str(it) + op + "_"+ imgName
      imgArr.append((image, newName))
    return imgArr

