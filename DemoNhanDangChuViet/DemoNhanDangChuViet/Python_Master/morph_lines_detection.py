"""
@file morph_lines_detection.py
@brief Use morphology transformations for extracting horizontal and vertical lines sample code
"""
import numpy as np
import sys
import cv2 as cv


def show_wait_destroy(winname, img):
    #cv.imshow(winname, img)
    #cv.moveWindow(winname, 500, 0)
    #cv.waitKey(0)
    #cv.destroyWindow(winname)
    print "........"

def main(argv):
    # [load_image]
    # Check number of arguments
    '''
    if len(argv) < 1:
        print ('Not enough parameters')
        print ('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
    '''
    # Load the image

    src = cv.imread("bangdiem_reshape.png", cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image: ' + argv[0])
        return -1

    # Show source image
    # [load_image]

    # [gray]
    # Transform source image to gray if it is not already
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src

    # Show gray image
    show_wait_destroy("gray", gray)
    # [gray]

    # [bin]
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    gray = cv.bitwise_not(gray)

    show_wait_destroy("gray", gray)

    
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                               cv.THRESH_BINARY, 15, -2)

                              
    # Show binary image
    show_wait_destroy("binary", bw)
    # [bin]

    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    # [init]

    # [horiz]
    # Specify size on horizontal axis
    # lay chieu dai => chi nhan cac doi tuong co chieu dai > heigh/10
    cols = horizontal.shape[1]
    horizontal_size = cols / 10
    # Create structure element for extracting horizontal lines through morphology operations
    #lay mat na quet
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
    # Apply morphology operations
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)

    # Show extracted horizontal lines
    show_wait_destroy("horizontal", horizontal)
    # [horiz]

    # [vert]
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows / 10

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)

    # Show extracted vertical lines
    show_wait_destroy("vertical", vertical)
    # [vert]

    # [smooth]
    # Inverse vertical image
    vertical = cv.bitwise_not(vertical)
    show_wait_destroy("vertical_bit", vertical)
    #shin add
    horizontal = cv.bitwise_not(horizontal)
    show_wait_destroy("horizontal_bit", horizontal)
    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''
    # trich chon vertical

    # Step 1
    edges_v = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges_v", edges_v)
    
    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges_v = cv.dilate(edges_v, kernel)
   
    show_wait_destroy("dilate_v", edges_v)
    # Step 3
    smooth_v = np.copy(vertical)
    
    # Step 4
    smooth_v = cv.blur(smooth_v, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges_v != 0)
    vertical[rows, cols] = smooth_v[rows, cols]
    # Show final result
    show_wait_destroy("smooth - final", vertical)
    # trich chon horizontal
    
    # Step 1
    edges_h = cv.adaptiveThreshold(horizontal, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges_h", edges_h)
    
    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges_h = cv.dilate(edges_h, kernel)
   
    show_wait_destroy("dilate_h", edges_h)
    # Step 3
    smooth_h = np.copy(horizontal)
    
    # Step 4
    smooth_h = cv.blur(smooth_h, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges_h != 0)
    horizontal[rows, cols] = smooth_h[rows, cols]

    
    # Show final result

    #bien doi vertical de add vao bang horizontal
    
    # Step 1
    #edges_v = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                            cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("ye ye ye", vertical)
    ret2,edges_v = cv.threshold(vertical,255,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    # Step 2
    #kernel = np.ones((2, 2), np.uint8)
    #edges_v = cv.dilate(edges_v, kernel)
        
    show_wait_destroy("ye ye ye", edges_v)
    # [smooth]

    #gop vertical va horizontal
    (rows, cols) = np.where(edges_v != 0)
    horizontal[rows, cols] = smooth_v[rows, cols]

    show_wait_destroy("last - final", horizontal)

    cv.imwrite("bangdiem_morph_line.png",horizontal)
    
    return 0

   
if __name__ == "__main__":
    main(sys.argv[1:])
