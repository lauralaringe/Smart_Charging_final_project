# Smart_Charging_final_project
# Final Project CAPUEE

This project will involve the use of electric devices such as mobile phones and laptops in an office or home environment. The main goal is to control the charging period of these devices in order to avoid overcharging. Additionally, the charging of these devices will automatically be triggered during the night time when electricity prices are lower. The outcome of this project will allow devices such as mobile phones and computers to receive the exact amount of charge required to reach maximum capacity while ensuring efficient energy usage. The expected intention of this project is to hopefully create a ‘smart office’ where electricity is utilized in the most efficient way possible when it comes to charging of electric devices. 

# Guide to files

Get_data_RE.ipynb and Get_data.ipynb are Jupyter Notebook code to visualize the data got from the APIs to get respectively price data, irradianca and wind power data.

RE_Data.py, Red_Electrica_Data.py and main.py are the code that run on the RaspBerry Pi and control di Arduino. main.py calls the funcions in the other to files to get data from the APIs

Optimization_problem.py gets data from the API and plots it. It is used to make calculations and test for the optimization problem.

The Arduino code folder contains the code that runs on the arduino which reads the current from the current sensor and changes the status of the relay based on the high or low signal incoming from the python code


# Status
Completed
