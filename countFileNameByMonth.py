import pandas as pd
import glob

# Count no of files by month
def countFileByMonth(month, directory, pattern):
    fileNames = glob.glob(f"/home/faysal/Desktop/{directory}*{month}_{pattern}.csv")
    totalFilesByMonth = len(fileNames)
    return f"{month} => {totalFilesByMonth}", sorted(fileNames)



def main(directory, pattern, months = ["Jan","Feb","Mar","Apr","May", "Jun", "Jul"]):
    monthToSearch = months
    directory = len(monthToSearch)*[directory]
    pattern = len(monthToSearch)*[pattern]
    totalFilesAndFileNames = list(map(countFileByMonth, monthToSearch, directory, pattern))
    totalFilesByMonth = [f[0] for f in totalFilesAndFileNames]
    return print(totalFilesByMonth)


# Asks for a number. If 1 is input, it optimizes 15 providers data. Otherwise it optimizes all discount courses data.
number = int(input("Type the required number:"))

if number==1:
	main("masterData/15Competitor/", "15_providers")
else:
	main("masterData/allDiscountCourse/", "allDiscount")