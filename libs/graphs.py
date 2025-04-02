from ast import List
from statistics import correlation
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DataVisualizer:
    """
    A class for visualizing data using various plots.

    This class provides methods for generating different types of plots
    to visualize relationships and distributions in the data.

    Attributes:
    - None

    Methods:
    - create_heatmap: Generate a heatmap to visualize the correlation matrix.
    - create_histogram: Generate a histogram to visualize the distribution of all numeric variable.
    - create_barplot: Generate a bar plot to visualize relationships between categorical and numeric variables.
    - create_scatterplot: Generate a scatter plot to visualize relationships between two numeric variables.
    - create_boxplot: Generate a box plot to visualize the distribution of a numeric variable across different categories.
    - create_violinplot: Generate a violin plot to visualize the distribution of a numeric variable across different categories.
    """

    def __init__(self, dataframe: pd.DataFrame):

        self.numeric_df = dataframe.select_dtypes(include=['int64', 'float64'])
        print("I am working on it")

    
    def create_heatmap(self,df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate a heatmap to visualize the correlation matrix of numeric features in the DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame containing numeric features.

        Returns:
        - correlation_matrix (pd.DataFrame): The correlation matrix computed from the numeric features.

        This function calculates the correlation matrix of the numeric features in the DataFrame 
        and visualizes it as a heatmap using Seaborn and Matplotlib. The correlation matrix 
        quantifies the pairwise relationships between the features, indicating how strongly 
        and in what direction they are correlated. 

        The heatmap provides a visual representation of the correlation matrix, where each cell 
        color represents the strength and direction of the correlation. Positive correlations 
        are indicated by warmer colors (shades of red), while negative correlations are shown 
        with cooler colors (shades of blue). The intensity of the color reflects the magnitude 
        of the correlation coefficient.

        - The 'annot' parameter adds numerical annotations to each cell, displaying the correlation
        coefficients.
        - The 'cmap' parameter specifies the color palette used for the heatmap.
        - The 'fmt' parameter formats the annotation text to two decimal places.
        - The 'vmin' and 'vmax' parameters set the lower and upper bounds of the color scale.
        - The 'linewidths' parameter controls the width of the lines separating each cell.

        Finally, the correlation matrix is returned for further analysis or interpretation.
        """
        
        correlation_matrix = self.numeric_df.corr()
        plt.figure(figsize=(10, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, linewidths=0.5)
        plt.title("Correlation Matrix")
        plt.show()
        return correlation_matrix


    def create_histplot(self, df: pd.DataFrame) -> None:
        """
        Create histogram plots for numeric columns in the DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data to be plotted.

        Returns:
        - None

        This method generates histogram plots for each numeric column in the DataFrame.
        For each numeric column, a histogram is created using Seaborn's histplot function.
        The histogram displays the distribution of values for that particular column.
        The 'kde' parameter is set to True to overlay a kernel density estimate on the histogram.
        Each histogram is displayed individually with a title indicating the column name, 
        x-axis labeled with the column name, and y-axis labeled as 'frequency'.
        """
        for col in self.numeric_df:
            plt.figure(figsize=(2,2))
            sns.histplot(data=df, x = col, kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel("frequency")
            plt.show()
        


    def create_barplot(self,df: pd.DataFrame, x_label: str, y_label: str ,title_label:  str,  hue_label:str = None, labels_hue: List = None ) -> None:
        """
        Create a bar plot using Seaborn.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data to be plotted.
        - x_label (str): The label for the x-axis.
        - y_label (str): The label for the y-axis.
        - title_label (str): The title of the plot.
        - hue_label (str, optional): The column in the DataFrame to use for color encoding (default is None).
        - labels_hue (List[str], optional): Labels for the hue categories (default is None).

        Returns:
        - None: The function displays the plot but does not return any value.

        This function generates a bar plot using Seaborn to visualize the relationship between 
        two variables in the DataFrame. It allows for both basic and grouped bar plots based on 
        the presence of the 'hue_label' parameter.

        - The 'sns.set_style("whitegrid")' statement sets the background style for the plot.
        - The 'plt.figure(figsize=(10, 10))' statement specifies the size of the plot figure.
        - Depending on whether 'hue_label' is provided:
        - If 'hue_label' is None, a basic bar plot is created with one variable plotted against 
            the other using 'sns.barplot'.
        - If 'hue_label' is not None, a grouped bar plot is created, with the bars grouped 
            according to the values in the 'hue_label' column. In this case, the 'labels_hue' 
            parameter can be used to provide custom labels for the hue categories.
        - The 'title_label', 'x_label', and 'y_label' parameters are used to set the title, x-axis 
        label, and y-axis label of the plot, respectively.
        - If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot 
        to indicate the categories represented by different colors.

        The function displays the plot using 'plt.show()' and does not return any value.
        """

        sns.set_style("whitegrid")
        plt.figure(figsize=(10,10))

        if  hue_label is None:
            sns.barplot(data =df, y = y_label, x= x_label)
        else:
            sns.barplot(data =df, y = y_label, x= x_label, hue = hue_label, errorbar = None)

        plt.title(title_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        if  hue_label is not None and labels_hue is not None:
            plt.legend(title = 'Emplyement Status', loc = 'upper right', labels=labels_hue)

        plt.show()



    def create_scatterplot(self,df: pd.DataFrame, x_label: str, y_label: str, title_label: str, hue_label: str = None, labels_hue: List = None) -> None:
        """
        Create a scatter plot using Seaborn.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data to be plotted.
        - x_label (str): The label for the x-axis.
        - y_label (str): The label for the y-axis.
        - title_label (str): The title of the plot.
        - hue_label (str, optional): The column in the DataFrame to use for color encoding.
        - labels_hue (List[str], optional): Labels for the hue categories.

        Returns:
        - None: The function displays the plot but does not return any value.

        This function generates a scatter plot using Seaborn to visualize the relationship 
        between two variables in the DataFrame. It allows for both basic and grouped scatter plots 
        based on the presence of the 'hue_label' parameter.

        - The 'sns.set_style("whitegrid")' statement sets the background style for the plot.
        - The 'plt.figure(figsize=(10, 10))' statement specifies the size of the plot figure.
        - Depending on whether 'hue_label' is provided:
        - If 'hue_label' is None, a basic scatter plot is created with one variable plotted against 
            the other using 'sns.scatterplot'.
        - If 'hue_label' is not None, a grouped scatter plot is created, with the points colored 
            according to the values in the 'hue_label' column. In this case, the 'labels_hue' 
            parameter can be used to provide custom labels for the hue categories.
        - The 'title_label', 'x_label', and 'y_label' parameters are used to set the title, x-axis 
        label, and y-axis label of the plot, respectively.
        - If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot 
        to indicate the categories represented by different colors.

        The function displays the plot using 'plt.show()' and does not return any value.
        """

        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 10))

        if  hue_label is None:
            sns.scatterplot(data =df, y = y_label, x= x_label)
        else:
            sns.scatterplot(data =df, y = y_label, x= x_label, hue = hue_label)

        plt.title(title_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        if  hue_label is not None and labels_hue is not None:
            plt.legend(title = 'Emplyement Status', loc = 'upper right', labels=labels_hue)

        plt.show()


    def create_boxplot(self,df: pd.DataFrame, x_label: str, y_label: str, title_label: str, hue_label: str = None, labels_hue: List = None) -> None:

        """
        Create a box plot using Seaborn.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data to be plotted.
        - x_label (str): The label for the x-axis.
        - y_label (str): The label for the y-axis.
        - title_label (str): The title of the plot.
        - hue_label (str, optional): The column in the DataFrame to use for color encoding.
        - labels_hue (List[str], optional): Labels for the hue categories.

        Returns:
        - None: The function displays the plot but does not return any value.

        This function generates a box plot using Seaborn to visualize the distribution of 
        a numeric variable across different categories. It allows for both basic and grouped 
        box plots based on the presence of the 'hue_label' parameter.

        - Depending on whether 'hue_label' is provided:
        - If 'hue_label' is None, a basic box plot is created with one variable plotted 
            against the other using 'sns.boxplot'.
        - If 'hue_label' is not None, a grouped box plot is created, with the boxes grouped 
            according to the values in the 'hue_label' column. In this case, the 'labels_hue' 
            parameter can be used to provide custom labels for the hue categories.
        - The 'title_label', 'x_label', and 'y_label' parameters are used to set the title, x-axis 
        label, and y-axis label of the plot, respectively.
        - If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot 
        to indicate the categories represented by different colors.

        The function displays the plot using 'plt.show()' and does not return any value.
        """
        if  hue_label is None:
            sns.boxplot(data =df, y = y_label, x= x_label)
        else:
            sns.boxplot(data =df, y = y_label, x= x_label, hue = hue_label) 
        plt.title(title_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label) 
        if  hue_label is not None and labels_hue is not None:
            plt.legend(title = 'Emplyement Status', loc = 'upper right', labels=labels_hue) 
        plt.show()



    def create_violinplot(self,df: pd.DataFrame, x_label: str, y_label: str, title_label: str, hue_label: str = None, labels_hue: List = None) -> None:

        """
        Create a violin plot using Seaborn.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data to be plotted.
        - x_label (str): The label for the x-axis.
        - y_label (str): The label for the y-axis.
        - title_label (str): The title of the plot.
        - hue_label (str, optional): The column in the DataFrame to use for color encoding.
        - labels_hue (List[str], optional): Labels for the hue categories.

        Returns:
        - None: The function displays the plot but does not return any value.

        This function generates a violin plot using Seaborn to visualize the distribution of 
        a numeric variable across different categories. It allows for both basic and grouped 
        violin plots based on the presence of the 'hue_label' parameter.

        - Depending on whether 'hue_label' is provided:
        - If 'hue_label' is None, a basic violin plot is created with one variable plotted 
            against the other using 'sns.violinplot'.
        - If 'hue_label' is not None, a grouped violin plot is created, with the violins 
            grouped according to the values in the 'hue_label' column. In this case, the 
            'labels_hue' parameter can be used to provide custom labels for the hue categories.
        - The 'title_label', 'x_label', and 'y_label' parameters are used to set the title, x-axis 
        label, and y-axis label of the plot, respectively.
        - If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot 
        to indicate the categories represented by different colors.

        The function displays the plot using 'plt.show()' and does not return any value.
        """
        if  hue_label is None:
            sns.violinplot(data =df, y = y_label, x= x_label)
        else:
            sns.violinplot(data =df, y = y_label, x= x_label, hue = hue_label)
        plt.title(title_label)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        if  hue_label is not None and labels_hue is not None:
            plt.legend(title = 'Emplyement Status', loc = 'upper right', labels=labels_hue)
        plt.show()


