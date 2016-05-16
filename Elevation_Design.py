import os
import numpy as np
from scipy import misc

def image_range_convert(image, Max, Min)
	image = (Max - Min)/(image.max() - imag.min()) * (image - image.min()) + Min
	return image

def reshape_image(imag, column, row):
	im = np.matrix(np.zeros(column * row).reshape((column, row)))
	imc = imag.shape[0]
	imr = imag.shape[1]
	for c in range(column):
		for r in range(row):
			im[c,r] = image[row*c + r:row*c + row, row*c + r:row*c + row].max()
	return im

def convert_density(imag, Range):

	return imagdensity

def digital_image(SunShine, WindPressure, column, row):
	sunshine = misc.imread(SunShine,mode = 'L')
	windpressure = misc.imread(WindPressure,mode = 'L')
	ss = reshape_image(sunshine, column, row)
	wp = reshape_image(windpressure, column, row)
	ssdensity = convert_density(ss, ssRange)
	wpdensity = convert_density(wp, wpRange)		
	return ssdensity, wpdensity

def selection(x, y, Cforbidden, Bforbidden):
	b = 1
	c = 1
	if (y in Cforbidden) | (selection(x, y - 1, sunshine, windpressure)[2] == 1):
		c = 0
	if (y in Bforbidden) | (selection(x, y - 1, sunshine, windpressure)[1] == 1):
		b = 0	
	return b, c
	
def ImageSize(column, row, roomrow, roomcolumn):
	Imagecolumn = column / roomcolumn
	Imagerow = row / roomcolumn
	return Imagecolumn, Imagerow

def designElevation(column, row, ssd, wpd, rcolumn, rrow, selection, icolumn):
	imageextract = selection[rrow*column + row:rrow*column + row, rrow*column + row:rrow*column + rrow,:]
	designElevation = np.matrix(np.zeros(rcolumn * rrow).reshape((rcolumn, rrow)))
	designElevation = [rrow*column + row:rrow*column + row, rrow*column + row:rrow*column + rrow] = imageextract[:,:,]
	Bdensity = designElevation[:, :, 1].sum()
	Cdensity = designElevation[:, :, 2].sum()

Column = 28
Row = 14
RoomRow = 2
RoomColumn = 4
Imagecolumn, Imagerow = ImageSize(Column, Row, RoomRow, RoomColumn)
SunShineDensity, WindPressureDensity = digital_image(dirsun, dirwind, Imagecolumn, Imagerow)
Selection = np.zeros((Column, Row, 3))
Cforbidden = [1, 4, 7]
Bforbidden = [2, 4, 7]
for c in range(Column):
	for r in range(1, Row):
		Selection[c,r,0] = 1
		Selection[c,r,1:3] = selection(c, r, Cforbidden, Bforbidden)

ElevationDesign = np.matrix(np.zeros(Column * Row).reshape((Column, Row)))
for ic in range(Imagecolumn):
	for ir in range(Imagerow):
		ElevationDesign[RoomRow*ic:RoomRow*(ic + 1), RoomColumn*ic:RoomColumn*(ic + 1)] = designElevation(ic, ir, SunShineDensity, WindPressureDensity, RoomColumn, RoomColumn, Selection, Imagecolumn)
