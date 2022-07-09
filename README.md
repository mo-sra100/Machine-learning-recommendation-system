# Machine-learning-recommendation-system
A recreation of the machine learning recommendation system used by Facebook Marketplace to clean and process text/image data and offer personalised results.

MILESTONE 1 - EXPLORE THE DATASET:
Accessed a dataset which contained different features of thousands of products found on Gumtree, including: product ID, product name, description, price, location etc. Using Pandas I cleaned this data: removed irrelevant columns, gave appropriate headings, removed rows containing null values, removed "£" symbol from price column.
Accessed a dataset which contained images of products found on Gumtree. These images were of various dimensions, so I resized them all to the same dimensions, and added black borders where necessary to keep the aspect ratio consistent. These cleaned images were saved as new files in a new folder.
Now that the ctext and image data has been claened, they can be used for the models which I will build next.