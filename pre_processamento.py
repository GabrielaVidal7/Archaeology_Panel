def down_sampling(pcd):
    '''
        Function that reduces point clouds amount of points
    '''    
    return pcd.voxel_down_sample(voxel_size=0.01)