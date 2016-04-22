# SEMS
S(mart) E(lectricity) M(management) S(system) aims to help reduce your electrical bill while using renewable energy to help the environment.
This project helps user manage their electricity expenditure by using a solar panel mounted ona motor and equipped with light sensors in order to track the motion of the sun in the sky in order to do 2 things :
1- provide electricity to the lights
2- keep the batteries charged
Inside the house, each room, depending on its size, is equipped with light sensors and led lights.
Once the software is up and running, it will do the following:
* check the luminosity in the room through the light sensors and compensate to keep and optimal lighting, through the dimming of the led lights (less if the sunlight is enough and more when it's not)
* the motor turns the solar panel to follow the sun, based on the input of the light sensors mounted on it, until it finds the optimal location, where both sensors have almost the same readings (+ or - 10%).
* when the light sensors mounted on the solar panel read a very low value, it might mean that the sun is down so the motor shuts down to preserve energy.
* the energy source for the lighting inside the house is from the battery charged through the solar panel. Once drained, the system automatically switches to the electrical current.

Team members :
* KHOURY Elie
* KHOURY Jean-Pierre
* ODEIMY Edwin 
