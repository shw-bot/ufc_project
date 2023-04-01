# UFC Project
This project analyzes data from the Ultimate Fighting Championship (UFC) and will eventually build machine learning models to predict the outcomes of future fights.
The analysis provided attempted to find trends specifically from the fighter data, and was able to pinpoint how a fighter's Stance affects their chance of winning.

All data was pulled from [official UFC statistics](ufcstats.com)

# Installation
To run this project, you will need to have Python 3.9 or higher installed on your system. You will also need to have Git installed to clone the repository.

### 1. Clone the repository to your local machine:
- git clone https://github.com/shw-bot/ufc_project
### 2. Navigate to the directory and open using a prompt or an IDE
### 3. Create and activate a virtual environment using a prompt or IDE
### 4. Install the required libraries
- pip install -r requirements.txt

## If You Are Running the Cleaning and Analysis in Jupyter Notebook:

- Follow the directions above for your desired terminal
- Run Jupyter from the virtual environment
- Open the cloned project folder using Jupyter notebook
- Open ufc_data_cleaning.ipynb and or ufc_fighter_analysis.ipynb
- Click Cell tab and then Run All

# Usage
## If You Want to Scrape the Most Recent Data
### To use the scraper, follow these steps:
- Open and run fights_to_csv.py
- Note that this can take over 20 minutes
- It will save the data as a csv file, which can be called in later programs in order to expedite the process
- Next, open and run fighters_to_csv.py
- Note this can sometimes take 5 or more minutes
- This data is also saved in a separate csv file

## Cleaning
### To clean the scraped data, follow these steps:
- Open and run cleaning.py in your IDE
- The data will be saved to new csv files, which can then be analyzed even easier
- Alternatively, you can use the ufc_data_cleaning.ipynb notebook for easy visualization of the cleaning process

## Analysis
### To analyze the cleaned data, follow these steps:
- Open and run the analysis.py file to generate graphs based on the cleaned data
- Alternatively, you can use the ufc_fighter_analysis.ipynb notebook for easy visualization of the analysis

# Important Vocab:

### Fighter Data:
- Ht.: Height
- Wt.: Weight
- Open Stance: The feet are spaced wider with the front toe toward the opponent and the rear foot at 45 degrees
- Orthodox: Fighters stand with their left foot in front and their right foot in the back. Right hand is connected to chin or head, while left hand is in the lead.
- Southpaw: Fighter has the right hand and the right foot forward, leading with right jabs, and following with a left cross right hook. It is the normal stance for a left-handed boxer.
- Sideways: Any guard in which the front foot is turned inward.
- Switch: Fighter switches between different stances.
- W: Win
- L: Loss
- D: Draw

### Fight Data:
- Kd: Knock-down rate per 15min fight time
- Str: Number of Significant Strikes
- Td: Number of Take-downs
- Sub: Number of Submissions
### Methods
- U-DEC: Unanimous decision by judges (if not finished by KO or TKO)
- S-DEC: 3 Judges pick different winners 1:2 (if not finished by KO or TKO)
- M-DEC: 2/3 judges pick a winner, 1 judge says draw (if not finished by KO or TKO)
- SUB: Loser taps out
- KO: Loser is knocked unconscious
- TKO: Technical KO, ref call fight due to severity of strikes/impact


# Project Code Files:

- **fights_to_csv.py**: Webscraper for historic fight information --> csv
- **fighters_to_csv.py**: Webscraper for individual fighter information --> csv
- **cleaning.py**: Cleans fight + fighter data --> csv
- **analysis.py**: Analysis --> graphs
- **ufc_data_cleaning.ipynb**: Jupyter Notebook for easy visualization of cleaning
- **ufc_fighter_analysis.ipynb**: Jupyter Notebook for easy visualization of analysis
- **requirements.txt**: Required libraries to run the program

# What's Next?

The intent of this project is to eventually build a predictive model for UFC Fight outcomes. The analysis provided by the current project gives a great starting point to show what data will be important to consider when training the model.
