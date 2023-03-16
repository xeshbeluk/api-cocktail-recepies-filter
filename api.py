import requests
import pandas as pd

# creating a function to make 10 API requests
raw = None
def fetch():
	global data
	url = "https://the-cocktail-db.p.rapidapi.com/randomselection.php"

	headers = {
		"X-RapidAPI-Key": "61ac0790b5msh0f2c788ea57f693p117a4fjsne635b7d638a9",
		"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers)
	raw = pd.DataFrame.from_dict(response.json(), orient='index')
	raw.to_csv('df.csv')

# fetching the data and transforming it into a dataframe
res_list = []
for i in range(1,20): 	# adjusting the number of fetches
	fetch()
	data = pd.read_csv('df.csv')
	data_2 = data.iloc[0]
	for i in range(1, len(data_2)):
		res_list.append(eval(data_2[i]))

# dropping unused categories
overall_data = pd.DataFrame(res_list).drop(['strInstructionsES', 'strInstructionsDE',
											'strInstructionsFR', 'strInstructionsIT',
											'strInstructionsZH-HANS', 'strInstructionsZH-HANT',
											'strDrinkThumb', 'strTags', 'strVideo', 'strDrinkAlternate',
											'strCreativeCommonsConfirmed', 'strImageAttribution',
											'strImageSource', 'strIBA'], axis = 1)

overall_data.to_csv('overall_data.csv')