x1 = input('x1 = ');
y1 = input('y1 = ');
z1 = input('z1 = ');

x2 = input('x2 = ');
y2 = input('y2 = ');
z2 = input('z2 = ');

p1 = [x1, y1, z1];
p2 = [x2, y2, z2];

n = cross(p1, p2);

th_r = asind(norm(n)/(norm(p1)*norm(p2)));

nx = (y1*z2 - y2*z1)/norm(n);
ny = (x2*z1 - x1*z2)/norm(n);
nz = (x1*y2 - x2*y1)/norm(n);


n_c = [nx, ny, nz];

t = 1 - cos(th_r);

c = cos(th_r);
s = sin(th_r);


R = [t*nx^2+c t*nx*ny-s*nx t*nx*ny+s*ny 0; t*nx*ny+s*nx t*ny^2+c t*ny*nz-s*nx 0;t*nx*nz-s*ny t*ny*nz+s*nx t*nz^2+c 0; 0 0 0 1];
D = abs(norm(p1)-norm(p2));
th_x = acosd(x2/norm(p2));
th_y = acosd(y2/norm(p2));
th_z = acosd(z2/norm(p2));


T = [1 0 0 D*cos(th_x);0 1 0 D*cos(th_y); 0 0 1 D*cos(th_z); 0 0 0 1];

M_final = T*R;
M_final