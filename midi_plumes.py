import csv
import math
import os
import shutil
from miditime.miditime import MIDITime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
#import multiprocessing as mp

## ----- Make midi files for each 

names = ['Bowie','Cobb','Easter','Foundation','Galapagos','Hawaii','Kerguelen','Louisville','Marquesas','Reunion','StHelena','Tristan']

notes = [ 1, 3, 37, 28, 8, -9, 9, -11, 13, 16, 18, 20, 23]

print(notes)
print(names)

midis = []
peaks = []
tones = []
points = []

for i in range(12): # loop over 11 hotspots
    #print(i)
    str = names[i] + "_totalpeaks"
    #print(str)
    tones=[] # empty tones list
    mymidi = MIDITime(120, 'mymidi.mid') # midi file setup
    
    with open(str, newline='') as csv_file: # read csv file
        csv_reader = csv.reader(csv_file)
        peaks = list(csv_reader)
        #print("peaks is", peaks)
        #peaks = [float(i) for i in peaks]
        #print(tmp)
        #print(len(tmp))
        
        for j in range(len(peaks[0])): # loop over peaks (notes)
            #print("j is", j)
            #print("tmp is", peaks)
            MX=max(peaks)
            #print(MX)
            A = [0, 59 + notes[i], 100, float(peaks[0][j])]
            #print("A is", A)
            
            for k in range(math.floor(200/A[3])): # repeat note enough to cover 200 seconds
                B = [k * A[3], A[1], A[2], A[3]]
                #print(B)
                #print("B is", B)
                tones.append(B) # stick notes on end of tones list
                C = [k * A[3] * 100, i, A[3]]
                points.append(C)
    

    
    mymidi.add_track(tones) # creat the midi from the list of tones (1 hotspot only)
#    print(i)
#    print(notes)
    
#print(mymidi)

#print(tones)

# Output the .mid file
    mymidi.save_midi() # save it
    
    dest = names[i] + 'midi.mid'

    os.rename("mymidi.mid", dest) # rename it
    
## -----

## ----- Plot data and make movie frames

names = ['Bowie','Cobb','Easter','Foundation','Galapagos','Hawaii','Kerguelen','Louisville','Marquesas','Reunion','St. Helena','Tristan']

colors = ['#c4fff7','#3690c0','#0570b0','#bdf6fe','#06b1c4','#3690c0','#9cef43','#b8ffeb','#41b6c4','#99cc04','#c83cb9','#ff0490']


#fig, ax = plt.subplots(dpi=100,figsize=(5,3),constrained_layout=True)



fig, ax = plt.subplots(dpi=400,figsize=(8,6))

ax.set_facecolor('xkcd:dark')
fig.patch.set_facecolor('xkcd:dark')


#ax.set_title('The Song of the Plume')
ax.set_xlim(0,12)
ax.grid(True)
ax.set_xlabel("time (myr)", loc='left')
plt.gca().invert_yaxis()

#params = {"ytick.color" : "w",
#          "xtick.color" : "w",
#          "axes.labelcolor" : "w",
#          "axes.edgecolor" : "w",
#          "text.color": "w",
#          "axes.titlecolor": "w"}
#plt.rcParams.update(params)
ax.grid(color='w', linestyle='-', linewidth=0.025)

l = 0

# plot data
p010, = ax.plot([l/100] * 12, names,'-',color='darkorange')

dotsx0 = []
dotsy0 = []
dotsx1 = []
dotsy1 = []
dotsx2 = []
dotsy2 = []
dotsx3 = []
dotsy3 = []
dotsx4 = []
dotsy4 = []
dotsx5 = []
dotsy5 = []
dotsx6 = []
dotsy6 = []
dotsx7 = []
dotsy7 = []
dotsx8 = []
dotsy8 = []
dotsx9 = []
dotsy9 = []
dotsx10 = []
dotsy10 = []
dotsx11 = []
dotsy11 = []
dotsx12 = []
dotsy12 = []
dotcolor = []
dotsnowx = []
dotsnowy = []
dotsnowcolor = []
dotsfadex = []
dotsfadey = []
dotsfadecolor = []
dotsfadealpha = []

