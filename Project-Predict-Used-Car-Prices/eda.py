#---------------------------------------------------------------------#
#Program Name: eda.py
#Description: Exploratory Analysis
#---------------------------------------------------------------------#
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def pair_plot(auto):

    print("\n\n Pair Plot")
    print("#-----------------------------------------------------------#")
    fig_name = 'pair_plot.png'
    fig_name = 'charts/'+fig_name
    sns.pairplot(auto)
    plt.savefig(fig_name)
    plt.show()

def bar_chart(column, col_name):
    print ('\n\n Value Counts and Bar Chart for ' + col_name)
    print("#-----------------------------------------------------------#")
    res = column.value_counts(dropna=False)
    print (res)
    fig_name = 'bar_plot_'+col_name+'.png'
    fig_name = 'charts/'+fig_name
    x = res.index
    y = res.values
    plt.bar(x,y, color='blue')
    plt.title('Bar Chart for '+col_name)
    plt.savefig(fig_name)
    plt.show()

def heatmap(data):
    corr = data.corr()
    print(corr)
    print ("#-----------------Printing Heatmap-------------------------#")
    sns.heatmap(corr, annot = True)
    plt.title('Heatmap')
    fig_name = 'charts/Heatmap.png'
    plt.savefig(fig_name)
    plt.show()
    print("#-----------------List of the most influencing features for the price-------------------------#")
    print (corr.loc[:, 'price'].abs().sort_values(ascending=False)[1:])