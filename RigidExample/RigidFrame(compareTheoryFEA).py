# _*_ coding:utf-8 _*_

b=0.3
h=0.4

l=1
E=2.1*10**11
I=(1/12)*b*h**3

#u_fea=6.726*10**-9
u_fea=6.032*10**-9
xita_fea=5.952*10**-9


xita_theory=2/(2.1*10**11*(1/12)*b*h**3)

u_theory=2/(2.1*10**11*(1/12)*b*h**3)

print('xita_theory:'+str(xita_theory))

print(('u_theory:'+str(u_theory)))

print('error_u:'+str(((u_fea-u_theory)/u_theory)))
print('error_xita:'+str(((xita_fea-xita_theory)/xita_theory)))


print(1*(E*I)**-1)
print(2/(2.1*10**11*(0.3*0.4)))