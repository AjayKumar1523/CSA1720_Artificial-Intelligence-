% Define relationships between students, teachers, and subjects with their codes

% Subject codes
subject_code(math, m101).
subject_code(science, s202).
subject_code(history, h303).
subject_code(english, e404).

% Teachers and the subjects they teach
teaches(john, math, m101).
teaches(lisa, science, s202).
teaches(mike, history, h303).
teaches(sarah, english, e404).

% Students and the subjects they study
studies(jack, math, m101).
studies(emma, science, s202).
studies(alex, history, h303).
studies(lily, english, e404).

% Query to find the subject code taught by a teacher
teacher_subject_code(Teacher, Subject, Code) :-
    teaches(Teacher, Subject, Code).

% Query to find the subject code studied by a student
student_subject_code(Student, Subject, Code) :-
    studies(Student, Subject, Code).
