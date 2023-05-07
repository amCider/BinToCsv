#import cv2
#import numpy as np

#from PIL import Image
import cv2
import numpy as np
import numpy as npdeci
from decimal import Decimal


##下に行くほど黒くなっていく画像
#width   = 176
#height  = 120
#img     = np.zeros((height, width, 3), np.uint8)
#bin     = np.zeros((height, width), np.uint8)
#for h in range(0, height):
#    color = int(255 * (height - h) / height)
#    bin[h,:] = color
#    img[h,:] [color, color, color]
#cv2.imwrite('img.png', img)
#binF = open('A.bin', 'wb')
#binF.write(bin)
#binF.close()
#
##右に行くほど黒くなっていく画像
#width   = 120
#height  = 80
#img2    = np.zeros((height, width, 3), np.uint16)
#bin2    = np.zeros((height, width), np.uint16)
#for w in range(0, width):
#    color = int(65534 * (width - w) / width)
#    bin2[:,w] = color
#    img2[:, w] = [color, color, color]
#cv2.imwrite('img2.png', img2)<
#bin2F = open('B.bin', 'wb')
#bin2F.write(bin2)
#bin2F.close()


def CreateImageSIchi ( overall_width, overall_height, bit_select, output_name):
    binHoge = 0
    if bit_select == "U32":
        binHoge = np.zeros((overall_height, overall_width), np.uint32)
    if bit_select == "U16":
        binHoge = np.zeros((overall_height, overall_width), np.uint16)
    if bit_select == "U16Deci":
        binHoge = np.zeros((overall_height, overall_width), np.int16)
    if bit_select == "U8":
        binHoge = np.zeros((overall_height, overall_width), np.uint8)
    
    for h in range(0, overall_height):  # 行を置き換える
        for w in range(0, overall_width):
            if((h + w) % 2) == 0:
                binHoge[ h, w] = 127#32767
            else:
                binHoge[ h, w] = 5#-32768
    binHogeF = open(output_name + ".bin", 'wb')
    binHogeF.write(binHoge)
    binHogeF.close()

if __name__ == "__main__":
    CreateImageSIchi ( 24, 24, "U8", "imgB")

