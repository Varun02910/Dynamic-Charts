import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def tick_control():
    if type(chdict["data"][chdict["x"]][1])==str:
        total = len(chdict["data"][chdict["x"]].unique())
        if total > 25:
                index = round(total/5)
                list = []
                tick = 0
                for i in range(total):
                    tick = tick
                    list.append(tick)
                    tick = tick+index
                    if tick >= total:
                        list.append(total-1)
                        break
                ticks = list
                plt.xticks(ticks=ticks, rotation=chdict["rotation"])

def sns_line():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; kind = chdict["type"]; hue = chdict["hue"]; col = chdict["col"]
    row = chdict["row"]; legend = chdict["legend"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]
    title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]

    sns.relplot(data=data, x=x, kind=kind, y=y, hue=hue,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def sns_scatter():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; kind = chdict["type"]; hue = chdict["hue"]; col = chdict["col"]
    row = chdict["row"]; legend = chdict["legend"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]
    title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]

    sns.relplot(data=data, x=x, y=y, kind=kind, hue=hue,
                col=col, row=row, legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def sns_bar():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; kind = chdict["type"]; hue = chdict["hue"]; col = chdict["col"]
    row = chdict["row"]; legend = chdict["legend"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]
    title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]

    sns.catplot(data=data, x=x, kind=kind, y=y, hue=hue,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def sns_hist():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; kind = chdict["type"]; hue = chdict["hue"]; col = chdict["col"]
    row = chdict["row"]; legend = chdict["legend"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]
    title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]; bins = chdict["bins"]

    sns.displot(data=data, x=x, y=y, kind=kind, hue=hue, bins=bins,
                col=col, row=row,  legend=legend, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def sns_count():
    data = chdict["data"]; x = chdict["x"]; hue = chdict["hue"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]; title = chdict["title"]; rotation = chdict["rotation"]
    sns.countplot(data=data, x=x, hue=hue, palette=palette)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    plt.xticks(rotation=rotation)

def sns_heatmap():
    data = chdict["data"]; title = chdict["title"]; rotation = chdict["rotation"]; annot = chdict["annot"]
    sns.heatmap(data.corr(), annot=annot)
    plt.title(title)
    plt.xticks(rotation=rotation)

def mat_line():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; hue = chdict["hue"]; legend = chdict["legend"]; palette = chdict["palette"]
    xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]; title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    if hue != None:
        data = data[[x, y, hue]].groupby([hue, x]).mean().reset_index()
        list1 = data[hue].unique()
        for hu in range(len(list1)):
            plt.plot(data[x].loc[data[hue] == list1[hu]],
                     data[y].loc[data[hue] == list1[hu]])
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
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def mat_scatter():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; hue = chdict["hue"]; legend = chdict["legend"]; palette = chdict["palette"]
    xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]; title = chdict["title"];xticks = chdict["xticks"];xlabels = chdict["xlabels"]
    rotation = chdict["rotation"]

    if hue != None:
        list1 = data[hue].unique()
        for hu in range(len(list1)):
            plt.scatter(data[x].loc[data[hue] == list1[hu]],
                        data[y].loc[data[hue] == list1[hu]], edgecolors="black")
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
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def mat_bar():
    data = chdict["data"]; x = chdict["x"]; y = chdict["y"]; legend = chdict["legend"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]
    ylimit = chdict["ylimit"]; title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]

    plt.bar(data[x], data[y], color=palette)
    if legend == True:
        plt.legend([y], loc=(1.1, 0))
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    if xticks==None:
        tick_control()
    else:
        plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def mat_hist():
    data = chdict["data"]; x = chdict["x"]; palette = chdict["palette"]; xlimit = chdict["xlimit"]; ylimit = chdict["ylimit"]
    title = chdict["title"]; xticks = chdict["xticks"]; xlabels = chdict["xlabels"]; rotation = chdict["rotation"]; bins = chdict["bins"]

    plt.hist(data[x], color=palette, bins=bins)
    plt.xlabel(x)
    plt.xlim(xlimit)
    plt.ylim(ylimit)
    plt.title(title)
    plt.xticks(ticks=xticks, labels=xlabels, rotation=rotation)

