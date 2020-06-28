# Import required modules.
import pandas as pd
import glob
from datetime import datetime
today = datetime.today().strftime("%d_%b")


def optimizeData(directory1, directory2, pattern):
	"""This script concats all the data frames into one and optimize variable data types (hence space) and save as a pickle file.
	directory1 = directory to read from.
	directory2 = directory to save the optimized file to.
	pattern = pattern by which files will be read."""
    
	# Read and concat all the dfs
	masterDf = pd.concat([pd.read_csv(f, encoding="latin1") for f in glob.glob(f"/home/faysal/Desktop/masterData{directory1}*{pattern}.csv")])

	# Sort string of dates to save file
	dateSorted = sorted(masterDf.date.unique()+"_20", key=lambda x: datetime.strptime(x, "%d_%b_%y"))
	day1 = dateSorted[0]
	day2 = dateSorted[-1]

	# These columns will will be converted into category
	colsToCat = masterDf.columns[~masterDf.columns.isin(["unitSold", "offerPrice", "savingsPercent"])]

	# Create an empty dataframe 
	optimizedDf = pd.DataFrame()
	optimizedDf[colsToCat] = masterDf[colsToCat].astype("category")
	optimizedDf["unitSold"] = pd.to_numeric(masterDf.unitSold, downcast="integer")
	optimizedDf["offerPrice"] = masterDf["offerPrice"].apply(pd.to_numeric, downcast="float")
	optimizedDf["savingsPercent"] = pd.to_numeric(masterDf["savingsPercent"], downcast="integer")

	# Remove unnamed columns if any
	optimizedDf = optimizedDf.loc[:, ~optimizedDf.columns.str.contains("^Unnamed")]
	day1 = "_".join(day1.split("_")[:2])
	day2 = "_".join(day2.split("_")[:2])
	print(f"{masterDf.date.unique().shape[0]} files optimized.")
	return optimizedDf.to_pickle(f"/home/faysal/Desktop{directory2}{day1}_to_{day2}_{pattern}.pickle")



# Asks for a number. If 1 is input, it optimizes 15 providers data. Otherwise it optimizes all discount courses data.
number = int(input("Type the required number:"))

if number==1:
	# Optimize 15 providers data
	optimizeData("/15Competitor/", "/pickledData/", "15_providers")
else:
	# Or if we wanna optimize all the discount courses
	optimizeData("/allDiscountCourse/", "/pickledData/", "allDiscount")
