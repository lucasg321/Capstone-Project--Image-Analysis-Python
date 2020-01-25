# Capstone-Project--Image-Analysis-Python
Image analysis via Python with OpenCV and numPy

The goal of the project is to anlayze soil and agricultural land conditions via drone mounted sensors. 

The image anlysis portion of the project utilizes Python with numPy and OpenCV to analyse images taken from a drone and match the soil color/hue to a database of over 300 samples of soil. This allows us to determine such things as the fertility of the soil. On the hardware side, an ATmega328P microcontroller is used to connect a LiDAR sensor to an SD card and store distance and signal strength values while the drone is in flight. The distance values are then used to create a topographical view of the land. In combination, the soil fertility measurements and land topography will allow us to provide recommendations for land use in order to optimize crop yields. Signal strength values from the LiDAR are currently being experimented with to record additional characteristics of the soil, such as Albedo. 
