
f1=74.9 #mm %Insert focal length of the lens that needs to be characterised
f1_m=f1*100
phi1=1/f1_m
f3=30 #mm %Insert focal length of the lens that needs to be characterised
f3_m=f3*100
phi3=1/f3_m
f2=-8.92 #mm  %Insert focal length of the lens that needs to be characterised
f2_m=f2*100
phi2=1/f2_m
Tmax=-((f2+f3)*f1)/(f2*f3)
Tmin=-(f2*f1)/((f1+f2)*f3)


print("maximum magnification=", Tmax)
print("smallest magnification=", Tmin)
L_max= f1+2*f2+f3+f2*((f3+Tmax)/(f1)+(f1)/(f3*Tmax))
t1max=f1+f2+((f1*f2)/(Tmax*f3))
t2max=f2+f3+(f2*f3*Tmax/f1)


L_min= f1+2*f2+f3+f2*((f3+Tmin)/(f1)+(f1)/(f3*Tmin))
t1min=f1+f2+((f1*f2)/(Tmin*f3))
t2min=f2+f3+(f2*f3*Tmin/f1)

print("For maximum magnification", Tmax, "t1=", t1max, "t2=", t2max)
print("For minimum magnification", Tmin, "t1=", t1min, "t2=", t2min)


T=0.5
while T < 2:
  print("T=",T)
  #lets find the length of the system!
  L_max= f1+2*f2+f3+f2*((f3+T)/(f1)+(f1)/(f3*T))
  print("Lmax=", L_max)
  #Distance btw lense 1 and 2
  t1=f1+f2+((f1*f2)/(T*f3))
  t2=f2+f3+(f2*f3*T/f1)
  T=T+0.1
  print("t1=", t1)
  print("t2=", t2)