def mat_count():
    data = chdict["data"]; x=chdict["x"]; palette = chdict["palette"]; ylimit = chdict["ylimit"]; title = chdict["title"]; rotation = chdict["rotation"]

    if x!= None:
        count = data[x].value_counts().reset_index()
        plt.bar(count["index"],count[x], color=palette)
    else:
        count = data.count().reset_index()
        plt.bar(count["index"], count[0], color=palette)
    plt.ylabel("Count")
    plt.ylim(ylimit)
    plt.title(title)
    plt.xticks(rotation=rotation)

def mat_pie():
    data = chdict["data"]; x = chdict["x"]; legend1 = chdict["legend"]; palette = chdict["palette"]; title = chdict["title"]

    plt.pie(data[x].value_counts(), labels=data[x].value_counts().reset_index()["index"], colors=palette, autopct='%1.1f%%')
    plt.title(title)
    if legend1 == True:
        plt.legend(data[x].value_counts().reset_index()["index"],loc=(1.3, 0))
# list of parameters used in the function data, type, annot, lib, x, y, xticks, xlimit, ylimit, col, row, hue, legend, palette, xlabels, title, rotation, bins

#creating chart function depending on the type and the liberary.
def charts():
    lib = chdict["lib"]
    type = chdict["type"]
    if lib == "seaborn":
        if type == "line":sns_line()
        elif type == "scatter":sns_scatter()
        elif type == "bar":sns_bar()
        elif type == "hist":sns_hist()
        elif type == "count":sns_count()
        elif type == "heatmap":sns_heatmap()

    elif lib == "matplotlib":
        if type == "line":mat_line()
        elif type == "scatter":mat_scatter()
        elif type == "bar":mat_bar()
        elif type == "hist":mat_hist()
        elif type == "count":mat_count()
        elif type == "pie":mat_pie()
    
    
    plt.tight_layout()
    figName=input("Enter the name of the file with which you want to save:")
    plt.savefig(figName+'.png', dpi=200)
    return plt.show()

start = 10
print("Dynamic Charts generation tool:")

chdict = {"data": None}
# selecting the location of the .csv file.
for i in range(start):
    location = input("Please enter the loction of the .csv file:\n")
    try:
        chdict["data"] = pd.read_csv(location)
    except:
        print("Error: location of the data is not correct....Please check the location.")
        continue
    break