for p in range(len(points)):
    if points[p][0] < l:
        if points[p][1]==0:
            dotsx0.append(points[p][0]/100)
            dotsy0.append(points[p][1])
        if points[p][1]==1:
            dotsx1.append(points[p][0]/100)
            dotsy1.append(points[p][1])
        if points[p][1]==2:
            dotsx2.append(points[p][0]/100)
            dotsy2.append(points[p][1])
        if points[p][1]==3:
            dotsx3.append(points[p][0]/100)
            dotsy3.append(points[p][1])
        if points[p][1]==4:
            dotsx4.append(points[p][0]/100)
            dotsy4.append(points[p][1])
        if points[p][1]==5:
            dotsx5.append(points[p][0]/100)
            dotsy5.append(points[p][1])
        if points[p][1]==6:
            dotsx6.append(points[p][0]/100)
            dotsy6.append(points[p][1])
        if points[p][1]==7:
            dotsx7.append(points[p][0]/100)
            dotsy7.append(points[p][1])
        if points[p][1]==8:
            dotsx8.append(points[p][0]/100)
            dotsy8.append(points[p][1])
        if points[p][1]==9:
            dotsx9.append(points[p][0]/100)
            dotsy9.append(points[p][1])
        if points[p][1]==10:
            dotsx10.append(points[p][0]/100)
            dotsy10.append(points[p][1])
        if points[p][1]==11:
            dotsx11.append(points[p][0]/100)
            dotsy11.append(points[p][1])
        if points[p][1]==12:
            dotsx12.append(points[p][0]/100)
            dotsy12.append(points[p][1])
  
    if round(points[p][0]) == l:
        dotsnowx = points[p][0]/100
        dotsnowy = points[p][1]
        dotsnowcolor = colors[points[p][1]]
    if (round(points[p][0]) > (l-100)) & (points[p][0] < l):
        dotsfadex.append(points[p][0]/100)
        dotsfadey.append(points[p][1])
        dotsfadecolor.append(colors[points[p][1]])
        dotsfadealpha.append((100-(l-round(points[p][0])))/100)
        
    
#dotsy = names[points[l][1]]*len(dotsx)
#for q in range(len(dotsx)):
    p00, = ax.plot(dotsx0, dotsy0, 'o', markersize=7, markerfacecolor='xkcd:dark', color='aquamarine')# color=dotcolor[q])
    p01, = ax.plot(dotsx1, dotsy1, 'o', markersize=5, markerfacecolor='xkcd:dark', color='paleturquoise')# color=dotcolor[q])
    p02, = ax.plot(dotsx2, dotsy2, 'o', markersize=5, markerfacecolor='xkcd:dark', color='lightblue')# color=dotcolor[q])
    p03, = ax.plot(dotsx3, dotsy3, 'o', markersize=6, markerfacecolor='xkcd:dark', color='cyan')# color=dotcolor[q])
    p04, = ax.plot(dotsx4, dotsy4, 'o', markersize=10, markerfacecolor='xkcd:dark', color='aqua')# color=dotcolor[q])
    p05, = ax.plot(dotsx5, dotsy5, 'o', markersize=6, markerfacecolor='xkcd:dark', color='cornflowerblue')# color=dotcolor[q])
    p06, = ax.plot(dotsx6, dotsy6, 'o', markersize=12, markerfacecolor='xkcd:dark', color='springgreen')# color=dotcolor[q])
    p07, = ax.plot(dotsx7, dotsy7, 'o', markersize=6, markerfacecolor='xkcd:dark', color='mediumaquamarine')# color=dotcolor[q])
    p08, = ax.plot(dotsx8, dotsy8, 'o', markersize=5, markerfacecolor='xkcd:dark', color='lightcyan')# color=dotcolor[q])
    p09, = ax.plot(dotsx9, dotsy9, 'o', markersize=8, markerfacecolor='xkcd:dark', color='lime')# color=dotcolor[q])
    p10, = ax.plot(dotsx10, dotsy10, 'o', markersize=6, markerfacecolor='xkcd:dark', color='magenta')# color=dotcolor[q])
    p11, = ax.plot(dotsx11, dotsy11, 'o', markersize=6, markerfacecolor='xkcd:dark', color='hotpink')# color=dotcolor[q])
    #p12, = ax.plot(dotsx12, dotsy12, 'o', markersize=5, markerfacecolor='xkcd:dark', color='aquamarine')# color=dotcolor[q])
#for r in range(len(dotsfadex)):
    #p015, = ax.plot(dotsfadex, dotsfadey, 'bo', markersize=8, alpha=0.1)# color=dotsfadecolor[r], alpha=dotsfadealpha[r]/2)
#if dotsnowx:
    #p016, = ax.plot(dotsnowx, dotsnowy, 'o', markersize=20, markerfacecolor='darkslategray', color='magenta')# color=dotsnowcolor)
    
# # Data Update
xmin = 0.0
xmax = 12.0
x = 0.0

def updateData(self):
    global x
#     global names:
#     global points
#     global m
    global l
    global dotsnowx
    global dotsnowy
#     global markerdecay
    
    l += 2

    p010.set_data([l/100] * 12, names)
     
    dotsx0 = []
    dotsy0 = []
    dotsx1 = []
    dotsy1 = []
    dotsx2 = []
    dotsy2 = []
    dotsx3 = []
    dotsy3 = []
    dotsx4 = []
    dotsy4 = []
    dotsx5 = []
    dotsy5 = []
    dotsx6 = []
    dotsy6 = []
    dotsx7 = []
    dotsy7 = []
    dotsx8 = []
    dotsy8 = []
    dotsx9 = []
    dotsy9 = []
    dotsx10 = []
    dotsy10 = []
    dotsx11 = []
    dotsy11 = []
