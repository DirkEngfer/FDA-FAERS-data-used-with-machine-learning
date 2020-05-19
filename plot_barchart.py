import matplotlib.pyplot as plt
import numpy as np

def make_barchart(figname=None, figwidth=None, figheight=None, adjust_bottom=None, title=None, ticklabels=None, data1=None, data2=None, label1=None, label2=None, c1=None, c2=None):
    locs = np.arange(0, len(data1))
    width=0.3
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(figwidth,figheight))
    ax.bar(locs, data1, color=c1,width=width, label=label1)
    ax.bar(locs+width, data2, color=c2, width=width, label=label2)
    plt.title(title)
    plt.legend([label1, label2])
    plt.xticks(locs, ticklabels, rotation=90)
    plt.ylabel('%')
    #plt.margins(0.2)
    fig.subplots_adjust(bottom=adjust_bottom)
    fig.savefig(figname)

# barchart over 3 groups
def make_barchart3(figname=None, figwidth=None, figheight=None, adjust_bottom=None, title=None, ticklabels=None, data1=None, data2=None, data3=None, label1=None, label2=None, label3=None, c1=None, c2=None, c3=None):
    locs = np.arange(0, len(data1))
    width=0.2
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(figwidth,figheight))
    ax.bar(locs, data1, color=c1,width=width, label=label1)
    ax.bar(locs+width, data2, color=c2, width=width, label=label2)
    ax.bar(locs+2*width, data3, color=c3, width=width, label=label3)
    plt.title(title)
    plt.legend([label1, label2, label3])
    plt.xticks(locs, ticklabels, rotation=90)
    plt.ylabel('%')
    #plt.margins(0.2)
    fig.subplots_adjust(bottom=adjust_bottom)
    fig.savefig(figname)
