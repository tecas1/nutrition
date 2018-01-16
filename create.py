from pandas import read_csv, pivot_table

na = read_csv("NUTRIENT AMOUNT.csv",index_col="NutrientID",usecols=["FoodID","NutrientID","NutrientValue"])
nn = read_csv("NUTRIENT NAME.csv",index_col="NutrientID",usecols=["NutrientID","NutrientSymbol","NutrientName","NutrientUnit"],na_filter = False)

a1 = na.join(nn)
a2 = pivot_table(a1,values="NutrientValue",index=["FoodID"],columns=["NutrientSymbol"])

fn = read_csv("FOOD NAME.csv",index_col="FoodID",usecols=["FoodID","FoodDescription","FoodGroupID"])
fg = read_csv("FOOD GROUP.csv",index_col="FoodGroupID",usecols=["FoodGroupID","FoodGroupName"])

fg["Volume"] = 1

a3 = a2.join(fn).join(fg,"FoodGroupID").sort_values(by=["FoodGroupName","FoodDescription"])

with open("data.js","w") as outfile:
	outfile.write("var foods = " + a3.to_json(orient="records"))

with open("labels.js","w") as outfile:
	outfile.write("var nutrient_labels = " + nn.set_index("NutrientSymbol").to_json(orient="index"))


