import streamlit as st
import plotly.express as px
import pandas as pd
import pandas as pd

st.title("Silicon Starlings")
stars_dataframe = pd.read_csv("Stars.csv")

st.write("Inspection")
st.write("Head")
st.table(stars_dataframe.head())
st.write("Tail")
st.table(stars_dataframe.tail())
st.write("Shape")
st.write(stars_dataframe.shape)
st.write("Columns")
st.write(stars_dataframe.columns)
st.write("Basic Statistics")
st.table(stars_dataframe.describe())
st.write("Info")
st.write(stars_dataframe.info())

st.markdown("---")

# Clean the data -> Leon
cleanstars_dataframe = stars_dataframe.dropna()
dropped_columns = ['Type']
cleanstars_dataframe.drop(dropped_columns, axis=1, inplace=True)
cleanstars_dataframe.describe()

st.write("Cleaned data")
st.write("The data cleaning process involved the removal of all null values as well as the the final column. The column 'Type' was removed because of it's irrelevance to the processing.")
st.write("Post-processing Head")
st.table(cleanstars_dataframe.head())
st.write("Post-processing Tail")
st.table(cleanstars_dataframe.tail())
st.write("Post-processing Shape")
st.write(cleanstars_dataframe.shape)
st.write("Post-processing Columns")
st.write(cleanstars_dataframe.columns)
st.write("Post-processing Basic Statistics")
st.table(cleanstars_dataframe.describe())
st.write("Post-processing Info")
st.write(cleanstars_dataframe.info())

st.write("Hypothesis 1")
fig = px.scatter(x=cleanstars_dataframe["L"], y=cleanstars_dataframe["R"])
st.plotly_chart(fig, use_container_width=True)

st.write(
  "Two main groupings of stars: those with small relative radii and a range of different luminosities, and those with large relative radii and a range of different luminosities. The latter is far more spread out in terms of radii, rather than being 'squished' down near the x-axis for the former. While the graph has loose form, it does indicate that stars tend to either have small or large relative radii, with little inbetween, alongside a range of luminosities."
)

st.write(
  "Why is there a split in the grouping of stars, and what kinds of stars make up the groups with large and small radii?"
)

st.write(
  "This can be answered by color coding the stars different colors based on star color and spectral class, alongside online research of stars with abnormally high radii."
)

st.markdown("---")

st.write("Hypothesis 2")
fig2 = px.scatter(x=cleanstars_dataframe['L'],
                  y=cleanstars_dataframe['Temperature'],
                  log_x=True,
                  range_x=[0.00001, 1000000])
fig2.update_layout(height=800,
                   title_text="Relative Luminosity vs. Temperature (k)")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(x=cleanstars_dataframe['L'],
                  y=cleanstars_dataframe['A_M'],
                  log_x=True,
                  range_x=[0.00001, 1000000])

st.write("Even after the removal of outliers (Luminosity {<1, >70000}), there seems to be little correlation between the luminosity and temperature of the stars. Within the dataset, most of the points are below 1 and above 10000, with a large variation in luminosity. This can be largely attributed to the nature of the relative luminosity value. It's formula is simply a constant multiplied by the size of the star and the temperature raised to the fourth power. When adjusted to a logarithmic scale (10^x), the graph seems to conform to the exponential growth curve with two clusters of outliers, similar to the relationship between temperature and absolute magnitude.")
st.plotly_chart(fig3, use_container_width=True)
st.write("Most datapoints that are outliers in this graph are also outliers in the absolute magnitude vs temperature graph, suggesting a relationship between absolute magnitude and luminosity as seen by the correlation in fig. 3"
)

st.markdown("---")

st.write("Hypothesis 3")
fig4 = px.scatter(x=cleanstars_dataframe["A_M"],
                 y=cleanstars_dataframe["Temperature"])
st.plotly_chart(fig4, use_container_width=True)

st.write(
  "There is a general curve of stars that looks like an exponential decay curve. In general, the higher the absolute magnitude (lower the brightness), the lower the temperature, which makes sense intuitively. However, there are two groups of outliers. The first group is located when the absolute magnitude is less than -5. Despite their low absolute magnitudes (high brightness), they have incredibly low temperatures. The second group is located with the absolute magnitude is greater than 10. Despite their high absolute magnitudes (low brightness), they have incredibly high temperatures."
)

st.write(
  "What makes the stars from each outlier group special?"
)

st.write(
  "This can be answered by color coding the stars different colors based on star color and spectral class, alongside online research of stars with abnormally high brightness and low temperatures and stars with low brightness and high temperatures."
)

st.markdown("---")

st.write("Hypothesis 4")
color_frequency = cleanstars_dataframe["Color"].value_counts()
fig5 = px.pie(cleanstars_dataframe, names='Color', title='Frequency of star')
fig5.update_traces(hoverinfo='percent', textinfo='value')
st.plotly_chart(fig5, use_container_width=True)

st.write(
  "Hypothesis 4 Anaylsis"
)

st.markdown("---")

st.write("Hypothesis 5")
fig6 = px.density_heatmap(x=cleanstars_dataframe["Color"],
                         y=cleanstars_dataframe["Spectral_Class"])
fig6.update_xaxes(categoryarray=[
  "Red", "OrangeRed", "Orange", "YellowOrange", "Yellow", "YellowWhite",
  "White", "BlueWhite", "Blue"
])
fig6.update_yaxes(categoryarray=["M", "K", "G", "F", "A", "B", "O"])
st.plotly_chart(fig6, use_container_width=True)

st.write(
  "According to online research, the spectral classifications indicate different colors and temperatures of the star, where M is the most red and O is the most blue. We see this in the heat map, as bluer stars are of the O, B, and A spectral classes, yellower stars are part of the F and G classes, and oranger stars are part of the K class, and red stars are part of the M class. Online research also indicates increasing temperature for different spectral classes, where O>B>A>F>G>K>M in terms of temperature."
)

st.write(
  "Would the same pattern of increasing temperature based on spectral class also apply to solely color, considering spectral class and color have a proportional relationship?"
)

st.write(
  "This can be answered through studying the relationship and creating graphs between temperature and color, as well as online research on why stars of certain color have different or greater temperatures than stars of other colors."
)

"""
#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Title Here")

#adding discription to your website
st.text('Description')

#Thesis here
st.header('Thesis')
st.text('Add your Thesis here')


#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
BostonHousing = pd.read_csv("BostonHousing.csv")

#showing dataset
st.table(BostonHousing.head())
st.text('Showing dataset and writting about it here')


#Adding images to make your streamlit look visually better!
st.image('pro.png')
st.text('You can add photos with descriptions')

#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
#adding graphs by images
st.image('pasted image 0.png')
st.text('Discription about your graph and visualizations')

#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')


#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')
"""
