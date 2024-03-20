% Define facts about fruits and their colors
color_of(fruit, red).
color_of(apple, red).
color_of(banana, yellow).
color_of(grape, purple).
color_of(orange, orange).

% Define rules to find fruit based on color
fruit_of_color(Color, Fruit) :-
    color_of(Fruit, Color).

% Entry point for backtracking
find_fruit(Color, Fruit) :-
    fruit_of_color(Color, Fruit).

% Example usage:
% ?- find_fruit(red, Fruit).
% Fruit = fruit ;
% Fruit = apple.
