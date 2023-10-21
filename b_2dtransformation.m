x1 = input('x1 = ');
y1 = input('y1 = ');


x2 = input('x2 = ');
y2 = input('y2 = ');




m1 = y1/x1;
m2 = y2/x2;

a = atand((m2 - m1)/(1+m1*m2));
b = atand(y2/x2);
r = [cos(a) -sin(a) 0; sin(a) cos(a) 0; 0 0 1];
d = abs(sqrt(x2^2 + y2^2)-sqrt(x1^2 + y1^2));

t = [1 0 d*cos(b); 0 1 d*sin(b); 0 0 1];

m_final = t*r;
m_final



[c(t)      -s(t)         0     r(i-1); 
 s(t)*c(a)  c(t)*c(a)   -s(a)  -d(s(a));
 s(t)*s(a)  c(t)*s(a)   s(a)   d*s(a);
 0           0           0        1];











