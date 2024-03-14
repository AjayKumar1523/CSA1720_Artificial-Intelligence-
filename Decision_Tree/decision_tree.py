from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
outlook = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy']
temperature = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild']
humidity = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high']
wind = ['weak', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong']
play = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
le_outlook = LabelEncoder()
le_temperature = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
outlook_encoded = le_outlook.fit_transform(outlook)
temperature_encoded = le_temperature.fit_transform(temperature)
humidity_encoded = le_humidity.fit_transform(humidity)
wind_encoded = le_wind.fit_transform(wind)
features = list(zip(outlook_encoded, temperature_encoded, humidity_encoded, wind_encoded))
clf = DecisionTreeClassifier()
clf = clf.fit(features, play)
tree_rules = export_text(clf, feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'])
print(tree_rules)
