import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# Load the dataset
df = pd.read_csv('World_Nuclear_Power_Reactors.csv', encoding='ISO-8859-1')

# Summary statistics
summary_stats = df.describe(include='all')


# Convert 'Net Capacity (MWe)' to numeric type
df['Net Capacity (MWe)'] = pd.to_numeric(df['Net Capacity (MWe)'], errors='coerce')

# Display the top ten reactors by net capacity
df_top_ten = df.nlargest(10, 'Net Capacity (MWe)')


# Convert 'Reactor Type' to a numeric type (this may not be appropriate, needs context)
df['Reactor Type'] = pd.to_numeric(df['Reactor Type'], errors='coerce')

# Filter data for the given example
df_filtered = df[(df['Country'].isin(['Argentina', 'Armenia'])) &
                 (df['Reactor Name'].isin(['Atucha 1', 'Embalse', 'Atucha 2', 'Armenian 2']))]

# Ensure correct data types
df_filtered['Construction Start'] = pd.to_datetime(df_filtered['Construction Start'], errors='coerce')
df_filtered['First Grid Connection'] = pd.to_datetime(df_filtered['First Grid Connection'], errors='coerce')

# Get the top ten counts of reactor distribution by country
top_ten_counts = df['Country'].value_counts().nlargest(5)

# Create the dashboard
fig = plt.figure(figsize=(20, 18))
gs = GridSpec(4, 2, figure=fig, height_ratios=[1, 1, 0.1, 1])

# Distribution of Reactors by Country (Top Ten)
ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(top_ten_counts, labels=top_ten_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(top_ten_counts)))
ax1.set_title("Distribution of Reactors by Country",fontweight='bold')

# Count of Reactor Types
ax2 = fig.add_subplot(gs[0, 1])
sns.countplot(x="Reactor Type", data=df, palette="viridis", ax=ax2)
ax2.set_title("Count of Reactor Types",fontweight='bold')
ax2.set_xlabel("Reactor Type",fontweight='bold')
ax2.set_ylabel("Count",fontweight='bold')

# Timeline of Reactor Construction and Grid Connection
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(df_filtered["Reactor Name"], df_filtered["Construction Start"], marker='o', label='Construction Start')
ax3.plot(df_filtered["Reactor Name"], df_filtered["First Grid Connection"], marker='o', label='First Grid Connection')
ax3.set_title("Timeline of Reactor Construction and Grid Connection",fontweight='bold')
ax3.set_xlabel("Reactor Name",fontweight='bold')
ax3.set_ylabel("Year",fontweight='bold')
ax3.legend()
ax3.set_xticklabels(df_filtered["Reactor Name"], rotation=45)

# Bar Plot of Net Capacity by Reactor for the top ten reactors
ax4 = fig.add_subplot(gs[1, 1])
sns.barplot(x="Reactor Name", y="Net Capacity (MWe)", data=df_top_ten, palette="viridis", ax=ax4)
ax4.set_title("Top 10 Reactors by Net Capacity",fontweight='bold')
ax4.set_xlabel("Reactor Name",fontweight='bold')
ax4.set_ylabel("Net Capacity (MWe)",fontweight='bold')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=25)

# Add some space between plots and the text description
fig.subplots_adjust(hspace=0.5, top=0.85)

# Text description
ax5 = fig.add_subplot(gs[3, :])
ax5.axis('off')
description_text = """
This dashboard provides an overview of the world’s nuclear power reactors:
1. Reactors by Net Capacity: USA has the highest net capacity of reactors.
2. Count of Reactor Types: 32.0 reactor type has the highest distribution.
3. Timeline of Reactor Construction and Grid Connection: Illustrates the construction and grid connection timelines for selected reactors.
4. Distribution of Reactors by Country: 'Beloyarsk 4' and 'Akademik lomonosvo1' have the highest number of reactors.

Name: Narendar Vatsavai
Student Id: 22103577
"""
ax5.text(0, 0.5, description_text, ha='left', va='center', fontsize=12, fontweight='bold', wrap=True)

# Add a title to the entire dashboard
fig.suptitle('World Nuclear Power Reactors Dashboard', fontsize=20, y=0.98, weight='bold')

# Save the figure as a JPG image
plt.savefig('22103577.jpg', format='jpg', bbox_inches='tight',dpi=300)



