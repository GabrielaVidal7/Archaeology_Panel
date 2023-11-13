import open3d as o3d
import cv2
import numpy as np

def open_file(path):
    '''
        Function that opens point cloud file
    '''

    print("Load a ply point cloud")
    pointCloud = o3d.io.read_point_cloud(path)

    print("Quantidade de pontos pré downsampling: {}".format(pointCloud))
    
    return pointCloud

def create_panel(img_o3d, file_name):
    '''
        Function that creates image file based on scene renderer
    '''

    img_cv2 = cv2.cvtColor(np.array(img_o3d), cv2.COLOR_RGBA2BGRA)
    cv2.imshow("Preview window", img_cv2)
    cv2.waitKey()
    file_name = file_name+".png"
    o3d.io.write_image(file_name, img_o3d, 9)