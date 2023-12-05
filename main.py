import argparse

import views
import calc_normal
import pre_processamento
import manage_files

import time

def main():
    inicio = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Nome do arquivo de nuvem de pontos")
    parser.add_argument("-o", "--output", required=True, help="Nome do arquivo do painel de saída")
    parser.add_argument("-z", "--zoom_out", required=True, help="Valor multiplicativo do vetor normal para dar zoom out no painel")

    args = parser.parse_args()

    file = args.input
    zoom_out = int(args.zoom_out)

    # Opens point cloud and visualize it
    pcd = manage_files.open_file(file)

    # Calculates the time spent on this part of the code
    fim = time.time()
    t_total = fim-inicio
    print("Tempo de processamento: {}".format(t_total))

    views.view(pcd)

    inicio = time.time()

    #Calls pre-processing downsample and visualizes the downsampled point cloud
    downpcd = pre_processamento.down_sampling(pcd)

    # Calculates the time spent on this part of the code
    fim = time.time()
    print("Tempo de downsampling: {}".format(fim-inicio))
    t_total = t_total + fim - inicio

    # print("Quantidade de pontos após downsampling: {}".format(downpcd))
    views.view(downpcd)

    inicio = time.time()

    # Calculates normal for each point in point cloud and visualizes it
    calc_normal.get_normals(downpcd)

    # Calculates the time spent on this part of the code
    fim = time.time()
    print("Tempo de calculo das normais: {}".format(fim-inicio))
    t_total = t_total + fim - inicio

    views.view_normals(downpcd)

    inicio = time.time()

    downpcd = calc_normal.normalize_normals(downpcd)

    # Calculates the time spent on this part of the code
    fim = time.time()
    print("Tempo de normalização das normais: {}".format(fim-inicio))
    t_total = t_total + fim - inicio

    views.view_normals(downpcd)

    inicio = time.time()

    # Calculates main normal using np.mean()
    normal = calc_normal.get_main_normal(downpcd)

    # print("Normal mean: {}".format(normal))
    # print("Center of mesh: {}".format(downpcd.get_center()))

    normal_point = tuple(map(sum, zip(downpcd.get_center(), normal)))

    # Calculates the time spent on this part of the code
    fim = time.time()
    print("Tempo de cálculo da normal principal: {}".format(fim-inicio))
    t_total = t_total + fim - inicio

    views.view_main_normal(downpcd, normal_point)

    img_o3d = views.panel_view(downpcd,
                               downpcd.get_center(),
                               tuple(map(sum, zip(downpcd.get_center(), normal*zoom_out))),
                               [0, 0, 1])
    
    manage_files.create_panel(img_o3d, args.output)

    print("Tempo total de processamento do código: {}".format(t_total))

if __name__ == "__main__":
    main()