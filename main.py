import open3d as o3d
import cv2
import numpy as np
import argparse

import views
import calc_normal
import pre_processamento

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Nome do arquivo de nuvem de pontos")
    parser.add_argument("-o", "--output", required=True, help="Nome do arquivo do painel de saída")

    args = parser.parse_args()

    file = args.input

    # Opens point cloud and visualize it
    pcd = open_file(file)
    views.view(pcd)

    #Calls pre-processing downsample and visualizes the downsampled point cloud
    downpcd = pre_processamento.down_sampling(pcd)
    print("Quantidade de pontos após downsampling: {}".format(downpcd))
    views.view(downpcd)

    # Calculates normal for each point in point cloud and visualizes it
    calc_normal.get_normals(downpcd)
    views.view_normals(downpcd)

    # Calculates main normal using np.mean()
    normal = calc_normal.get_main_normal(downpcd)

    print("Normal mean: {}".format(normal))
    print("Center of mesh: {}".format(downpcd.get_center()))

    normal_point = tuple(map(sum, zip(downpcd.get_center(), normal)))

    views.view_main_normal(downpcd, normal_point)

    img_o3d = views.panel_view(downpcd,
                               downpcd.get_center(),
                               tuple(map(sum, zip(downpcd.get_center(), normal*12))),
                               [0, 0, 1])
    
    create_panel(img_o3d, args.output)

if __name__ == "__main__":
    main()