#    dotsx12 = []
#    dotsy12 = []
    dotcolor = []
    dotsnowx = []
    dotsnowy = []
    dotsnowcolor = []
    dotsfadex = []
    dotsfadey = []
    dotsfadecolor = []
    dotsfadealpha = []
    
    for p in range(len(points)):
        if points[p][0] < l:
            if points[p][1]==0:
                dotsx0.append(points[p][0]/100)
                dotsy0.append(points[p][1])
            if points[p][1]==1:
                dotsx1.append(points[p][0]/100)
                dotsy1.append(points[p][1])
            if points[p][1]==2:
                dotsx2.append(points[p][0]/100)
                dotsy2.append(points[p][1])
            if points[p][1]==3:
                dotsx3.append(points[p][0]/100)
                dotsy3.append(points[p][1])
            if points[p][1]==4:
                dotsx4.append(points[p][0]/100)
                dotsy4.append(points[p][1])
            if points[p][1]==5:
                dotsx5.append(points[p][0]/100)
                dotsy5.append(points[p][1])
            if points[p][1]==6:
                dotsx6.append(points[p][0]/100)
                dotsy6.append(points[p][1])
            if points[p][1]==7:
                dotsx7.append(points[p][0]/100)
                dotsy7.append(points[p][1])
            if points[p][1]==8:
                dotsx8.append(points[p][0]/100)
                dotsy8.append(points[p][1])
            if points[p][1]==9:
                dotsx9.append(points[p][0]/100)
                dotsy9.append(points[p][1])
            if points[p][1]==10:
                dotsx10.append(points[p][0]/100)
                dotsy10.append(points[p][1])
            if points[p][1]==11:
                dotsx11.append(points[p][0]/100)
                dotsy11.append(points[p][1])
#            if points[p][1]==12:
#                dotsx12.append(points[p][0]/100)
#                dotsy12.append(points[p][1])  
        if round(points[p][0]) == l:
            dotsnowx = points[p][0]/100
            dotsnowy = points[p][1]
            dotsnowcolor = colors[points[p][1]]
        if (round(points[p][0]) > (l-100)) & (points[p][0] < l):
            dotsfadex.append(points[p][0]/100)
            dotsfadey.append(points[p][1])
            dotsfadecolor.append(colors[points[p][1]])
            dotsfadealpha.append((100-(l-round(points[p][0])))/100)

    p00.set_data(dotsx0, dotsy0)
    p01.set_data(dotsx1, dotsy1)
    p02.set_data(dotsx2, dotsy2)
    p03.set_data(dotsx3, dotsy3)
    p04.set_data(dotsx4, dotsy4)
    p05.set_data(dotsx5, dotsy5)
    p06.set_data(dotsx6, dotsy6)
    p07.set_data(dotsx7, dotsy7)
    p08.set_data(dotsx8, dotsy8)
    p09.set_data(dotsx9, dotsy9)
    p10.set_data(dotsx10, dotsy10)
    p11.set_data(dotsx11, dotsy11)
#    p12.set_data(dotsx12, dotsy12)

    if (l/100>=10):
         ax.set_xlim(l/100-10,l/100+2)
#         # p011.ax.set_xlim(l/100-10,l/100+2)
#         # p012.ax.set_xlim(l/100-10,l/100+2)
#         # p013.ax.set_xlim(l/100-10,l/100+2)
#         p014.ax.set_xlim(l/100-10,l/100+2)

    #p016.set_data(dotsnowx, dotsnowy)
    
    #params = {"ytick.color" : "w",
#	  "xtick.color" : "w",
#	  "axes.labelcolor" : "w",
#	  "axes.edgecolor" : "w",
#	  "text.color": "w",
#	  "axes.titlecolor": "w"}
#    plt.rcParams.update(params)
     
    ax.grid(color='w', linestyle='-', linewidth=0.025)
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_xlabel("time (myr)", loc='left')

    
    return p00, p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, ax, plt
    
simulation = animation.FuncAnimation(fig, updateData, blit=False, frames=20000, interval=20, repeat=False)
simulation.save(filename='plumesong.mp4',fps=50,dpi=400)
     
     
     
    
#     dotsx.append(points[l][0]/100)
#     dotsy.append(names[points[l][1]])
    
#     p014.set_data(dotsx,dotsy)

#     #for m in range(len(points)):

#         # if (points[m][0]/100 <= l/100) & (m > 0):
#         #     p011.set_data(np.true_divide(points[0:m][0],100), names[points[m][1]]*m)
#         #     p011.set_color(colors[points[m][1]])
            
