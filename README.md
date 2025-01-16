# IPL Match Winner Prediction 
<div align="center">
    <img align="center" alt="IPL"  width="full" height="500" src="https://static.toiimg.com/thumb/msid-108684102,width-1280,height-720,imgsize-194624,resizemode-6,overlay-toi_sw,pt-32,y_pad-40/photo.jpg">
</div>

## ABSTRACT
<p align="justify">    Predicting the outcome of Indian Premier League (IPL) matches using machine learning algorithms has significant interest due to its potential to enhance strategic decision-making and fan engagement. In this paper, K-Means clustering are used to group the players based on their performance. Four classifiers namely, Random Forest, Decision Tree, Gaussian Naïve Bayes and Logistic Regression are used to develop predictive models. </p>

## METHODOLOGY
<p align="justify">    The proposed method has four phases namely i. Data Cleaning, ii. Feature Extraction, iii. Clustering Players based on the performance, and iv. Prediction. In this work, K-Means clustering algorithm is considered for finding the best player based performance. Four classification algorithms namely Random Forest, Decision Tree, Gaussian Naive Bayes and Logistic Regression are considered for the results and experiments. Figure 3.1 represents the flow diagram of proposed method.</p>

#### i. Data Cleaning
<p align="justify">Data cleaning is the process of removing unwanted columns and missing values from the raw data. In this phase, if the row contains null values, missing values and NaN values then the columns are removed. The cleaned data is fed into the feature extraction phase.</p>

#### ii. Feature Extraction
<p align="justify">In this phase, significant features are extracted using the pandas library. The features are extracted based on the player faced the balls, innings, runs, player out, batting average of batsman and  batting strike rate of batsman. The selected features are used to find the best players using k-means clustering.</p>

#### iii. Clustered Best player based on performance
<p align="justify">In this phase, the players are grouped using K-Means clustering based on their performance metrics namely batting average and bowling economy.</p>

#### iv. Winning Prediction
<p align="justify">In this phare, four classification algorithms were employed to forecast the output of clustered phare data. Random Forest yielded an accuracy of 99.89% in our experiments, followed by Decision Tree with 99.56%. Logistic Regression achieved an accuracy of 80.19%, while Gaussian Naive Bayes attained 63.93%. Notably, Random Forest outperformed the other algorithms, delivering the most accurate results.</p>


###### 6.1 Decision Tree Algorithm
<ul>
    <li>
        <p align="justify">Decision Tree is a supervised learning technique that can be used for classification.</p>
    </li>
</ul>

###### 6.2 Random Forest Algorithm
<ul>
    <li>
        <p align="justify">Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. </p>
    </li>
</ul>

###### 6.3 Logistic Regression Algorithm
<ul>
    <li>
        <p align="justify">Logistic regression algorithm is used for predicting the categorical dependent variable using a given set of independent variables. Logistic regression predicts the output of a categorical dependent variable. </p>
    </li>
</ul>


###### 6.4 Gaussian Naive Bayes Algorithm
<ul>
    <li>
        <p align="justify">Gaussian Naive Bayes is a type of Naive Bayes method where continuous attributes are considered and the data features follow a Gaussian distribution throughout the dataset. </p>
    </li>
</ul>

#### IV. Results and Discussion
<p align="justify">The dataset used in this research collected from the Kaggle website. In this paper there are two types of datasets. One is the IPL Match dataset, and another is the ball-by-ball dataset. The data set is a historical data from 2008 to 2022. Figure 3.1 and 3.2 represents the dataset description. Loading dataset to summarize the datatype and not null counts in Figure 3.3. 
Figure 3.4 represents the extracted features of the batsman's strike rate and average. 
</p>


### Use Payload on the Following example

```bash
{
    "BattingTeam": "Chennai Super Kings",
    "BowlingTeam": "Mumbai Indians",
    "City": "Mumbai",
    "runs_left": 12,
    "balls_left": 3,
    "wickets_left": 5,
    "current_run_rate": 7,
    "required_run_rate": 10,
    "target": 173
}
```


### And only use the Team Name Must on the Following Content
<div>
    <ul>
        <li>Rajasthan Royals</li>
        <li>Royal Challengers Bangalore</li>
        <li>Sunrisers Hyderabad</li>
        <li>Delhi Capitals</li>
        <li>Chennai Super Kings</li>
        <li>Gujarat Titans</li>
        <li>Lucknow Super Giants</li>
        <li>Kolkata Knight Riders</li>
        <li>Punjab Kings</li>
        <li>Mumbai Indians</li>
    </ul>
</div>
