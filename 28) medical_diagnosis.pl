% Define symptoms and corresponding diseases
symptom(fever, malaria).
symptom(cough, cold).
symptom(rash, allergy).
symptom(headache, migraine).

% Define rules for diagnosis
diagnosis(Patient, Disease) :-
    symptom(Symptom, Disease),
    patient_has_symptom(Patient, Symptom).

% Define example patient symptoms
patient_has_symptom(john, fever).
patient_has_symptom(john, headache).

% Query for diagnosis
% ?- diagnosis(john, Disease).
