from math import pi
import math
import torch as t
def get_intersection_point_2cameras(screen1_x,screen1_y, 
                           screen2_x, screen2_y, scres_x, scres_y, 
                           focal, m_width, m_height, cam1_x, cam1_y, cam1_z, cam1_az,
                           cam2_x, cam2_y, cam2_z, cam2_az):
    


    screen_center_x = scres_x/2
    screen_center_y = scres_y/2

    camera_angle_x = ((pi/2)-math.atan(focal/(m_width/2)))*2
    camera_angle_y = ((pi/2)-math.atan(focal/(m_height/2)))*2

    angle_per_pixel_x = camera_angle_x/scres_x
    angle_per_pixel_y = camera_angle_y/scres_y
 # ------------------------------
    screen1_x = screen1_x-screen_center_x
    screen1_y = screen_center_y-screen1_y

    pitch1 = screen1_x*angle_per_pixel_x
    yaw1 = screen1_y*angle_per_pixel_y

    screen2_x = screen2_x-screen_center_x
    screen2_y = screen_center_y-screen2_y

    pitch2 = screen2_x*angle_per_pixel_x
    yaw2 = screen2_y*angle_per_pixel_y
# -----------------
    step_l = 1
    step_n = 400


    ray1_x0 = cam1_x
    ray1_y0 = cam1_y
    ray1_z0 = cam1_z
    ray1_az = cam1_az+yaw1
    ray1_pitch = pitch1

    ray2_x0 = cam2_x
    ray2_y0 = cam2_y
    ray2_z0 = cam2_z

    ray2_az = cam2_az+yaw2
    ray2_pitch = pitch2
    # ------------------

    ray1_x_increment = math.cos(ray1_az)*step_l
    ray1_y_increment = math.sin(ray1_az)*step_l
    ray1_z_increment = math.sin(ray1_pitch)*step_l

    ray2_x_increment = math.cos(ray2_az)*step_l
    ray2_y_increment = math.sin(ray2_az)*step_l
    ray2_z_increment = math.sin(ray2_pitch)*step_l

    steps1_y = t.linspace(ray1_y0, ray1_y0+step_n*ray1_y_increment, step_n)
    steps1_z = t.linspace(ray1_z0, ray1_z0+step_n*ray1_z_increment, step_n)
    steps1_x = t.linspace(ray1_x0, ray1_x0+step_n*ray1_x_increment, step_n)

    steps2_x = t.linspace(ray2_x0, ray2_x0+step_n*ray2_x_increment, step_n)
    steps2_y = t.linspace(ray2_y0, ray2_y0+step_n*ray2_y_increment, step_n)
    steps2_z = t.linspace(ray2_z0, ray2_z0+step_n*ray2_z_increment, step_n)
    x1 = steps1_x.repeat(step_n,1)
    x2 = steps2_x.repeat(step_n,1).transpose(0,1)
    y1 = steps1_y.repeat(step_n,1)
    y2 = steps2_y.repeat(step_n,1).transpose(0,1)
    z1 = steps1_z.repeat(step_n,1)
    z2 = steps2_z.repeat(step_n,1).transpose(0,1)
    difx = x1-x2
    dify = y1-y2
    difz = z1-z2
    sqx = difx**2
    sqy = dify**2
    sqz = difz**2
    res = t.sqrt(sqx+sqy+sqz)
    for i in range(step_n):
        res[i,i] = 100000

    r1r2distances = res
    # -------------------------------------
    argmin = r1r2distances.argmin()
    presicion = r1r2distances.min()
    argmin_1 = argmin // step_n
    argmin_2 = argmin % step_n

    min1_x = ray1_x0 + ray1_x_increment*argmin_1
    min1_y = ray1_y0 + ray1_y_increment*argmin_1
    min1_z = ray1_z0 + ray1_z_increment*argmin_1

    min2_x = ray2_x0 + ray2_x_increment*argmin_2
    min2_y = ray2_y0 + ray2_y_increment*argmin_2
    min2_z = ray2_z0 + ray2_z_increment*argmin_2


    intersection_x = (min1_x + min2_x) / 2
    intersection_y = (min1_y + min2_y) / 2
    intersection_z = (min1_z + min2_z) / 2
    return intersection_x, intersection_y, intersection_z, presicion


get_intersection_point_2cameras(1920/2,1080/2,1920/2,1080/2,1920,1080,35,20,20,100,0,0,pi,0,100,0,3*pi/2)
# test1 ,= 0,0,0,1