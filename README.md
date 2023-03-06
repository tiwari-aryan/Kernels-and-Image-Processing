# Kernels, Convolutions, and Image Processing

## Overview

Convolutions are an important part of image processing, that allow computers to alter, identify, and detect various patterns in images.
## Implementation

Convolutions are implemented by passing an image kernel over an image. A kernel is generally a matrix with a series of values, for example:

    0.0625 0.125 0.0625
    0.125  0.25  0.125
    0.0625 0.125 0.0625

The above is an example of a kernel that when passed over an image, makes the image blurry.

### *How does it work?*

Given an `nxn` kernel, as the `nxn` matrix is passed over the image, each individual pixel is assigned a value equivalent to the sum of the element-wise product of the `nxn` matrix of its adjacent neighbouring values and the kernel matrix itself.

For example, given the sample grayscale image below:

![image](example_image.jpg)

The pixel shown has a grayscale value of 40. The values of the neighbouring pixels are shown below.

    51 57 63
    39 40 41
    63 58 54

After passing a blur kernel over the pixel, the resulting value can be determined by the calculation shown below:

``` (51 * 0.0625) + (57 * 0.125) + (63 * 0.0625) + (39 * 0.125) + (40 * 0.25) + (41 * 0.125) + (63 * 0.0625) + (58 * 0.125) + (54 * 0.125) = 52.1875 ```

which would be rounded to 52.

After passing this kernel over every pixel in the image (ignoring border pixels), the resulting image is the following:

![image](resulting_image.jpg)

As you can see, there is a noticeable blurring effect.

## Determining Kernel Values

Some kernel values in the examples shown are quite intuitive. Let's take the blur kernel as an example:

    0.0625 0.125 0.0625
    0.125  0.25  0.125
    0.0625 0.125 0.0625

Each pixel is influenced slightly by all pixels that are diagonal to itself, while being influenced slightly more by directly adjacent pixels. The sum of all values in this kernel is equal to 1, an important detail, as it ensures the resulting pixel value is always within the range 0-255.

This is true for all kernels in fact, and can be seen in the other examples as well.

## How to Use The Program

``` python main.py sample_image.jpg ```

You can replace `sample_image.jpg` with your desired file.