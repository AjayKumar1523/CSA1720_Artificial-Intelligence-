% Define initial state
initial_state(state(atdoor, onfloor, atwindow, hasnot)).

% Define final state
final_state(state(_, _, _, has)).

% Define move actions
move(state(middle, onbox, middle, hasnot), grab, state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H), climb, state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H), push(P1, P2), state(P2, onfloor, P2, H)).
move(state(P1, onfloor, B, H), walk(P1, P2), state(P2, onfloor, B, H)).

% Define goal-reaching predicate
goal_reached(State) :-
    final_state(State).

% Solve predicate
solve(State, []) :-
    goal_reached(State).
solve(State1, [Move | Moves]) :-
    move(State1, Move, State2),
    solve(State2, Moves).

% Print solution
print_solution([]).
print_solution([Move | Moves]) :-
    writeln(Move),
    print_solution(Moves).

% Entry point to solve the problem
solve_problem :-
    initial_state(InitialState),
    solve(InitialState, Moves),
    write('Solution: '), nl,
    print_solution(Moves).
