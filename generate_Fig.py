import numpy as np

from matplotlib import rcParams
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
myData = np.loadtxt('Data/stroop_mg.csv', delimiter=';',dtype=str,skiprows=1)



fig_width = 6 # width in inches
fig_height = 8  # height in inches
fig_size =  [fig_width,fig_height]
params = {'axes.labelsize': 14,
          'axes.titlesize': 13,
          'font.size': 11,
          'xtick.labelsize': 11,
          'ytick.labelsize': 11,
          'figure.figsize': fig_size,
          #'savefig.dpi' : 600,
          'axes.linewidth' : 1.3,
          'ytick.major.size' : 4,      # major tick size in points
          'xtick.major.size' : 4      # major tick size in points
          #'edgecolor' : None
          #'xtick.major.size' : 2,
          #'ytick.major.size' : 2,
          }
rcParams.update(params)

# set sans-serif font to Arial
rcParams['font.sans-serif'] = 'Arial'

# create figure instance
fig = plt.figure()


# define sub-panel grid and possibly width and height ratios
gs = gridspec.GridSpec(2, 1,
                       #width_ratios=[1,1.2],
                       #height_ratios=[1,1]
                       )

# define vertical and horizontal spacing between panels
gs.update(wspace=0.3,hspace=0.4)

# possibly change outer margins of the figure
plt.subplots_adjust(left=0.2, right=0.92, top=0.9, bottom=0.1)

# sub-panel enumerations
plt.figtext(0.05, 0.95, 'Stroop effect',clip_on=False,color='black', weight='bold',size=20)
#plt.figtext(0.47, 0.92, 'B',clip_on=False,color='black', weight='bold',size=22)
#plt.figtext(0.06, 0.47, 'C',clip_on=False,color='black', weight='bold',size=22)
#plt.figtext(0.47, 0.47, 'D',clip_on=False,color='black', weight='bold',size=22)


# first sub-plot #######################################################
ax0 = plt.subplot(gs[0])

# title
ax0.set_title('Absolut times for each word list')

# diplay of data
#ax0.axhline(y=0,ls='--',color='0.5',lw=2)
#ax0.axvline(x=0,ls='--',color='0.5',lw=2)
for i in range(len(myData)):
    ax0.plot(np.array([0,1]),([myData[i,2].astype(np.float),myData[i,3].astype(np.float)]),'-o')
    #ax0.plot(x,cosy,label='cos')

# removes upper and right axes 
# and moves left and bottom axes away
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['bottom'].set_position(('outward', 10))
ax0.spines['left'].set_position(('outward', 10))
ax0.yaxis.set_ticks_position('left')
ax0.xaxis.set_ticks_position('bottom')


ax0.set_xlim(-.3,1.3)
plt.xticks([0, 1],["1. list\ncongruent", "2. list\nincongruent"])

# legends and labels
#plt.legend(loc=1,frameon=False)

#plt.xlabel('time (sec)')
plt.ylabel('time (sec)')

# first sub-plot #######################################################
ax0 = plt.subplot(gs[1])

# title
ax0.set_title('Difference in times between both lists')

# diplay of data
ax0.axhline(y=1,ls='--',color='0.7',lw=2)
#ax0.axvline(x=0,ls='--',color='0.5',lw=2)
#for i in range(len(myData)):
ax0.plot(myData[:,0].astype(np.int),myData[:,3].astype(np.float)/myData[:,2].astype(np.float),'o')
#ax0.plot(x,cosy,label='cos')

# removes upper and right axes 
# and moves left and bottom axes away
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['bottom'].set_position(('outward', 10))
ax0.spines['left'].set_position(('outward', 10))
ax0.yaxis.set_ticks_position('left')
ax0.xaxis.set_ticks_position('bottom')

majorLocator_x = plt.MultipleLocator(1)
ax0.xaxis.set_major_locator(majorLocator_x)


ax0.set_xscale('log')


# legends and labels
#plt.legend(loc=1,frameon=False)

#plt.xlabel('time (sec)')
plt.ylabel('ratio of times\n(incongruent/congruent)')
plt.xlabel('age of participant (years)')

## save figure ############################################################
fname = 'fig_stroop'

plt.savefig(fname+'.png')
plt.savefig(fname+'.pdf')
