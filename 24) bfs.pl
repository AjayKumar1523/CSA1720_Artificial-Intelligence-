% Example heuristic function: number of misplaced tiles in a 8-puzzle problem
heuristic(State, H) :-
    final_state(GoalState),
    misplaced_tiles(State, GoalState, H).

misplaced_tiles(State, GoalState, H) :-
    State = [S1, S2, S3, S4, S5, S6, S7, S8],
    GoalState = [G1, G2, G3, G4, G5, G6, G7, G8],
    misplaced_tiles_helper([S1, S2, S3, S4, S5, S6, S7, S8], [G1, G2, G3, G4, G5, G6, G7, G8], 0, H).

misplaced_tiles_helper([], [], H, H).
misplaced_tiles_helper([S | SRest], [G | GRest], Acc, H) :-
    (   S \= G -> NewAcc is Acc + 1 ; NewAcc is Acc ),
    misplaced_tiles_helper(SRest, GRest, NewAcc, H).

% Example successor function for a 8-puzzle problem
successor(State, Successors) :-
    findall(NextState, move(State, NextState), Successors).

move(State, NextState) :-
    select(X, State, Rest),
    select(Y, Rest, NewRest),
    swap(X, Y, State, NextState),
    NextState \= State. % to avoid looping back to the same state

swap(X, Y, List, Result) :-
    append(Prefix, [X|Suffix], List),
    append(Prefix, [Y|Suffix], Temp),
    append(Pre, [Y|Post], Temp),
    append(Pre, [X|Post], Result).

% Example final state for a 8-puzzle problem
final_state([1, 2, 3, 4, 5, 6, 7, 8]).

% Best-First Search algorithm
best_first_search(Start, Path) :-
    best_first_search([node(Start, [])], [], Path).

best_first_search([node(State, Path) | _], _, Path) :-
    final_state(State).
best_first_search([node(State, Path) | Queue], Closed, FinalPath) :-
    \+ member(State, Closed),
    successor(State, Successors),
    add_to_queue(Successors, Path, [State | Closed], NewQueue),
    best_first_search(NewQueue, [State | Closed], FinalPath).

add_to_queue([], _, _, []).
add_to_queue([State | States], Path, Closed, NewQueue) :-
    heuristic(State, H),
    append(Path, [State], NewPath),
    add_to_queue(States, Path, Closed, RestQueue),
    insert_queue(node(State, NewPath), H, RestQueue, NewQueue).

insert_queue(Node, _, [], [Node]).
insert_queue(Node, H1, [node(State2, Path2) | RestQueue], [Node, node(State2, Path2) | RestQueue]) :-
    heuristic(State2, H2),
    H1 =< H2.
insert_queue(Node, H1, [node(State2, Path2) | RestQueue], [node(State2, Path2) | NewRestQueue]) :-
    heuristic(State2, H2),
    H1 > H2,
    insert_queue(Node, H1, RestQueue, NewRestQueue).

% Define a predicate to start the search with a given initial state
start_best_first_search(InitialState, Path) :-
    best_first_search(InitialState, Path).
