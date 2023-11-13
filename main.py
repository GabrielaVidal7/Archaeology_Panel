import open3d as o3d
import cv2
import numpy as np
import argparse

import views
import calc_normal
import pre_processamento
import manage_files

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Nome do arquivo de nuvem de pontos")
    parser.add_argument("-o", "--output", required=True, help="Nome do arquivo do painel de saída")
    parser.add_argument("-z", "--zoom_out", required=True, help="Valor multiplicativo do vetor normal para dar zoom out no painel")

    args = parser.parse_args()

    file = args.input
    zoom_out = int(args.zoom_out)

    # Opens point cloud and visualize it
    pcd = manage_files.open_file(file)
    views.view(pcd)

    #Calls pre-processing downsample and visualizes the downsampled point cloud
    downpcd = pre_processamento.down_sampling(pcd)
    # print("Quantidade de pontos após downsampling: {}".format(downpcd))
    views.view(downpcd)

    # Calculates normal for each point in point cloud and visualizes it
    calc_normal.get_normals(downpcd)
    views.view_normals(downpcd)

    downpcd = calc_normal.normalize_normals(downpcd)
    views.view_normals(downpcd)

    # Calculates main normal using np.mean()
    normal = calc_normal.get_main_normal(downpcd)

    # print("Normal mean: {}".format(normal))
    # print("Center of mesh: {}".format(downpcd.get_center()))

    normal_point = tuple(map(sum, zip(downpcd.get_center(), normal)))

    views.view_main_normal(downpcd, normal_point)

    img_o3d = views.panel_view(downpcd,
                               downpcd.get_center(),
                               tuple(map(sum, zip(downpcd.get_center(), normal*zoom_out))),
                               [0, 0, 1])
    
    manage_files.create_panel(img_o3d, args.output)

if __name__ == "__main__":
    main()