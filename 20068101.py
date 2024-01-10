# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:16:08 2024

@author: Guest User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap

# Load the dataset
file_path = r'./content/dataset.csv'
data = pd.read_csv(file_path)

# Set the background style
sns.set(rc={'axes.facecolor': 'blue', 'figure.facecolor': 'forestgreen', 'text.color': 'white'})

# Create plots
fig, axs = plt.subplots(nrows=16, ncols=2, figsize=(30, 75), gridspec_kw={'hspace': 0.15, 'height_ratios': [0.5, 0.01, 1, 1, .2, 0.03, 1, 0.4, 0.2, 1, 0.4, 0.2, 1.5, 1.5, 1.5, 1.5]})

title_text_1 = "Comparative Analysis of Agricultural Land, Forest Area, and Environmental Metrics Across Austria, Albania, United Arab Emirates, and Brazil (1990-2020)"
student_name = 'Muhammad Usman Khurshid'
student_id = '20068101'

axs[0, 0].remove()  # Remove the existing subplot
axs[0, 1].remove()  # Remove the first row in the second column

axs[0, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[0, 0].wrapped_text = textwrap.fill(title_text_1, width=130)
axs[0, 0].text(0.5, 0.9, axs[0, 0].wrapped_text, ha='center', va='center', weight='bold', color='black', fontsize=20, transform=axs[0, 0].transAxes)
axs[0, 0].text(0.5, 0.86, student_name, ha='center', va='center', weight='bold', color='black', fontsize=15, transform=axs[0, 0].transAxes)
axs[0, 0].text(0.5, 0.84, student_id, ha='center', va='center', weight='bold', color='black', fontsize=15, transform=axs[0, 0].transAxes)
axs[0, 0].axis('off') 
axs[0, 1].axis('off')  

# Graphs
title_text_2 = "Agricultural Land Percentage Comparison (2000-2020) in Austria, Albania, United Arab Emirates, and Brazil"

axs[1, 0].remove()  # Remove the existing subplot
axs[1, 1].remove()  # Remove the first row in the second column

axs[1, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[1, 0].wrapped_text = textwrap.fill(title_text_2, width=130)
axs[1, 0].text(0.5, 0.8, axs[1, 0].wrapped_text, ha='center', va='center', weight='bold', color='black', fontsize=20, transform=axs[1, 0].transAxes)

axs[1, 0].axis('off') 
axs[1, 1].axis('off')  

# Plot 1

# Select specific indicator for analysis
indicator_to_analyze_pie_chart = 'Agricultural land (% of land area)'

# Select the specific country for analysis
selected_country_first = 'Austria'
selected_country_second = 'Brazil'
selected_country_third = 'United Arab Emirates'
selected_country_fourth = 'Albania'

# Select the range of years for analysis
start_year = 2000
end_year = 2020

# Filter data for the selected indicator, country, and years
selected_data_first = data[(data['Indicator Name'] == indicator_to_analyze_pie_chart) & (data['Country Name'] == selected_country_first)]

# Filter data for the selected indicator, country, and years
selected_data_second = data[(data['Indicator Name'] == indicator_to_analyze_pie_chart) & (data['Country Name'] == selected_country_second)]

# Filter data for the selected indicator, country, and years
selected_data_third = data[(data['Indicator Name'] == indicator_to_analyze_pie_chart) & (data['Country Name'] == selected_country_third)]

# Filter data for the selected indicator, country, and years
selected_data_fourth = data[(data['Indicator Name'] == indicator_to_analyze_pie_chart) & (data['Country Name'] == selected_country_fourth)]

# Extract values for the selected range of years
selected_years = [str(year) for year in range(start_year, end_year + 1)]

#pie chart 1
values = selected_data_first[selected_years].astype(float).mean()

# Plot pie chart on axs[2, 0]
axs[2, 0].pie(values, labels=selected_years, startangle=140, shadow=True, radius=1.1, autopct='%1.1f%%')
axs[2, 0].set_title(f'Pie Chart for {indicator_to_analyze_pie_chart} - {selected_country_first}')

#pie chart 2
values = selected_data_second[selected_years].astype(float).mean()

# Plot pie chart on axs[2, 1]
axs[2, 1].pie(values, labels=selected_years, startangle=140, shadow=True, radius=1.1, autopct='%1.1f%%')
axs[2, 1].set_title(f'Pie Chart for {indicator_to_analyze_pie_chart} - {selected_country_second}')

#pie chart 3
values = selected_data_third[selected_years].astype(float).mean()

# Plot pie chart on axs[3, 0]
axs[3, 0].pie(values, labels=selected_years, startangle=140, shadow=True, radius=1.1, autopct='%1.1f%%')
axs[3, 0].set_title(f'Pie Chart for {indicator_to_analyze_pie_chart} - {selected_country_third}')

#pie chart 4
values = selected_data_fourth[selected_years].astype(float).mean()

# Plot pie chart on axs[3, 1]
axs[3, 1].pie(values, labels=selected_years, startangle=140, shadow=True, radius=1.1, autopct='%1.1f%%')
axs[3, 1].set_title(f'Pie Chart for {indicator_to_analyze_pie_chart} - {selected_country_fourth}')

# pie chart explanation
title_text_3 = "View the agricultural land proportion of Austria, Albania, UAE, and Brazil from 2000 to 2020 using a pie chart. The pie chart shows agricultural land proportion changes throughout time. The percentage of agricultural land for the year is higher for larger slices."

axs[4, 0].remove()  # Remove the existing subplot
axs[4, 1].remove()  # Remove the first row in the second column

axs[4, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[4, 0].wrapped_text = textwrap.fill(title_text_3, width=150)
axs[4, 0].text(0.5, 0, axs[4, 0].wrapped_text, ha='center', va='center', color='black', fontsize=18, transform=axs[4, 0].transAxes)

axs[4, 0].axis('off') 
axs[4, 1].axis('off') 

#bar graph heading

title_text_4 = "Comparative Analysis of Key Indicators in Brazil and Austria (2010-2019)"

axs[5, 0].remove()  # Remove the existing subplot
axs[5, 1].remove()  # Remove the first row in the second column

axs[5, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[5, 0].wrapped_text = textwrap.fill(title_text_4, width=130)
axs[5, 0].text(0.5, -0.07, axs[5, 0].wrapped_text, ha='center', va='center', weight='bold', color='black', fontsize=20, transform=axs[5, 0].transAxes)

axs[5, 0].axis('off') 
axs[5, 1].axis('off')

# Bar Chart

# Select specific indicators for analysis
indicators_to_analyze_bar_chart = ['Agricultural land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)', 'GDP per capita growth (annual %)']

# Select the specific country for analysis
selected_country_first = 'Brazil'
selected_country_second = 'Austria'

# Select the range of years for analysis
start_year_bar_chart = 2010
end_year_bar_chart = 2019

# Filter data for the selected indicators, country, and years
selected_data_first = data[(data['Indicator Name'].isin(indicators_to_analyze_bar_chart)) & (data['Country Name'] == selected_country_first)]
selected_years_first = [str(year) for year in range(start_year_bar_chart, end_year_bar_chart + 1)]

# Prepare data for the bar chart
bar_positions = np.arange(len(selected_years_first))
bar_width = 0.2

for i, indicator in enumerate(indicators_to_analyze_bar_chart):
    values = selected_data_first[selected_data_first['Indicator Name'] == indicator][selected_years_first].astype(float).values.flatten()

    axs[6, 0].bar(bar_positions + i * bar_width, values, width=bar_width, label=indicator)

# Adding Xticks
axs[6, 0].set_xlabel('Year', fontweight='bold', fontsize=15)
axs[6, 0].set_ylabel('Values', fontweight='bold', fontsize=15)
axs[6, 0].set_title(f'Clustered Bar Chart for {selected_country_first}', weight='bold', color='white', fontsize=20)
axs[6, 0].set_xticks(bar_positions)
axs[6, 0].set_xticklabels(selected_years_first)
axs[6, 0].legend()

# Filter data for the selected indicators, country, and years
selected_data_second = data[(data['Indicator Name'].isin(indicators_to_analyze_bar_chart)) & (data['Country Name'] == selected_country_second)]
selected_years_second = [str(year) for year in range(start_year_bar_chart, end_year_bar_chart + 1)]

# Prepare data for the bar chart
bar_positions = np.arange(len(selected_years_second))
bar_width = 0.2

for i, indicator in enumerate(indicators_to_analyze_bar_chart):
    values = selected_data_second[selected_data_second['Indicator Name'] == indicator][selected_years_second].astype(float).values.flatten()

    axs[6, 1].bar(bar_positions + i * bar_width, values, width=bar_width, label=indicator)

# Adding Xticks
axs[6, 1].set_xlabel('Year', fontweight='bold', fontsize=15)
axs[6, 1].set_ylabel('Values', fontweight='bold', fontsize=15)
axs[6, 1].set_title(f'Clustered Bar Chart for {selected_country_second}', weight='bold', color='white', fontsize=20)
axs[6, 1].set_xticks(bar_positions)
axs[6, 1].set_xticklabels(selected_years_second)
axs[6, 1].legend()

#bar graph explanation

title_text_5 = "Clustered bar chart comparing Brazil's and Austria’s indicators from 2010 to 2019. One may visually compare Brazil's indicators across the selected years using the chart. Clustering lets you compare indicator changes across time. The x-axis shows the years (2010–2019) while the y-axis shows the indicator values."

axs[7, 0].remove()  # Remove the existing subplot
axs[7, 1].remove()  # Remove the first row in the second column

axs[7, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[7, 0].wrapped_text = textwrap.fill(title_text_5, width=130)
axs[7, 0].text(0.5, -0.62, axs[7, 0].wrapped_text, ha='center', va='bottom', color='black', fontsize=18, transform=axs[7, 0].transAxes)

axs[7, 0].axis('off') 
axs[7, 1].axis('off')

#line graph heading
title_text_6 = "Time Trends Analysis for Key Metrics in the UAE and Albania"

axs[8, 0].remove()  # Remove the existing subplot
axs[8, 1].remove()  # Remove the first row in the second column

axs[8, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[8, 0].wrapped_text = textwrap.fill(title_text_6, width=100)
axs[8, 0].text(0.5, -0.72, axs[8, 0].wrapped_text, ha='center', va='top', weight='bold', color='black', fontsize=20, transform=axs[8, 0].transAxes)

axs[8, 0].axis('off') 
axs[8, 1].axis('off')

# Select specific indicators for analysis
indicators_to_analyze_line_chart = ['Agricultural land (% of land area)', 'Forest area (% of land area)', 'CO2 emissions (metric tons per capita)', 'GDP per capita growth (annual %)']

# Select the specific country for analysis
selected_country_first = 'United Arab Emirates'
# Select the specific country for analysis
selected_country_second = 'Albania'

# Filter data for selected indicators and country
selected_data_first = data[(data['Indicator Name'].isin(indicators_to_analyze_line_chart)) & (data['Country Name'] == selected_country_first)]

for indicator in indicators_to_analyze_line_chart:
    indicator_data = selected_data_first[selected_data_first['Indicator Name'] == indicator]
    axs[9,0].plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], marker='o', label=indicator)

axs[9,0].set_xlabel('Year')
axs[9,0].set_ylabel('Value')
axs[9,0].set_title(f'Time Trends for {selected_country_first} - Selected Indicators', weight='bold', color='white', fontsize=20)
axs[9,0].legend()

# Filter data for selected indicators and country
selected_data_second = data[(data['Indicator Name'].isin(indicators_to_analyze_line_chart)) & (data['Country Name'] == selected_country_second)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze_line_chart:
    indicator_data = selected_data_second[selected_data_second['Indicator Name'] == indicator]
    axs[9,1].plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], marker='o', label=indicator)

axs[9,1].set_xlabel('Year')
axs[9,1].set_ylabel('Value')
axs[9,1].set_title(f'Time Trends for {selected_country_first} - Selected Indicators', weight='bold', color='white', fontsize=20)
axs[9,1].legend()

#bar graph explanation

title_text_7 = "A line plot showing the time patterns of specific metrics for the United Arab Emirates and Albania using data. The dark-themed line plot displays time trends for agricultural land, forest area, CO2 emissions, and GDP per capita growth in the United Arab Emirates. The figure shows how each indicator changes over time."

axs[10, 0].remove()  # Remove the existing subplot
axs[10, 1].remove()  # Remove the first row in the second column

axs[10, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[10, 0].wrapped_text = textwrap.fill(title_text_7, width=150)
axs[10, 0].text(0.5, -1.3, axs[10, 0].wrapped_text, ha='center', va='bottom', color='black', fontsize=18, transform=axs[10, 0].transAxes)

axs[10, 0].axis('off') 
axs[10, 1].axis('off')

#line graph heading
title_text_8 = "Comparative Analysis of 2010 Indicators: Austria, Albania, UAE, Brazil"

axs[11, 0].remove()  # Remove the existing subplot
axs[11, 1].remove()  # Remove the first row in the second column

axs[11, 0] = fig.add_subplot(4, 2, (1,2), frame_on=False)  

axs[11, 0].wrapped_text = textwrap.fill(title_text_8, width=130)
axs[11, 0].text(0.5, -1.35, axs[11, 0].wrapped_text, ha='center', va='center', weight='bold', color='black', fontsize=20, transform=axs[11, 0].transAxes)

axs[11, 0].axis('off') 
axs[11, 1].axis('off')

# Select specific indicators for analysis
indicators_to_analyze_first = 'Agricultural land (% of land area)'
indicators_to_analyze_second = 'GDP per capita growth (annual %)'
indicators_to_analyze_third = 'Forest area (% of land area)'
indicators_to_analyze_fourth = 'CO2 emissions (metric tons per capita)'

# Select the specific country for analysis
selected_countries = ['Austria', 'Albania', 'United Arab Emirates', 'Brazil']

# Select the specific year for analysis
selected_year = '2010'

# Filter data for selected indicator, countries, and year
selected_data = data[(data['Indicator Name'] == indicators_to_analyze_first) &
                     (data['Country Name'].isin(selected_countries))]

# Extract values for the selected year
values = selected_data[selected_year].astype(float)

# Prepare data for clustered bar chart
bar_positions = np.arange(len(selected_countries))
bar_width = 0.4

# Plot clustered bar chart for the selected countries and indicator
axs[12, 0].barh(bar_positions, values, height=bar_width, color=['white', 'green', 'orange', 'yellow'])
axs[12, 0].set_xlabel(f'{indicators_to_analyze_first} Value')
axs[12, 0].set_ylabel('Country')
axs[12, 0].set_title(f'Clustered Bar Chart for {", ".join(selected_countries)} - {indicators_to_analyze_first} ({selected_year})', weight='bold')

# Add a vertical line at a specific position (e.g., x=20)
axs[12, 0].axvline(x=20, color='red', linestyle='--', label='Threshold Line')

# Customize legend
axs[12, 0].legend()

# Invert y-axis for better readability
axs[12, 0].invert_yaxis()

# Set y-axis ticks and labels
axs[12, 0].set_yticks(bar_positions)
axs[12, 0].set_yticklabels(selected_countries)

# Add labels to each bar
for i, value in enumerate(values):
    axs[12, 0].text(value, i, f'{value:.2f}', ha='left', va='center')

#explanation 1

title_text_9 = 'A clustered horizontal bar chart to compare graphically 2010 "Agricultural land (% of land area)" values for Austria, Albania, UAE, and Brazil. For comparison, use the red dashed threshold line. Country names appear on Y-axis ticks and labels. Each bar has labels with country-specific indicator values.'

axs[12, 1].wrapped_text = textwrap.fill(title_text_9, width=60)
axs[12, 1].text(0, 0.5, axs[12, 1].wrapped_text, ha='left', va='center', color='black', fontsize=18, transform=axs[12, 1].transAxes)

axs[12, 1].axis('off') 

# Plot clustered bar chart for the selected countries and indicator
axs[13, 0].barh(bar_positions, values, height=bar_width, color=['white', 'green', 'orange', 'yellow'])
axs[13, 0].set_xlabel(f'{indicators_to_analyze_second} Value')
axs[13, 0].set_ylabel('Country')
axs[13, 0].set_title(f'Clustered Bar Chart for {", ".join(selected_countries)} - {indicators_to_analyze_second} ({selected_year})', weight='bold')

# Add a vertical line at a specific position (e.g., x=20)
axs[13, 0].axvline(x=20, color='red', linestyle='--', label='Threshold Line')

# Customize legend
axs[13, 0].legend()

# Invert y-axis for better readability
axs[13, 0].invert_yaxis()

# Set y-axis ticks and labels
axs[13, 0].set_yticks(bar_positions)
axs[13, 0].set_yticklabels(selected_countries)

# Add labels to each bar
for i, value in enumerate(values):
    axs[13, 0].text(value, i, f'{value:.2f}', ha='left', va='center')

#explanation 2

title_text_10 = "Austria had 1.59% GDP per capita growth in 2010, whereas Albania had 4.22%, indicating economic expansion. The UAE contracted -4.26%, whereas Brazil grew 6.52%, showing economic diversity."

axs[13, 1].wrapped_text = textwrap.fill(title_text_10, width=60)
axs[13, 1].text(0, 0.5, axs[13, 1].wrapped_text, ha='left', va='center', color='black', fontsize=18, transform=axs[13, 1].transAxes)

axs[13, 1].axis('off') 

# Plot clustered bar chart for the selected countries and indicator
axs[14, 0].barh(bar_positions, values, height=bar_width, color=['white', 'green', 'orange', 'yellow'])
axs[14, 0].set_xlabel(f'{indicators_to_analyze_third} Value')
axs[14, 0].set_ylabel('Country')
axs[14, 0].set_title(f'Clustered Bar Chart for {", ".join(selected_countries)} - {indicators_to_analyze_third} ({selected_year})', weight='bold')

# Add a vertical line at a specific position (e.g., x=20)
axs[14, 0].axvline(x=20, color='red', linestyle='--', label='Threshold Line')

# Customize legend
axs[14, 0].legend()

# Invert y-axis for better readability
axs[14, 0].invert_yaxis()

# Set y-axis ticks and labels
axs[14, 0].set_yticks(bar_positions)
axs[14, 0].set_yticklabels(selected_countries)

# Add labels to each bar
for i, value in enumerate(values):
    axs[14, 0].text(value, i, f'{value:.2f}', ha='left', va='center')

#explanation 3

title_text_11 = "Austria had 8.37 metric tons of CO2 per capita in 2010, indicating a low environmental impact. Albania has a low 1.64 metric tons, indicating a greener footprint. The United Arab Emirates has a 19.19 metric ton carbon footprint, probably due to industrial activities. Brazil's CO2 emissions per capita were 2.03 metric tons, indicating a balanced environmental impact"

axs[14, 1].wrapped_text = textwrap.fill(title_text_11, width=60)
axs[14, 1].text(0, 0.5, axs[14, 1].wrapped_text, ha='left', va='center', color='black', fontsize=18, transform=axs[14, 1].transAxes)

axs[14, 1].axis('off') 

# Plot clustered bar chart for the selected countries and indicator
axs[15, 0].barh(bar_positions, values, height=bar_width, color=['white', 'green', 'orange', 'yellow'])
axs[15, 0].set_xlabel(f'{indicators_to_analyze_fourth} Value')
axs[15, 0].set_ylabel('Country')
axs[15, 0].set_title(f'Clustered Bar Chart for {", ".join(selected_countries)} - {indicators_to_analyze_fourth} ({selected_year})', weight='bold')

# Add a vertical line at a specific position (e.g., x=20)
axs[15, 0].axvline(x=20, color='red', linestyle='--', label='Threshold Line')

# Customize legend
axs[15, 0].legend()

# Invert y-axis for better readability
axs[15, 0].invert_yaxis()

# Set y-axis ticks and labels
axs[15, 0].set_yticks(bar_positions)
axs[15, 0].set_yticklabels(selected_countries)

# Add labels to each bar
for i, value in enumerate(values):
    axs[15, 0].text(value, i, f'{value:.2f}', ha='left', va='center')

#explanation 4

title_text_12 = "Austria displayed its 46.82% forest area in 2010 to demonstrate its environmental commitment. Albania had 28.54% forest cover, suggesting a high natural resource presence. The United Arab Emirates had only 4.47% woodland, reflecting its desert climate. Brazil had 61.21% forest area, demonstrating its biodiversity and rainforest coverage."

axs[15, 1].wrapped_text = textwrap.fill(title_text_12, width=60)
axs[15, 1].text(0, 0.5, axs[15, 1].wrapped_text, ha='left', va='center', color='black', fontsize=18, transform=axs[15, 1].transAxes)

axs[15, 1].axis('off') 

# Set the background color of the figure
fig.patch.set_facecolor('forestgreen')

# Save the figure as a PNG file
fig.savefig("/content/20068101.png", dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()