#         # if (points[m][0]/100 <= l/100) & (points[m][0]/100 <= (l/100)-5):
#         #     markerdecay=(points[m][0]/100-(l/100-8))
#         #     p012.set_data(points[m][0]/100, names[points[m][1]])
#         #     p012.set_markersize(markerdecay)
#         #     p012.set_color(colors[points[m][1]])
            
#         # if (points[m][0]/100 <= l/100) & (points[m][0]/100 > (l/100)-5):
#         #     markerdecay=(points[m][0]/100-(l/100-8))
#         #     p013.set_data(points[m][0]/100, names[points[m][1]])
#         #     p013.set_markersize(markerdecay)
#         #     p013.set_color(colors[points[m][1]])
            
#         # if (points[m][0]/100 == l/100):
#         #     p014.set_data(points[m][0]/100, names[points[m][1]])
#         #     p014.set_color(colors[points[m][1]])
    
    

#     if (l/100>=10):
#         # p010.ax.set_xlim(l/100-10,l/100+2)
#         # p011.ax.set_xlim(l/100-10,l/100+2)
#         # p012.ax.set_xlim(l/100-10,l/100+2)
#         # p013.ax.set_xlim(l/100-10,l/100+2)
#         p014.ax.set_xlim(l/100-10,l/100+2)
        
#     return p014

# simulation = animation.FuncAnimation(fig, updateData, blit=False, frames=200, interval=20, repeat=False)
# simulation.save(filename='sim.mp4',fps=30,dpi=300)

#plt.show()
 



# for l in range(1350,2000):
    
#     fig, ax = plt.subplots(dpi=100,figsize=(5,3),constrained_layout=True)

#     ax.set_facecolor('xkcd:dark')
#     fig.patch.set_facecolor('xkcd:dark')
#     params = {"ytick.color" : "w",
#               "xtick.color" : "w",
#               "axes.labelcolor" : "w",
#               "axes.edgecolor" : "w",
#               "text.color": "w",
#               "axes.titlecolor": "w"}
#     plt.rcParams.update(params)
    
#     ax.plot([l/100] * 12, names,'-',color='darkorange')
    
#     for m in range(len(points)):
    
#         if (points[m][0]/100 <= l/100):
#             ax.plot(points[m][0]/100, names[points[m][1]], 'o',markersize=1, color=colors[points[m][1]])
#         if (points[m][0]/100 <= l/100):
#             markerdecay=(points[m][0]/100-(l/100-8))
#             ax.plot(points[m][0]/100, names[points[m][1]], 'o',markersize=markerdecay, alpha=0.25, color=colors[points[m][1]])
#         if (points[m][0]/100 <= l/100) & (points[m][0]/100 > (l/100)-5):
#             markerdecay=(points[m][0]/100-(l/100-8))
#             ax.plot(points[m][0]/100, names[points[m][1]], 'o',markersize=markerdecay, alpha=0.5, color=colors[points[m][1]])
#         if (points[m][0]/100 == l/100):
#             ax.plot(points[m][0]/100, names[points[m][1]], 'o',markersize=16, color=colors[points[m][1]])
    
    
#         #ax.set(xlabel='time (myr)', title='The Song of the Plume')
#         ax.set_xlabel('time (myr)')
#         ax.grid(color='w', linestyle='-', linewidth=0.025)
#         plt.gca().invert_yaxis()
#         if (l/100<10):
#             plt.xlim(0,12)
#         else:
#             plt.xlim(l/100-10,l/100+2)
            
#         plot_margin = 0.25

#         x0, x1, y0, y1 = plt.axis()
#         plt.axis((x0 - plot_margin,
#           x1 + plot_margin,
#           y0 - plot_margin,
#           y1 + plot_margin))
#         plt.plot()
#         #plt.close()
    
#     framenum = "% s" % l
    
#     fig.savefig('frame'+ framenum + '.png')
#     plt.close(fig)
    


## -----
    
    
    
    


## ----- loading scripts    
    


#with open('Bowie_totalpeaks', newline='') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    Bowie = list(csv_reader)
    
# with open('Cobb_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Cobb = list(csv_reader)    

# with open('Easter_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Easter = list(csv_reader)
    
# with open('Foundation_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Foundation = list(csv_reader)    

# with open('Hawaii_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Hawaii = list(csv_reader)

# with open('Kerguelen_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Kerguelen = list(csv_reader)

# with open('Louisville_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Louisville = list(csv_reader)

# with open('Marquesas_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Marquesas = list(csv_reader)

# with open('Reunion_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Reunion = list(csv_reader)

# with open('StHelena_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     StHelena = list(csv_reader)

# with open('Tristan_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Tristan = list(csv_reader)

#with open('Galapagos_totalpeaks', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     Galapagos = list(csv_reader)

# -----
