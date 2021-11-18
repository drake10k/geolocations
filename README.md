# geolocations

## Setup

1. install python 3.9.2
2. clone this repository
3. create a virtual environment
```
python -m venv venv
```
4. activate the virtual environment
5. upgrade pip
```
python -m pip install --upgrade pip
```
6. install bar_char_race custom fork
```
pip install git+https://github.com/drake10k/bar_chart_race.git
```
7. install dependencies
```
pip install -r requirements.txt
```
8. add your user agent (your e-mail recommended) inside [geolocations.py](geolocations.py)
9. execute geolocations.py
```
python geolocations.py
```

## Output
1. [countries.csv](data/countries.csv) - contains a list of all countries with their name, their alpha_2 and alpha_3 codes and their coordinates