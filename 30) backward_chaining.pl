% Define facts about diseases and their symptoms
disease(malaria, [fever, chills, headache]).
disease(cold, [cough, sneezing, sore_throat]).
disease(allergy, [rash, itching, sneezing]).
disease(migraine, [headache, nausea, sensitivity_to_light]).

% Define rules for diagnosis using backward chaining
diagnosis(Patient, Disease) :-
    disease(Disease, Symptoms),
    patient_has_symptoms(Patient, Symptoms).

% Define predicate to check if patient has symptoms
patient_has_symptoms(_, []).
patient_has_symptoms(Patient, [Symptom | Rest]) :-
    patient_has_symptom(Patient, Symptom),
    patient_has_symptoms(Patient, Rest).

% Define patient symptoms
patient_has_symptom(john, fever).
patient_has_symptom(john, headache).

% Query for diagnosis using backward chaining
% ?- diagnosis(john, Disease).
