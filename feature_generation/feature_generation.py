from seperation import seperation
import pandas as pd

def feature_generation_cont(df, continous, target):
	"""Continous Variables"""
	
	for i in range(len(continous)-1):
		var_1 = continous[i]
		var_2 = continous[i+1]
		# ratios
		df["ratio_"+str(var_1)+"_"+str(var_2)] = df[var_1].astype("float")/df[var_2].astype("float")
		#products
		df["prod_"+str(var_1)+"_"+str(var_2)] = df[var_1].astype("float")*df[var_2].astype("float")

	for i in range(len(continous)):
		var_1 = continous[i]
		#square
		df["sqr_"+str(var_1)] = df[var_1].apply(lambda x: x**2)
		
	return df
	
def count_to_dict(df, col):
	grp = df.groupby([col])[col].agg(['count']).reset_index()
	dt = {}
	for i in range(grp.shape[0]):
		dt[grp.iloc[i,0]] = grp.iloc[i,1]
	return dt

def feature_generation_catg(df, categorical, target):
	'''categorical variables'''
	for col in categorical:
		if col == target:
			pass
		elif 'imputed' in col:
			pass
		else:
			dt = count_to_dict(df, col)
			df["count_"+str(col)] = df[col].apply(lambda x: dt[x])

	one_hot = []
	drop = []
	for col in categorical:
		if col == target:
			pass
		elif 'imputed' in col:
			pass
		else:
			if float(len(df[col].unique()))/df.shape[0] <= .10:
				one_hot.append(col)
			else:
				drop.append(col)
	df = pd.get_dummies(df, columns = one_hot, drop_first = True)
	df = df.drop(drop, axis = 1)

				
	return df

def feature_generation(df, target):
	idx, categorical, continous = seperation.seperation(df)
	df = feature_generation_cont(df, continous, target)
	df = feature_generation_catg(df, categorical, target)

	return df