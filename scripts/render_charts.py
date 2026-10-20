#!/usr/bin/env python3
"""Rebuild public SVG figures from safe observed metrics (not the agent implementation)."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/metrics.json').read_text(encoding='utf-8'))
OUT=ROOT/'assets'
OUT.mkdir(exist_ok=True)
DARK='#24313F'
BLUE='#3569A5'
SLATE='#64748B'
GRID='#DAE1E7'
LIGHT='#E5EBF1'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','axes.titlesize':11,'axes.titleweight':'semibold','font.size':9,'axes.edgecolor':GRID,'xtick.color':SLATE,'ytick.color':DARK,'figure.facecolor':'white','savefig.facecolor':'white'})

def bar_panel(ax,title,labels,vals,maxv,suffix=''):
    ax.set_title(title,loc='left',color=DARK,pad=15)
    y=np.arange(len(labels))
    ax.barh(y,vals,color=BLUE,height=.39)
    ax.set_xlim(0,maxv*1.17)
    ax.set_yticks(y,labels)
    ax.invert_yaxis()
    ax.set_xticks([])
    ax.tick_params(left=False)
    for spine in ax.spines.values():spine.set_visible(False)
    for yy,v in zip(y,vals): ax.text(min(v+.2,maxv*1.03),yy,f'{v}{suffix}',ha='left',va='center',color=DARK,fontweight='semibold',fontsize=10)

fig, axs=plt.subplots(1,3,figsize=(15.5,3.4),dpi=160)
bar_panel(axs[0],'Acceptance checks', ['Variant A','Variant B'],[DATA['acceptance_checks']['variant_A'],DATA['acceptance_checks']['variant_B']],11,' / 11')
bar_panel(axs[1],'Agent turns', ['Variant A','Variant B'],[DATA['agent_turns']['variant_A'],DATA['agent_turns']['variant_B']],9)
bar_panel(axs[2],'Matrix checker', ['Layer 0','Layer 5'],[DATA['matrix_checks']['layer_0'],DATA['matrix_checks']['layer_5']],5,' / 5')
fig.subplots_adjust(left=.07,right=.99,bottom=.14,top=.69,wspace=.75)
fig.suptitle('Observed verification summary',fontweight='bold',color=DARK,fontsize=16,x=.025,ha='left',y=.97)
fig.savefig(OUT/'verification-metrics.svg',bbox_inches='tight',pad_inches=.22)
plt.close(fig)

acts=DATA['feedback_disabled_actions']
fig,ax=plt.subplots(figsize=(10,3.1),dpi=170)
labels=list(acts)
vals=list(acts.values())
y=np.arange(4)
ax.barh(y,vals,color=[BLUE,LIGHT,LIGHT,LIGHT],height=.5)
ax.set_yticks(y,labels,fontsize=10)
ax.invert_yaxis()
ax.set_xlim(0,14)
ax.set_xticks([0,3,6,9,12])
ax.grid(axis='x',color=GRID,linestyle='-',lw=.7)
ax.set_axisbelow(True)
ax.tick_params(left=False,bottom=False)
for sp in ax.spines.values():sp.set_visible(False)
for yy,v in zip(y,vals):ax.text(v+.2,yy,str(v),va='center',fontsize=11,color=DARK,fontweight='semibold')
ax.set_title('Tool actions · feedback disabled (12-turn limit)',loc='left',fontsize=15,fontweight='bold',color=DARK,pad=16)
ax.set_xlabel('Recorded tool selections',color=SLATE,labelpad=8)
fig.subplots_adjust(left=.2,right=.97,top=.83,bottom=.2)
fig.savefig(OUT/'feedback-ablation.svg',bbox_inches='tight',pad_inches=.18)
plt.close(fig)

m=np.fromfunction(lambda i,j,k: i*100+j*10+k+1,(10,10,10),dtype=int).astype(int)
views=[('XY plane · k = 0',m[:,:,0], 'j →'),('YZ plane · i = 0',m[0,:,:],'k →'),('XZ plane · j = 0',m[:,0,:],'k →')]
fig,axs=plt.subplots(1,3,figsize=(16.4,6),dpi=180)
for ax,(title,plane,xlabel) in zip(axs,views):
    ax.imshow(plane,cmap='Blues',vmin=plane.min(),vmax=plane.max(),aspect='equal',interpolation='nearest')
    ax.set_title(title,fontsize=15,color=DARK,fontweight='semibold',pad=15)
    ax.set_xticks(np.arange(10),labels=np.arange(10),fontsize=8)
    ax.set_yticks(np.arange(10),labels=np.arange(10),fontsize=8)
    ax.tick_params(length=0,pad=5)
    ax.set_xticks(np.arange(-.5,10,1),minor=True)
    ax.set_yticks(np.arange(-.5,10,1),minor=True)
    ax.grid(which='minor',color='white',linewidth=1.25)
    ax.tick_params(which='minor',bottom=False,left=False)
    ax.set_xlabel(xlabel,color=SLATE,fontsize=10)
    ax.set_ylabel(['i ↓','j ↓','i ↓'][list(axs).index(ax)],color=SLATE,fontsize=10,rotation=0,labelpad=14)
    vmax=plane.max();vmin=plane.min()
    for i in range(10):
      for j in range(10):
        scaled=(plane[i,j]-vmin)/(vmax-vmin or 1)
        ax.text(j,i,str(plane[i,j]),ha='center',va='center',fontsize=6.0,color='white' if scaled>.6 else DARK)
fig.suptitle('Orthogonal views of M[i, j, k] = 100i + 10j + k + 1',fontsize=17,weight='bold',color=DARK,y=.985)
fig.subplots_adjust(left=.035,right=.99,bottom=.08,top=.87,wspace=.28)
fig.savefig(OUT/'matrix-planes.svg',bbox_inches='tight',pad_inches=.2)
plt.close(fig)

print('Charts updated:',*[p.name for p in OUT.glob('*.svg') if p.name!='agent-workflow.svg'])
