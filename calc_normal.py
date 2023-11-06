import open3d as o3d
import numpy as np

def get_normals(pcd):
    '''
        Function that calculate the normal of each point in pcd
    '''
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    return

def get_main_normal(pcd):
    '''
        Function that calculates the main normal by using np.mean()
    '''
    return np.mean(np.asarray(pcd.normals), axis=0)