# taking input in library.
for i in range(start):
    #defining the dict for all the features.
    chdict.update({"type": None, "annot": None, "lib": None, "x": None, "y": None, "xticks": None, "xlimit": None,
                   "ylimit": None, "col": None, "row": None, "hue": None, "legend": None, "palette": None, "xlabels": None, "title": None,
                   "rotation": None, "bins": 20})
    
    chdict["lib"] = input("Please enter the library ['matplotlib', 'seaborn']:")
    
    if chdict["lib"] not in ["matplotlib", "seaborn"]:
        print("Invalid Library used.Please Enter the correct library.")
        continue
    
    for i in range(start):  # type of plot to be generated.
        chdict["type"] = input(
            "What type of chart you want to plot?\n['line','scatter','bar','hist','count','pie','heatmap']:\n")
        if chdict["type"] not in ['line', 'scatter', 'bar', 'hist', 'count', 'pie', 'heatmap']:
            print("Invalid chart type.Please use the correct type:['scatter', 'line', 'bar', 'hist', 'count', 'heatmap', 'pie']")
            continue
        else :
            break

    # test for the suitable library for the plot type:['heatmap','pie']
    if chdict["type"] == "pie" and chdict["lib"] == "seaborn":
        print(
            "type = 'pie' can't be ploted in seaborn library \n please change the library to matplotlib")
        continue
    elif chdict["type"] == "heatmap" and chdict["lib"] == "matplotlib":
        print(
            "type = 'heatmap' can't be ploted in matplotlib library \n please change the library to seaborn")
        continue

    #showing the columns present in the selected Data.
    print("Columns that are present in the selected .csv file:")
    print(list(chdict["data"].columns))
 # further feature selection.......
    for i in range(start):
        if chdict["type"] in ["line", "scatter", "bar", "hist", "count", "heatmap", "pie"] and chdict["lib"] in ["seaborn", "matplotlib"]:
            if chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist", "pie","count"] and chdict["lib"] == "matplotlib":
                # input in x parameter.
                if chdict["type"]=="count" and chdict["lib"] in ["seaborn","matplotlib"]:
                    chdict["x"] = input("\nPlease enter the name of the column to count the no. of unique values in that column.\nif you don't want this option and want no. of values in each column please type 'None': \n")
                    if chdict["x"]=="None":
                        chdict["x"]=None
                elif chdict["type"]=="pie" and chdict["lib"]=="matplotlib":
                    chdict["x"]=input("\nPlease enter the column name: \n")
                else:
                    chdict["x"] = input(
                    "\nEnter the column name you want to take on x-axis:\n")
            if chdict["type"] in ["line", "scatter", "bar", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar"] and chdict["lib"] == "matplotlib":
                # input in y parameter.
                chdict["y"] = input(
                    "\nEnter the column name you want to take on y-axis:\n")

            
            addit = input("\nDo you want to access additional features.[y,n]: ")
            for i in range(start):  # activating additional features.
                if addit == "y":
                    features = input(
                        "\nwhich feature you want to access: \n['hue','title','xlimit','ylimit','legend','xticks','xlabels','col','row','rotation','palette','annot','bins'],\n xlabels can only be selected after xticks\nIf you don't want to select any feature, Please type 'EXIT'.\n\nPlease select one feature:")
                    if features not in ['hue', 'title', 'xlimit', 'ylimit', 'legend', 'xticks', 'xlabels', 'col', 'row', 'rotation', 'palette', 'EXIT','annot','bins']:
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
                                "\nThis feature is used to put the title of the Chart,\n Please write the chart title: ")
                            print("your `title` feature has been recorded.")
                            print("Please select the another feature.")
                            if chdict["title"]=="None":
                                chdict["title"]=None
                            continue

                        # xlimit parameter
                        elif features == "xlimit" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "hist", "bar"] and chdict["lib"] == "matplotlib"):
                            print("\nFor setting the value of xlimit None. Please Enter 0 in both lower and upper limit.")
                            lower= int(input(
                                "This feature is used to limit the value of x-axis,\n Enter the lower limit of xlimit: "))
                            upper= int(input(
                                "Enter the upper limit of xlimit: "))
                            chdict["xlimit"]=(lower,upper)
                            print("your `xlimit` feature has been recorded.")
                            print("Please select the another feature.")
                            if upper==0 and lower==0:
                                chdict["xlimit"]=None
                            continue

                        # ylimit parameter
                        elif features == "ylimit" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "hist", "bar", "count"] and chdict["lib"] == "matplotlib"):
                            print("\nFor setting the value of ylimit None. Please Enter 0 in both lower and upper limit.")
                            lower= int(input(
                                "This feature is used to limit the value of y-axis,\n Enter the lower limit of ylimit: "))
                            upper= int(input(
                                "Enter the upper limit of ylimit: "))
                            chdict["ylimit"]=(lower,upper)
                            print("your `ylimit` feature has been recorded.")
                            print("Please select the another feature.")
                            if upper==0 and lower==0:
                                chdict["ylimit"]=None
                            continue

                        # xticks and xlabels parameter.
                        elif features in ["xticks", "xlabels"] and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "matplotlib"):
                            print("\nThis feature is array-like containing the list of xtick locations. Passing an empty list removes all xticks.(leave all input blank.)\nPlease enter the xticks values as list: ")
                            num=int(input("How many xtick location you want to set: "))
                            xtick=[]
                            for i in range(num):
                                loc=int(input(f"Please Enter the value of {i+1} tick location:"))
                                xtick.append(loc)
                            chdict["xticks"]=xtick
                            print(
                                "your `xticks` feature has been recorded.\nEnter the name for the xticks location in xlabels. ")
                            str=input(
                                "Do you want to enter the value of xlabels?[y,n]: ")
                            xlabel=[]
                            if str=="y":
                                print("\nThis feature is array-like containing the list of xtick locations labels.")
                                for i in range (num):
                                    leb=input(f"Please Enter the name of {i+1} tick: ")
                                    xlabel.append(leb)
                                chdict["xlabels"]=xlabel
                                print("your `xlabels` feature has been recorded.")
                                print("Please select the another feature.")
                                continue
                            elif str=="n":
                                print("Please select the another feature.")
                                continue
                            else:
                                print("Invalid text: you wrote the wrong input.\n")
                                continue
                        # col and row parameter.
                        elif features in ["col", "row"] and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn"):
                            print("\nAssigning a col or row variable creates a faceted figure with multiple subplots arranged across the columns or rows of the grid.\nif you want to left any feature blank write `None`")
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
                        elif features == "legend" and (chdict["type"] in ["line", "scatter", "bar", "hist"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar","pie"] and chdict["lib"] == "matplotlib"):
                            legend =input("\nDo you want to see legend ? ['True','False']: ")
                            if legend == "True":
                                chdict["legend"] = True
                            elif legend == "False":
                                chdict["legend"] = False
                            elif legend =="None":
                                chdict["legend"]=None
                            else:
                                print("Something Wrong: Please write the value of legend again.")
                                continue
                            print("your `legend` feature has been recorded.")
                            print("Please select the another feature.")
                            continue

                        # rotation parameter
                        elif features == "rotation" and (chdict["type"] in ["line", "scatter", "bar", "hist", "count", "heatmap"] and chdict["lib"] == "seaborn" or chdict["type"] in ["line", "scatter", "bar", "hist", "count"] and chdict["lib"] == "matplotlib"):
                            chdict["rotation"] = int(input(
                                "\nBy what angle you want to rotate the labels of xaxis. \n Please enter the angle in degree: "))
                            print("your `rotation` feature has been recorded.")
                            print("Please select the another feature:")
                            if chdict["rotation"]=="None":
                                chdict["rotation"]=None
                            continue
                        # annot parameter
                        elif features == "annot" and chdict["type"] == "heatmap" and chdict["lib"] == "seaborn":
                            annot = input(
                                "\nDo you want to see values of each correlation in heatmap ? ['True','False']: ")
                            if annot == "True":
                                chdict["annot"] = True
                            elif annot == "False":
                                chdict["annot"] = False
                            elif chdict["annot"]=="None":
                                chdict["annot"]=None
                            else:
                                print("Something Wrong: Please write the value of annot again.")
                                continue
                            print("your `annot` feature has been recorded.")
                            print("Please select the another feature.")
                            
                            continue
                        # bins parameter
                        elif features == "bins" and chdict["type"] in ["hist"] and chdict["lib"] in ["seaborn", "matplotlib"]:
                            chdict["bins"] = int(
                                input("\nno. of bins you want in histogram plot:"))
                            print("your `bins` feature has been recorded.")
                            print("Please select the another feature:")
                            if chdict["bins"]=="None":
                                chdict["bins"]=None
                            continue
                        # palette parameter
                        elif features == "palette" and chdict["type"] in ["line", "scatter", "bar", "hist", "count", "pie"] and chdict["lib"] in ["seaborn", "matplotlib"]:
                            palette = input(
                                "\nEnter the color palette,\n---You can use colour name in this.---\nYou may also use ['tab10','deep','pastel','muted','bright','colorblind','dark','hls','husl','Set2','Paired','rocket']:\n")
                            if palette in ['tab10','deep','pastel','muted','bright','colorblind','dark','hls','husl','Set2','Paired','rocket']:
                                chdict["palette"] = sns.color_palette(palette)
                                print("your `palette` feature has been recorded.")
                            elif palette in ['tab10','deep','pastel','muted','bright','colorblind','dark','hls','husl','Set2','Paired','rocket'] and chdict["type"] in ["scatter","line"] and chdict["lib"]=="matplotlib":
                                print("\n'Scatter' plot in'matplotlib' liberary does not support this list palette-\n['tab10','deep','pastel','muted','bright','colorblind','dark','hls','husl','Set2','Paired','rocket']\nPlease enter any simple colour again.....")
                            elif chdict["palette"]=="None":
                                chdict["palette"]=None
                                print("your `palette` feature has been recorded.")
                            else :
                                chdict["palette"]=palette
                                print("your `palette` feature has been recorded.")
                            print("Please select the another feature.")
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
    print("Your plot is successfully generated and saved in your current folder.")
    repeate = input("Do you want to make another plot?[y,n]:")
    if repeate == "y":continue
    elif repeate == "n":break
    else:break
