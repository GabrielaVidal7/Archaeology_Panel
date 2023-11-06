import open3d as o3d

def view(pcd):
    '''
        Function that draws point cloud
    '''
    o3d.visualization.draw_geometries([pcd])
    return

def view_normals(pcd):
    '''
        Function that draws point cloud and show all normals
    '''
    o3d.visualization.draw_geometries([pcd], point_show_normal=True)
    return

def view_main_normal(pcd, normal):
    '''
        Function that draws the point cloud and a point representing the main normal
    '''
    normal = [normal]
    pointSet = o3d.geometry.PointCloud()
    pointSet.points = o3d.utility.Vector3dVector(normal)

    o3d.visualization.draw_geometries([pcd, pointSet])
    return

def panel_view(pcd, look, position, orientation):
    '''
        Function that creates a rendering scene, positions the camera and sets point cloud material
    '''
    render = o3d.visualization.rendering.OffscreenRenderer(1024, 768, headless=False)

    material = o3d.visualization.rendering.MaterialRecord()
    material.shader = "defaultUnlit"
        
    render.scene.add_geometry("modelo", pcd, material)
    render.scene.show_axes(False)

    '''
        render.scene.camera.look_at(look, position, orientation)
            look = where to look (xyz)
            position = position of the camera far enough to see the object (xyz)
            orientation = camera orientation (xyz)
    '''
    render.scene.camera.look_at(look, position, orientation)

    return render.render_to_image()
