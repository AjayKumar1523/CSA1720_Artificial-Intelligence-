% Define facts about birds and whether they can fly
can_fly(sparrow).
can_fly(eagle).
can_fly(crow).

% Query to determine if a specific bird can fly
can_fly_query(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

can_fly_query(Bird) :-
    \+ can_fly(Bird),
    format('~w cannot fly.~n', [Bird]).
