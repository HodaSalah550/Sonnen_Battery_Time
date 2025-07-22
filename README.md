# 🔋 Battery Time Series Cleaner for Sonnen GmbH Corporate
This Python app loads time series data of battery usage in csv format which has a common data quality issues,
such as missing values, incorrect data types, and inconsistent formatting. 
This task is to develop an application that will transform and cleanse the data, 
and then write the cleaned data to an output file. 
whith an hourly summary.

## 📦 Features
- Cleans missing/invalid values
- Converts data types
- Removes duplicates
- Aggregates hourly data
- Flags hour with highest grid feed-in

## 🧱 Built With
- Python 3.10
- pandas
- Docker

## 🚀 How to Run

### Clone the Repo

```bash
git clone https://github.com/HodaSalah550/Sonnen_Battery_Time.git
cd Sonnen_Battery_Time


### Build Docker Image

```bash
docker build -t Sonnen_Battery_Time

### Run the App

```bash
docker run --rm -v "$PWD/input":/app/input -v "$PWD/output":/app/output Sonnen_Battery_Time




