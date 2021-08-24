## Water Potability Project

### Table of contents
1. [Introduction](#Introduction)
2. [Getting Started](#GettingStarted)
    1. [Dependency](#Dependencies)
    2. [Installation](#Installation)
    3. [Executing Program](#Execution)
3. [Authors](#Authors)
4. [License](#License)
5. [Acknowledgement](#Acknowledgement)
6. [Screenshots](#Screenshots)

## Introduction <a name='Introduction'></a>
This goal of this project is to a build a machine learning model that can classify water potability
based on pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes 
and Turbidity.

1. pH value:
PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.

2. Hardness:
Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.

3. Solids (Total dissolved solids - TDS):
Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.

4. Chloramines:
Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.

5. Sulfate:
Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.

6. Conductivity:
Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.

7. Organic_carbon:
Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.

8. Trihalomethanes:
THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.

9. Turbidity:
The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.

10. Potability:
Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.

The project is divided into following sections
1. ETL Pipeline that loads data from files, cleans data and then saves in a sqlite database
2. Machine Learning Pipeline that normalizes and trains model to be used for classifying messages
3. Web application that takes above-mentioned parameters as input and predicts the potability of water in real time
 
## Getting Started <a name='GetStarted'></a>
### Dependencies <a name='Dependencies'></a>
Following packages were used in this project
* numpy
* sklearn
* seaborn
* matplotlib
* joblib
* flask

### Installation <a name='Installation'></a>
* Clone this repository by executing `git clone https://github.com/sumitkumar-00/water-potability`
* Install required packages by executing `pipenv install` in the project's root directory

### Executing program <a name='Execution'></a>
1. Run following commands in project's root directory
   1. To execute ETL pipeline `pipenv run python data/process_data.py data/water_potability.csv data/water_potability.db`
   2. To execute ML pipeline `pipenv run python models/train_classifier.py data/water_potability.db models/water_potability.pkl`
   3. To run web app execute `pipenv run python run.py` from app's directory
2. Go to http://127.0.0.1:3001 to check out the app 

## Authors <a name='Authors'></a>
. [Sumit Kumar](https://github.com/sumitkumar-00)
## License <a name='License'></a>
Feel free to make changes
## Acknowledgement <a name='Acknowledgement'></a>
I would like to thank Kaggle making this data available
## Screenshots <a name='Screenshots'></a>         
![charts](static/images/screenshot.png)
![charts](static/images/correlation.png)




