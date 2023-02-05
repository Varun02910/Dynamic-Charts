'''FUNCTION TO GENERATE DYNAMIC_CHARTS '''
import matplotlib.pyplot as plt
import seaborn as sns

def charts(data=None, type: str = "scatter", annot=None, lib: str = "seaborn", x=None, y=None, xticks=None, xlimit=None, 
           ylimit=None, col: int = None, row: int = None, hue=None, legend=None, palette=None,  xlabels=None,
            title=None, rotation=0, bins:int =None):
    '''
    charts(data=None, type: str = "scatter", annot=None, lib: str = "seaborn", x=None, y=None, xticks=None, xlimit=None, 
           ylimit=None, col: int = None, row: int = None, hue=None, legend=None, palette=None,  xlabels=None,
            title=None, rotation=0, bins:int =None)

    This `charts` function is used to do the simple visualization on a dataset. 
    We can make chart types like ['line', 'scatter', 'bar', 'hist', 'pie', 'heatmap', 'count'] using libraries like ['seaborn', 'matplotlib'].
    we have a multiple parameter like `hue`, `col`, `row` in seaborn to do more better visulization.   

    the `lib` parameter selects the library to be used:

    - : (..`lib = "seaborn",`); the default
    - : (..`lib = "matplotlib",`) 

    The ``type`` parameter selects the underlying axes-level
    function to use:
    
    - :func:`scatterplot` (with ``type="scatter"``; the default)
    - :func:`lineplot` (with ``type="line"``)
    - :func:`lineplot` (with ``type="pie"``) ; can only be used with matplotlib libraray.
    - :func:`lineplot` (with ``type="bar"``)
    - :func:`lineplot` (with ``type="heatmap"``) ; can only be used with seaborn libraray.
    - :func:`lineplot` (with ``type="hist"``)
    - :func:`lineplot` (with ``type="count"``)

    Parameters
    ----------
    x, y : vectors or keys in ``data``
        Variables that specify positions on the x and y axes.
    hue : vector or key in ``data`` ; Can only be used with Seaborn library.
        Grouping variable that will produce elements with different colors.
        Can be either categorical or numeric, although color mapping will
        behave differently in latter case.
    data : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence
        Input data structure. Either a long-form collection of vectors that can be
        assigned to named variables or a wide-form dataset that will be internally
        reshaped.
    row, col : vectors or keys in ``data``; Can only be used with Seaborn library.
        Variables that define subsets to plot on different facets.
    annot : fill the values of correlation in `heatmap`.
    lib : passing the name of the library i.e. ["seaborn" ; Default,"matplotlib"] 
    xticks : This parameter is the list of xtick locations. and an optional parameter. If an empty list is 
          passed as an argument then it will removes all xticks.
    xlimit ,ylimit : helps in limiting the values of xaxis and yaxis.
    legend : In seaborn;["auto", "brief", "full", or False
        How to draw the legend. If "brief", numeric ``hue`` and ``size``
        variables will be represented with a sample of evenly spaced values.
        If "full", every group will get an entry in the legend. If "auto",
        choose between brief or full representation based on number of levels.
        If ``False``, no legend data is added and no legend is drawn.]
             In matplotlib;[This parameter is the list of labels to show next to the artists.]
    palette: used for changing the color of the graph.
    xlabels : This parameter is the list of name of the xtick location.
    title : Used to give the Title of the graph.
    rotation : Used to rotate the name on xaxis by a certain degree.
    bins : used to set the bin size in histogram plot.

    '''
    
    def sns_line(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
               palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        
        sns.relplot(data=data, x=x, kind=kind, y=y, hue=hue,col=col, row=row,  legend=legend, palette=palette)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)
    
    def sns_scatter(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
                    palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        sns.relplot(data=data, x=x, y=y, kind=kind, hue=hue,
                    col=col, row=row, legend=legend,palette=palette)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)

    def sns_bar(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
                    palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        sns.catplot(data=data, x=x, kind=kind, y=y, hue=hue,col=col, row=row,  legend=legend, palette=palette)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)
    
    def sns_hist(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,bins=bins,
                 palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        sns.displot(data=data, x=x, y=y,kind=kind, hue=hue, bins=bins,
                        col=col, row=row,  legend=legend, palette=palette)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)

    def sns_count(data=data, x=x, y=y, hue=hue,palette=palette,xlimit=xlimit,ylimit=ylimit,
                  title=title,rotation=rotation):
        sns.countplot(data=data, x=x, y=y, hue=hue, palette=palette)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.xticks(rotation=rotation)
    
    def sns_heatmap(data=data, annot=annot,title=title,rotation=rotation):
        sns.heatmap(data.corr(), annot=annot)
        plt.title(title)
        plt.xticks(rotation=rotation)

    def mat_line(data=data, x=x, y=y, hue=hue,  legend=legend,
                 palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        if hue != None:
            data = data[[x, y, hue]].groupby([x, hue]).mean().reset_index()
            list1 = data[hue].unique()
            for hu in range(len(list1)):
                plt.plot(data[x].loc[data[hue] == list1[hu]],
                         data[y].loc[data[hue] == list1[hu]], color=palette)
                plt.legend(data[hue], title=hue)

        else:
            plt.plot(data[x], data[y], color=palette)
            
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.legend(legend)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)

    def mat_scatter(data=data, x=x, y=y, hue=hue,  legend=legend,
                 palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        if hue != None:
            data = data[[x, y, hue]].groupby([x, hue]).mean().reset_index()
            list1 = data[hue].unique()
            for hu in range(len(list1)):
                plt.scatter(data[x].loc[data[hue] == list1[hu]],
                         data[y].loc[data[hue] == list1[hu]], color=palette)
                plt.legend(data[hue], title=hue)

        else:
            plt.scatter(data[x], data[y], color=palette)
            
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.legend(legend)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)

    def mat_bar(data=data, x=x, y=y,   legend=legend,palette=palette,
                xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        
        plt.bar(data[x], data[y], color=palette) 
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.legend(legend)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)

    def mat_hist(data=data, x=x,   legend=legend,palette=palette,bins=bins,
                xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation):
        
        plt.hist(data[x], color=palette,bins=bins) 
        plt.xlabel(x)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        plt.legend(legend)
        plt.xticks(ticks=ticks, labels=labels, rotation=rotation)
    
    def mat_count(data=data,   legend=legend,palette=palette,
                  ylimit=ylimit,title=title,rotation=rotation):
        
        count = data.count().reset_index()
        plt.bar(count["index"],count[0],color = palette)
        plt.ylabel("Count")
        plt.ylim(ylimit)
        plt.title(title)
        plt.legend(legend)
        plt.xticks( rotation=rotation)
    
    def mat_hist(data=data,palette=palette,title=title,legend=None):
        
        plt.pie(data.value_counts(), labels=data.value_counts().reset_index()["index"], colors=palette)
        plt.title(title)
        plt.legend(legend)

    if lib=="seaborn" :
        if type == "line":
           sns_line(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
                    palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)
           
        elif type == "scatter":
            sns_scatter(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
                        palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)

        elif type == "bar":
            sns_bar(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,
                    palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)

        elif type == "hist":
            sns_hist(data=data, x=x, kind=type, y=y, hue=hue,col=col, row=row,  legend=legend,bins=bins,
                     palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)

        elif type == "count":
            sns_count(data=data, x=x, y=y, hue=hue,palette=palette,xlimit=xlimit,ylimit=ylimit,
                      title=title,rotation=rotation)
 
        elif type == "heatmap":
            sns_heatmap(data=data, annot=annot,title=title,rotation=rotation)
            
        elif type == "pie":
            raise TypeError("\n `Error` type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")
        
        else :
            raise TypeError("Invalid type:",type ,"\n Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'heatmap']")

    elif lib == "matplotlib":

        if type == "line":
            mat_line(data=data, x=x, y=y, hue=hue,  legend=legend,palette=palette,xlimit=xlimit,
                     ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)
            
        elif type == "scatter":
            mat_scatter(data=data, x=x, y=y, hue=hue,  legend=legend,
                 palette=palette,xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)

        elif type == "bar":
            mat_bar(data=data, x=x, y=y,   legend=legend,palette=palette,
                xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)
            
        elif type == "hist":
            mat_hist(data=data, x=x,   legend=legend,palette=palette,bins=bins,
                xlimit=xlimit,ylimit=ylimit,title=title,ticks=xticks,labels=xlabels,rotation=rotation)
            
        elif type == "count":
            mat_count(data=data,   legend=legend,palette=palette,
                      ylimit=ylimit,title=title,rotation=rotation)
                
        elif type == "heatmap":
            raise TypeError("type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")
        
        elif type == "pie":
            mat_hist(data=data,palette=palette,title=title,legend=None)

        else:
            raise TypeError("Invalid type:",type ,"\n Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'pie']")

    else:
        raise TypeError('Invalid Liberary used. Please use lib:["seaborn","matplotlib"]')
    
    plt.savefig('Plot.png', dpi = 150) 
    return plt.show()