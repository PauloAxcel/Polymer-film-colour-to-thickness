# -*- coding: utf--8 -*-
"""
Created on Sun Sep 16 00:58:29 2018

@author: user
"""

from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
Polynomial = np.polynomial.Polynomial

#Import image and display it in an array. This array is built based on the pixels of the image.
#Pixel(0,0),Pixel(1,0)...Pixel(n,0)
#Pixel(0,1)...
#...
#Pixel(0,n)...          Pixel(n,n)
#Each pixel is composed of an array with 3 values correspoding to the each RGB value.

im = Image.open('C:\\Users\\user\\Documents\\birmingham\\MT_Measurement techniques\O_EHD\\experimental work\Patterns\\PG_EHD_05_20_18\\PG_EHD_1\\PG_EHD1.png')
imarray = np.array(im)

#Import also the reference image, the image that is known and that we can make the conversion between pixels and film thickness
ref = Image.open('C:\\Users\\user\\Documents\\birmingham\\MT_Measurement techniques\O_EHD\\calibration.png')
refarray = np.array(ref)

#open empty vectors to fill in with known tickness points and colours.
#This information can be obtained in "E Schaffer. Instabilities in thin polymer films: structure formation
#and pattern transfer. PhD Thesis, http://www.ub.unikonstanz.
#de/kops/volltexte/2002/779/, 2001." On fig 3.2 we have 20 nm (light brown), 70 nm (dark brown), 100 nm (dark blue), 140 nm (light blue) 200 nm (yellow), 250–280 nm (purple), 290 nm (blue),
#310 nm (turquoise), 330 nm (green), 350 nm (yellow), 400 nm (light purple), 420 nm (green), 460 nm (yellow), 520 nm (pink) . . . alternating light green and pink up to approximately
#1.5 µm until it changes to a transparent gray

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]


#plot the reference image

fig, ax = plt.subplots()
ax.imshow(ref, extent=[0,1066, 0, 101])

#In this part I opened the reference image in the following website https://imagecolorpicker.com and pickes spots where I have the reference value
#The spots are given in RGB code in order for python to identify these points in the image
#After finding the correspondent RGB point, we plot the point and the ref image all together.

for i in range(0,101):
    for j in range(0,1066):
        #LIGHT BROWN
        if np.array_equal(refarray[i,j], [154 , 86 , 15]):
            a = np.append([i,j],20)
            ax.plot(a[1] , a[0], "x")   
        #DARK BROWN    
        if np.array_equal(refarray[i,j],[ 98 , 58 , 48]):
            b = np.append([i,j],70)   
            ax.plot(b[1] , b[0], "x")  
        #DARK BLUE    
        if np.array_equal(refarray[i,j],[43 , 76 , 107]):
            c = np.append([i,j],100) 
            ax.plot(c[1] , c[0], "x")  
        #LIGHT BLUE
        if np.array_equal(refarray[i,j],[47,117,143]):
            d = np.append([i,j],140)
            ax.plot(d[1] , d[0], "x")
        #YELLOW
        if np.array_equal(refarray[i,j],[253 , 231 , 119]):
            e = np.append([i,j],200)
            ax.plot(e[1] , e[0], "x")
        #PURPLE
        if np.array_equal(refarray[i,j],[176,76,130]):
            f = np.append([i,j],250)
            ax.plot(f[1] , f[0], "x")
        #BLUE
        if np.array_equal(refarray[i,j],[78 , 166 , 176]):
            p = np.append([i,j],270)
            ax.plot(p[1] , p[0], "x")
        #TURQUOISE    
        if np.array_equal(refarray[i,j],[88, 207,175]):
            g = np.append([i,j],310) 
            ax.plot(g[1] , g[0], "x")
        #GREEN
        if np.array_equal(refarray[i,j],[168 , 243 , 140]):
            h = np.append([i,j],330)
            ax.plot(h[1] , h[0], "x")
        #YELLOW2
        if np.array_equal(refarray[i,j],[244 , 247 , 94]):
            k = np.append([i,j],350)
            ax.plot(k[1] , k[0], "x")
        #LIGHT PURPLE   
        if np.array_equal(refarray[i,j],[ 252,130,145]):
            l = np.append([i,j],400)
            ax.plot(l[1] , l[0], "x")
        #GREEN2    
        if np.array_equal(refarray[i,j],[158 , 223 , 123]):
            m = np.append([i,j],420)
            ax.plot(m[1] , m[0], "x")
        #YELLOW3
        if np.array_equal(refarray[i,j],[228 , 207 , 128]):
            n = np.append([i,j],460) 
            ax.plot(n[1] , n[0], "x")
        #PINK    
        if np.array_equal(refarray[i,j],[247, 174, 133]):
            o = np.append([i,j],520)
            ax.plot(o[1] , o[0], "x")
            
#since the ref image increases the film thickness from left to right a good way to represent the data is by ploting the thickness with respect to the x-axis pixesl

fig2, ax2 = plt.subplots() 
x=[a[1],b[1],c[1],d[1],e[1],f[1],p[1],g[1],h[1],k[1],l[1],m[1],n[1],o[1]]
x=[float(i) for i in x]
y=[a[2],b[2],c[2],d[2],e[2],f[2],p[2],g[2],h[2],k[2],l[2],m[2],n[2],o[2]]        
y=[float(i) for i in y]

#We fit the data with a linear fit y=ax+b -> thickness = a * pixel_x + b

z = np.polyfit(x, y, 1)
zf = np.poly1d(z)
plt.plot(x,y,'o')
plt.plot(x,zf(x))
plt.xlabel('pixel in x')
plt.ylabel('height(nm)')
slope, intercept, r_value, p_value, std_err = sp.stats.linregress(x, y)

plt.show()  
