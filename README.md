# Bayesian-Network-Location
The project is centered on developing an AI to pinpoint a stealthy monkey's location within a grid-represented ballroom, leveraging Bayesian networks to interpret data from motion and sound sensors. 

Monkey Tracking AI Project
Overview
In an amusing twist of events reminiscent of 1976, a group of rhesus monkeys has once again escaped from the Memphis Zoo and ventured into the Rhodes College campus. All but one mischievous monkey have been recaptured. This project outlines the development of an AI solution tasked with tracking down the elusive monkey using a combination of motion and sound sensors placed within the BCLC ballroom at Rhodes College.

# Project Description
The Challenge
The last remaining monkey has taken refuge in the spacious BCLC ballroom, expertly evading detection. Given the difficulty in visually locating the monkey, we have deployed an AI-based approach to monitor its movements and predict its location within the ballroom, which is represented as a two-dimensional grid.

# System Architecture
Motion Sensors
Two basic motion sensors are positioned at opposite corners of the ballroom. Their detection capabilities are limited to their immediate vicinity and orthogonal directions, leaving significant areas of the grid unmonitored.

# Sound Sensors
To complement motion detection, sound sensors are installed throughout the ballroom. These sensors can pinpoint the monkey's location with varying degrees of accuracy, accounting for potential errors in determining the exact square.

# AI Implementation
The core of this project is the development of a dynamic Bayesian network that integrates data from both motion and sound sensors to estimate the monkey's location over time. The network adjusts its predictions based on sensor inputs, updating the probability distribution of the monkey's position with each new reading.

# Operation
Upon receiving sensor data, the program calculates the likelihood of the monkey's presence in each grid square, factoring in the potential inaccuracies of each sensor type. This process iteratively refines the estimation of the monkey's current location, enabling more targeted efforts to recapture it.

# Usage
To utilize the program, users are prompted to input a sequence of sensor readings via a text file. This file specifies the grid size and contains lines of sensor data corresponding to different time steps. The program outputs the probability distribution of the monkey's location at each time step, aiding in its eventual capture.

# Conclusion
This project showcases the application of AI in addressing real-world challenges, specifically in wildlife management and the recapture of escaped animals. Through the integration of sensor data and Bayesian inference, we demonstrate the potential of AI to solve complex, dynamic problems in innovative ways.

