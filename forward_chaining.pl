% Define facts about symptoms and diseases
symptom(fever, malaria).
symptom(cough, cold).
symptom(rash, allergy).
symptom(headache, migraine).

% Define rules for diagnosis using forward chaining
diagnosis(Patient, Disease) :-
    symptom(Symptom, Disease),
    patient_has_symptom(Patient, Symptom).

% Define patient symptoms
patient_has_symptom(john, fever).
patient_has_symptom(john, headache).

% Query for diagnosis using forward chaining
% ?- diagnosis(john, Disease).
