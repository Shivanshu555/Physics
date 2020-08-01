## This program is to draw various graph for a motion defined by an equation
## The graphs included are
##   * Position-Time Graph
##   * Velocity-Time Graph
##   * Acceleration-Time Graph

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.gridspec as gridspec


# Equation for the motion

t=symbols('t')

##--------------------------------------------------------------------------------------,
expr=cos(t)+10 # Expression of position in time (Equation input is given here)             |
##--------------------------------------------------------------------------------------'

x=lambdify(t,expr) # gives position at time t (works as a lambda function)


# Time interval
ti=0            #inital time
tf=10           #final time

n=100 #number of divisions
fig=plt.figure()

# For maximizing the graph window
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()


# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)
#============================== Position Time Graph ========================================

T=np.linspace(ti, tf, n) # Time Interval
X=x(T) #Position

#Creating first plot
ax1=plt.subplot(gs[0,0]) #row 0, col 0

line, =ax1.plot(T,X,label='Position')
point,=ax1.plot([T[0]],[X[0]],'o')
trace,=ax1.plot([T[0],T[0]],[0,X[0]],color='orange')
ax1.legend()
ax1.set_xlim(ti,tf)
try:ax1.set_ylim(min(X),max(X))
except:pass
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')

#=============================== Velocity-Time Graph ======================================

ax2=plt.subplot(gs[0,1]) #row 0, col 1

dv=diff(expr,t) # dv=dx/dt
v=lambdify(t,dv) # gives the instantaneous velocity at time t

V=v(T) # Instantaneous Velocity

# Creating the first plot
ax2=plt.subplot(gs[0,1]) #row 0, col 1

line2, =ax2.plot(T,V,label='Instataneous Velocity')
point2,=ax2.plot([T[0]],[V[0]],'o')
trace2,=ax2.plot([T[0],T[0]],[0,V[0]],color='orange')
ax2.legend()
ax2.set_xlim(ti,tf)
try:ax2.set_ylim(min(V),max(V))
except:pass
ax2.set_xlabel('Time')
ax2.set_ylabel('Velocity')

#==================================Acceleration-Time Graph=================================
ax3=plt.subplot(gs[1,:]) #row 2, col span all

da=diff(dv,t) # da=dv/dt
a=lambdify(t,da)

A=a(T) #Instataneous Acceleration

# Creating the first plot

line3, =ax3.plot(T,A,label='Instataneous Acceleration')
point3,=ax3.plot([T[0]],[A[0]],'o')
trace3,=ax3.plot([T[0],T[0]],[0,A[0]],color='orange')

ax3.legend()
ax3.set_xlim(ti,tf)
try:
    ax3.set_ylim(min(A),max(A))
except:
    pass
ax3.set_xlabel('Time')
ax3.set_ylabel('Acceleration')

# moving the point position at every frame
def update_point(n,T,X,V,A,point,point2,point3,trace,trace2,trace3):
    point.set_data(np.array([T[n],  X[n]]))
    point2.set_data(np.array([T[n], V[n]]))
    point3.set_data(np.array([T[n], A[n]]))

    trace.set_data([T[n],T[n]],[0,X[n]])
    trace2.set_data([T[n],T[n]],[0,V[n]])
    trace3.set_data([T[n],T[n]],[0,A[n]])
    
    return point,point2,point3,trace,trace2,trace3

ani=animation.FuncAnimation(fig, update_point, frames=n,
                            fargs=(T,X,V,A,point,point2,point3,trace,trace2,trace3),
                            interval=5,repeat=False)

plt.show()
