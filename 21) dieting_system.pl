% Define facts for dietary recommendations based on health conditions
diet_recommendation(diabetes, 'Eat more whole grains, fruits, vegetables, and lean proteins. Avoid sugary drinks and processed foods.').
diet_recommendation(hypertension, 'Limit sodium intake, eat more fruits, vegetables, and low-fat dairy products. Avoid high-fat, high-cholesterol foods.').
diet_recommendation(obesity, 'Reduce calorie intake, eat smaller portions, increase physical activity. Focus on a balanced diet with plenty of fruits, vegetables, and whole grains.').

% Query predicate to get diet recommendation for a specific health condition
get_diet_recommendation(Condition, Recommendation) :-
    diet_recommendation(Condition, Recommendation).
