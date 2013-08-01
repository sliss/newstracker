'''
Created on Jun 24, 2012

@author: stevenliss
'''
from decimal import *

getcontext().prec = 30

#special relativity
mph=Decimal(65)
v=Decimal(mph*Decimal("0.44704"))
#print mph
#print v
stationary_time=Decimal(16000)
special_bus_time=Decimal(0)
c=Decimal(299800000)

L=getcontext().power(Decimal("1")-(v*v)/(c*c), Decimal(".5"))

special_bus_time = stationary_time * L
print special_bus_time
s_dif = stationary_time-special_bus_time
print s_dif

# general relativity
general_bus_time=Decimal(0)
schwarzchild=Decimal(".009")
height=Decimal("2")
r=Decimal("6378100")

tau0=getcontext().power(Decimal("1")-schwarzchild/r, Decimal(".5"))
tau=getcontext().power(Decimal("1")-schwarzchild/(r+height), Decimal(".5"))

general_bus_time = stationary_time * (tau/tau0)
#print tau/tau0
print general_bus_time
g_dif = stationary_time-general_bus_time
print g_dif

total_dilation= g_dif + s_dif #time saved onboard bus
print total_dilation
print stationary_time - g_dif - s_dif

print total_dilation * Decimal("1000000000")