% Define family relationships

parent(john, mary).
parent(john, adam).
parent(eve, mary).
parent(eve, adam).
parent(mary, anne).
parent(mary, tom).

% Define rules for different relationships

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

grandfather(Grandfather, Grandchild) :-
    grandparent(Grandfather, Grandchild),
    male(Grandfather).

grandmother(Grandmother, Grandchild) :-
    grandparent(Grandmother, Grandchild),
    female(Grandmother).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

brother(Brother, Sibling) :-
    sibling(Brother, Sibling),
    male(Brother).

sister(Sister, Sibling) :-
    sibling(Sister, Sibling),
    female(Sister).

% Define genders

male(john).
male(adam).
male(tom).

female(mary).
female(eve).
female(anne).
