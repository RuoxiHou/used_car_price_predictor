Based on more than 10K usable data records scraped from a website for used car offers, the price predictor was trained and validated and eventually tested with the ability of explaining more than 91% of the variance from the data collected. 
The purposes of building this predictor is to facilitate the decision making process for used car buyers to know if the new offer is with a reasonable price or not, and for the car sellers to make a price proposal on their used cars.

Data Collection:
- 3 rounds of Web scraping by using Selenium to gather data for the used car prices
- Collect comments in each car brand's subreddit from App Reddit by using PRAW Python Reddit API
- Manually save the car logos for the Data Visualization in Power BI

Data Cleaning:
- Missing value handling
- Currency conversion
- Duplicate information deletion

NLP:
Sentiment Intensity Analysis for the comments in Reddit
- Emoji-to-Text
- Tokenization
- Lemmatization
- Stop Words
- Sentiment Intensity Analyzer

EDA:
- Matplotlib
- Seaborn

Power BI Dashboard

Machine Learning:
- Auto ML (PyCaret)
- pipeline
- Feature engineering (One-hot encoding & Target Encoding)
- XGBoost Regressor

Web design:
Flask

