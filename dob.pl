% Database of names and dates of birth (DOB)
dob(john, '1990-05-15').
dob(sarah, '1985-09-20').
dob(mike, '1978-03-10').
dob(lisa, '2000-11-25').
dob(emma, '1998-07-03').

% Query to retrieve date of birth based on name
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).
