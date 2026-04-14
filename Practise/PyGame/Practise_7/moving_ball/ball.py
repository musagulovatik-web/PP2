def mb(x, y, k, w, h):
    nx=x
    ny=y
    if k==1:
        ny=ny-20
    if k==2:
        ny=ny+20
    if k==3:
        nx=nx-20
    if k==4:
        nx=nx+20
    if 25<=nx<=w-25 and 25<=ny<=h-25:
        return nx, ny
    return x,y