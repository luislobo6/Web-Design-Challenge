import pandas as pd

# Route to the file
file = "Resources/cities.csv"
# read file with pandas
file_df = pd.read_csv(file)
#file_df.head()

# set the index to City_ID so we don't have 0,1,2...
file_df = file_df.set_index("City_ID")

# write the file into html code to copy
file_df.to_html("Resources/dataframe.html")