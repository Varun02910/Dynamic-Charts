import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

chdict = {"data": None, "type": None, "annot": None, "lib": None, "x": None, "y": None, "xticks": None, "xlimit": None,
          "ylimit": None, "col": None, "row": None, "hue": None, "legend": None, "palette": None, "xlabels": None, "title": None,
          "rotation": None, "bins": None}


def sns_line():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    kind = chdict["type"]
    hue = chdict["hue"]
    col = chdict["col"]
    row = chdict["row"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    sns.relplot(data=data, x=x, kind=kind, y=y, hue=hue,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def sns_scatter():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    kind = chdict["type"]
    hue = chdict["hue"]
    col = chdict["col"]
    row = chdict["row"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    sns.relplot(data=data, x=x, y=y, kind=kind, hue=hue,
                col=col, row=row, legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def sns_bar():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    kind = chdict["type"]
    hue = chdict["hue"]
    col = chdict["col"]
    row = chdict["row"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    sns.catplot(data=data, x=x, kind=kind, y=y, hue=hue,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def sns_hist():
    data = chdict["data"]
    x = chdict["x"]
    kind = chdict["type"]
    y = chdict["y"]
    hue = chdict["hue"]
    col = chdict["col"]
    row = chdict["row"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]
    bins = chdict["bins"]

    sns.displot(data=data, x=x, y=y, kind=kind, hue=hue, bins=bins,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def sns_count():
    data = chdict["data"]
    x = chdict["x"]
    hue = chdict["hue"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    rotation = chdict["rotation"]

    sns.countplot(data=data, x=x, hue=hue, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    plt.xticks(rotation=rotation)

def sns_heatmap():
    data = chdict["data"]
    title = chdict["title"]
    rotation = chdict["rotation"]
    annot = chdict["annot"]

    sns.heatmap(data.corr(), annot=annot)
    plt.title(title)
    plt.xticks(rotation=rotation)


def mat_line():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    hue = chdict["hue"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    if hue != None:
        data = data[[x, y, hue]].groupby([hue, x]).mean().reset_index()
        list1 = data[hue].unique()
        for hu in range(len(list1)):
            plt.plot(data[x].loc[data[hue] == list1[hu]],
                     data[y].loc[data[hue] == list1[hu]], color=palette)
            if legend == True:
                plt.legend(list1, title=hue, loc=(1.1, 0))

    else:
        data = data[[x, y]].groupby(x).mean().reset_index()
        plt.plot(data[x], data[y], color=palette)
        if legend == True:
            plt.legend([y], loc=(1.1, 0))
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
        index = round(total/5)
        list = []
        tick = 0
        for i in range(total):
            tick = tick
            list.append(tick)
            tick = tick+index
            if tick > total:
                break
        ticks = list
        plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def mat_scatter():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    hue = chdict["hue"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    if hue != None:
        list1 = data[hue].unique()
        for hu in range(len(list1)):
            plt.scatter(data[x].loc[data[hue] == list1[hu]],
                        data[y].loc[data[hue] == list1[hu]], color=palette)
            if legend == True:
                plt.legend(list1, title=hue, loc=(1.1, 0))

    else:
        plt.scatter(data[x], data[y], color=palette, edgecolors="black")
        if legend == True:
            plt.legend([y], loc=(1.1, 0))
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xlim(xlimit)
        plt.ylim(ylimit)
        plt.title(title)
        total = len(data[x].unique())
        if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def mat_bar():
    data = chdict["data"]
    x = chdict["x"]
    y = chdict["y"]
    legend = chdict["legend"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    plt.bar(data[x], data[y], color=palette)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    if legend == True:
        plt.legend([y], loc=(1.1, 0))

    total = len(data[x].unique())
    if total > 25:
        index = round(total/5)
        list = []
        tick = 0
        for i in range(total):
            tick = tick
            list.append(tick)
            tick = tick+index
            if tick > total:
                break
        ticks = list
        plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def mat_hist():
    data = chdict["data"]
    x = chdict["x"]
    palette = chdict["palette"]
    xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    xticks = chdict["xticks"]
    xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]
    bins = chdict["bins"]

    plt.hist(data[x], color=palette, bins=bins)
    plt.xlabel(x)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    total = len(data[x].unique())
    if total > 25:
            index = round(total/5)
            list = []
            tick = 0
            for i in range(total):
                tick = tick
                list.append(tick)
                tick = tick+index
                if tick > total:
                    break
            ticks = list
            plt.xticks(ticks=ticks, rotation=rotation)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)


def mat_count():  # for count plot only DataFrame is needed.
    data = chdict["data"]
    palette = chdict["palette"]
    ylimit = chdict["ylimit"]
    title = chdict["title"]
    rotation = chdict["rotation"]

    count = data.count().reset_index()
    plt.bar(count["index"], count[0], color=palette)
    plt.ylabel("Count")
    plt.ylim(ylimit)
    plt.title(title)
    plt.xticks(rotation=rotation)


def mat_pie():
    data = chdict["data"]
    x = chdict["x"]
    legend = chdict["legend"],
    palette = chdict["palette"]
    title = chdict["title"]

    plt.pie(data[x].value_counts(), labels=data[x].value_counts().reset_index()["index"], colors=palette)
    plt.title(title)
    if legend == True:
        plt.legend(data.value_counts().reset_index()
                   ["index"], loc=(1.5, 0))
# list of parameters used in the function data, type, annot, lib, x, y, xticks, xlimit, ylimit, col, row, hue, legend, palette, xlabels, title, rotation, bins


def charts():
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
    lib = chdict["lib"]
    type = chdict["type"]
    if lib == "seaborn":
        if type == "line":
            sns_line()

        elif type == "scatter":
            sns_scatter()

        elif type == "bar":
            sns_bar()

        elif type == "hist":
            sns_hist()

        elif type == "count":
            sns_count()

        elif type == "heatmap":
            sns_heatmap()

        elif type == "pie":
            raise TypeError(
                "type = 'pie' can't be ploted in seaborn library \n please change the library to matplotlib")

        else:
            raise TypeError(
                " Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'heatmap']")

    elif lib == "matplotlib":

        if type == "line":
            mat_line()

        elif type == "scatter":
            mat_scatter()

        elif type == "bar":
            mat_bar()

        elif type == "hist":
            mat_hist()

        elif type == "count":
            mat_count()

        elif type == "heatmap":
            raise TypeError(
                "type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")

        elif type == "pie":
            mat_pie()

        else:
            raise TypeError(
                "Invalid type, Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'pie']")

    else:
        raise TypeError(
            'Invalid Liberary used. Please use lib:["seaborn","matplotlib"]')

    plt.savefig('Plot.png', dpi=250)
    return plt.show()


start = 10
l = 0
print("Dynamic Charts generation tool:")
# selecting the location of the .csv file.
for i in range(start):
    location = input("Please enter the loction of the .csv file:\n")
    try:
        chdict["data"] = pd.read_csv(location)
    except:
        print("Error: location of the data is not correct....Please check the location.")
        continue
    break


for i in range(start):  # taking input in library.
    chdict["lib"] = input(
        "Please enter the library ['matplotlib', 'seaborn']:")
    try:
        if chdict["lib"] not in ["matplotlib", "seaborn"]:
            raise TypeError(
                'Invalid Library used. Please use lib:["seaborn","matplotlib"]')
    except:
        print("Invalid Library used.Please Enter the correct library.")
        continue

    for i in range(start):  # type of plot to be generated.
        chdict["type"] = input(
            "What type of chart you want to plot?\n['line','scatter','bar','hist','count','pie','heatmap']:\n")
        try:
            if chdict["type"] not in ['line', 'scatter', 'bar', 'hist', 'count', 'pie', 'heatmap']:
                raise TypeError(
                    " Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'heatmap','pie']")
        except:
            print(
                "Invalid chart type.Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'heatmap', 'pie']")
            continue
        break

    try:  # test for the suitable library for the plot type:['heatmap','pie']
        if chdict["type"] == "pie" and chdict["lib"] == "seaborn":
            raise TypeError(
                "type = 'pie' can't be ploted in seaborn library \n please change the library to matplotlib")
        elif chdict["type"] == "heatmap" and chdict["lib"] == "matplotlib":
            raise TypeError(
                "type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")
    except:
        if chdict["type"] == "pie" and chdict["lib"] == "seaborn":
            print(
                "type = 'pie' can't be ploted in seaborn library \n please change the library to matplotlib")
            continue
        elif chdict["type"] == "heatmap" and chdict["lib"] == "matplotlib":
            print(
                "type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")
            continue


# further feature selection.......
    for i in range(start):
        if chdict["type"] in ["line", "scatter", "bar", "hist", "count", "heatmap", "pie"] and chdict["lib"] in ["seaborn", "matplotlib"]:
            if chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist", "pie"] and chdict["lib"] == "matplotlib":
                # input in x parameter.
                if chdict["type"]=="count" and chdict["lib"]=="seaborn":
                    chdict["x"] = input("\n Please enter the name of the column to count the no. of unique values in that column.\n if you don't want this option and want no. of values in each column please type 'None'")
                    if chdict["x"]=="None":
                        chdict["x"]=None

                else:
                    chdict["x"] = input(
                    "\nEnter the column name you want to take on x-axis:\n")
            if chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar"] and chdict["lib"] == "matplotlib":
                # input in y parameter.
                chdict["y"] = input(
                    "\nEnter the column name you want to take on y-axis:\n")

            
            addit = input("\nDo you want to access additional features.[y,n]: ")
            for i in range(start):  # activating additional features.
                if addit == "y":
                    features = input(
                        "\nwhich feature you want to access: \n['hue','title','xlimit','ylimit','legend','xticks','xlabels','col','row','rotation','palette','annot','bins'],\n xlabels can only be selected after xticks\nIf you don't want to select any feature, Please type 'EXIT'.\n\nPlease select one feature:")
                    if features not in ['hue', 'title', 'xlimit', 'ylimit', 'legend', 'xticks', 'xlabels', 'col', 'row', 'rotation', 'palette', 'EXIT','annot','bins']:
                        try:
                            raise TypeError("Invalid feature selected.")
                        except:
                            print("Invalid feature selected.")
                            continue
                    else:
                        # hue parameter
                        if features == "hue" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter"] and chdict["lib"] == "matplotlib"):
                            chdict["hue"] = input(
                                "\nThis feature is used to determine which column in the DataFrame is used as colour encoding.\n please enter the 3rd column: ")
                            print("your `hue` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["hue"]=="None":
                                chdict["hue"]=None
                            continue
                        # title parameter
                        elif features == "title" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count", "heatmap"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist", "count", "pie"] and chdict["lib"] == "matplotlib"):
                            chdict["title"] = input(
                                "This feature is used to put the title of the Chart,\n Please write the chart title: ")
                            print("your `title` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["title"]=="None":
                                chdict["title"]=None
                            continue
                        # xlimit parameter
                        elif features == "xlimit" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "hist", "bar"] and chdict["lib"] == "matplotlib"):
                            chdict["xlimit"] = tuple(input(
                                "This feature is used to limit the value of x-axis:\n Put the xlimit as (<upper limit>,<lower limit>): "))
                            print("your `xlimit` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["xlimit"]=="None":
                                chdict["xlimit"]=None
                            continue
                        # ylimit parameter
                        elif features == "ylimit" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "hist", "bar", "count"] and chdict["lib"] == "matplotlib"):
                            chdict["ylimit"] = tuple(input(
                                "This feature is used to limit the value of y-axis:\n Put the ylimit as (<upper limit>,<lower limit>): "))
                            print("your `ylimit` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["ylimit"]=="None":
                                chdict["ylimit"]=None
                            continue
                        # xticks and xlabels parameter.
                        elif features in ["xticks", "xlabels"] and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "matplotlib"):
                            chdict["xticks"] = list(input(
                                "This feature is array-like containing the list of xtick locations. Passing an empty list removes all xticks.\nPlease enter the xticks values as list: "))
                            print(
                                "your `xticks` feature has been recorded.\nEnter name for the xticks location in xlabels. ")
                            print(
                                "Enter xlabels values-- (if you don't want to enter any value enter 'None')")
                            chdict["xlabels"] = list(input(
                                "This feature is array-like containing the list of xtick locations labels. Passing an empty list removes all xlabels.\nPlease enter the xlabels values as list: "))
                            print("your `xlabels` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["xticks"]=="None":
                                chdict["xticks"]=None
                            if chdict["xlabels"]=="None":
                                chdict["xlabels"]=None
                            continue
                        # col and row parameter.
                        elif features in ["col", "row"] and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn"):
                            print("Assigning a col or row variable creates a faceted figure with multiple subplots arranged across the columns or rows of the grid.\nif you want to left any feature blank write `None`")
                            chdict["col"] = input(
                                "Enter the column name in col: ")
                            chdict["row"] = input(
                                "Enter the column name in row: ")
                            print("your `col` or `row` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["col"]=="None":
                                chdict["col"]=None
                            if chdict["row"]=="None":
                                chdict["row"]=None
                            continue
                        # legend parameter
                        elif features == "legend" and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar"] and chdict["lib"] == "matplotlib"):
                            legend = input(
                                "do you want to see legend ? ['True','False']: ")
                            if legend == "True":
                                chdict["legend"] = True
                            elif legend == "False":
                                chdict["legend"] = False
                            else:
                                try:
                                    raise TypeError(
                                        "Something Wrong: Please write the value of legend again.")
                                except:
                                    print(
                                        "Something Wrong: Please write the value of legend again.")
                                    continue
                            print("your `legend` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["legend"]=="None":
                                chdict["legend"]=None
                            continue
                        # rotation parameter
                        elif features == "rotation" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count", "heatmap"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "matplotlib"):
                            chdict["rotation"] = int(input(
                                "By what angle you want to rotate the labels of xaxis. \n Please enter the angle in degree: "))
                            print("your `rotation` feature has been recorded.")
                            print("Please select the another feature:")
                            if chdict["rotation"]=="None":
                                chdict["rotation"]=None
                            continue
                        # annot parameter
                        elif features == "annot" and chdict["type"] == "heatmap" and chdict["lib"] == "seaborn":
                            annot = input(
                                "do you want to see values of each correlation in heatmap ? ['True','False']: ")
                            if annot == "True":
                                chdict["annot"] = True
                            elif annot == "False":
                                chdict["annot"] = False
                            else:
                                try:
                                    raise TypeError(
                                        "Something Wrong: Please write the value of annot again.")
                                except:
                                    print(
                                        "Something Wrong: Please write the value of annot again.")
                                    continue
                            print("your `annot` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["annot"]=="None":
                                chdict["annot"]=None
                            continue
                        # bins parameter
                        elif features == "bins" and chdict["type"] in ["hist"] and chdict["lib"] in ["seaborn", "matplotlib"]:
                            chdict["bins"] = int(
                                input("no. of bins you want in histogram plot:"))
                            print("your `bins` feature has been recorded.")
                            print("Please select the another feature:")
                            if chdict["bins"]=="None":
                                chdict["bins"]=None
                            continue
                        # palette parameter
                        elif features == "palette" and chdict["type"] in ["line", "scatter", "bar", "hist", "count", "pie"] and chdict["lib"] in ["seaborn", "matplotlib"]:
                            palette = input(
                                "Enter the color palette,\n You can use colour name in this.\nYou may also use ['tab10','deep','pastel','muted','bright','colorblind','dark','hls','husl','Set2','Paired','rocket']:\n")
                            chdict["palette"] = sns.color_palette(palette)
                            print("your `palette` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["palette"]=="None":
                                chdict["palette"]=None
                            continue
                        # exiting the feature option and start generating plot
                        elif features == "EXIT":
                            print("Your chart is generating please wait...")
                            break
                        else:
                            print("please choose the correct parameter for respective chart type=" +
                                  chdict["type"]+" and library="+chdict["lib"]+
                                  "\n Maybe, the selected feature that you have selected is not supported by the chart type= "+chdict["type"])
                            continue

                elif addit == "n":
                    print("Your chart is generating please wait...")
                    break
                else:
                    print(
                        "Invalid Input: please enter the correct input-[y,n]")
                    continue
        break
    charts()
    print("Your plot is successfully generated and saved in your corrent folder.")
    repeate = input("Do you want to make another plot?[y,n]:")
    if repeate == "y":
        continue
    elif repeate == "n":
        break
    else:
        break