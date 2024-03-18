% Define planets and their characteristics

planet(mercury, rocky, small, closest_to_sun).
planet(venus, rocky, medium, second_closest_to_sun).
planet(earth, rocky, medium, third_closest_to_sun).
planet(mars, rocky, small, fourth_closest_to_sun).
planet(jupiter, gas_giant, large, fifth_closest_to_sun).
planet(saturn, gas_giant, large, sixth_closest_to_sun).
planet(uranus, ice_giant, medium, seventh_closest_to_sun).
planet(neptune, ice_giant, medium, eighth_closest_to_sun).

% Query to retrieve characteristics of a planet
planet_characteristics(Planet, Type, Size, Position) :-
    planet(Planet, Type, Size, Position).
