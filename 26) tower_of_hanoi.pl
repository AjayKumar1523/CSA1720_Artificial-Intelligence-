% Define the predicate to solve Towers of Hanoi
hanoi(1, Start, _, End, Moves) :-
    append([], [move(Start, End)], Moves).
hanoi(N, Start, Helper, End, Moves) :-
    N > 1,
    M is N - 1,
    hanoi(M, Start, End, Helper, FirstMoves),
    hanoi(1, Start, _, End, LastMove),
    hanoi(M, Helper, Start, End, SecondMoves),
    append(FirstMoves, [LastMove | SecondMoves], Moves).
