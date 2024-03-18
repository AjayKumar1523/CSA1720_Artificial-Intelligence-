% Base case: The sum of integers from 1 to 1 is 1.
sum_up_to_n(1, 1).

% Recursive case: To compute the sum of integers from 1 to n,
% we compute the sum of integers from 1 to n-1 and add n to it.
sum_up_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_up_to_n(N1, Sum1),
    Sum is Sum1 + N.
