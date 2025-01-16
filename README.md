# IPL Match Winner Prediction 
<div align="center">
    <img align="center" alt="IPL"  width="full" height="500" src="https://static.toiimg.com/thumb/msid-108684102,width-1280,height-720,imgsize-194624,resizemode-6,overlay-toi_sw,pt-32,y_pad-40/photo.jpg">
</div>

## ABSTRACT
<ul>
    <li>
        <p align="justify">Predicting the outcome of Indian Premier League (IPL) matches using machine learning algorithms has significant interest due to its potential to enhance strategic decision-making and fan engagement. In this paper, K-Means clustering are used to group the players based on their performance. Four classifiers namely, Random Forest, Decision Tree, Gaussian Naïve Bayes and Logistic Regression are used to develop predictive models. </p>
    </li>
</ul>

## METHODOLOGY
<ul>
    <li>
        <p align="justify">The proposed method has four phases namely i. Data Cleaning, ii. Feature Extraction, iii. Clustering Players based on the performance, and iv. Prediction. In this work, K-Means clustering algorithm is considered for finding the best player based performance. Four classification algorithms namely Random Forest, Decision Tree, Gaussian Naive Bayes and Logistic Regression are considered for the results and experiments. Figure 3.1 represents the flow diagram of proposed method.</p>
    </li>
</ul>

#### i. Data Cleaning
<ul>
    <li>
        <p align="justify">Data cleaning is the process of removing unwanted columns and missing values from the raw data. In this phase, if the row contains null values, missing values and NaN values then the columns are removed. The cleaned data is fed into the feature extraction phase.</p>
    </li>
</ul>

#### ii. Feature Extraction
<ul>
    <li>
        <p align="justify">In this phase, significant features are extracted using the pandas library. The features are extracted based on the player faced the balls, innings, runs, player out, batting average of batsman and  batting strike rate of batsman. The selected features are used to find the best players using k-means clustering.</p>
    </li>
</ul>

#### iii. Clustered Best player based on performance
<ul>
    <li>
<p align="justify">In this phase, the players are grouped using K-Means clustering based on their performance metrics namely batting average and bowling economy.</p>
    </li>
</ul>   

#### iv. Winning Prediction
<ul>
    <li>
        <p align="justify">In this phare, four classification algorithms were employed to forecast the output of clustered phare data. Random Forest yielded an accuracy of 99.89% in our experiments, followed by Decision Tree with 99.56%. Logistic Regression achieved an accuracy of 80.19%, while Gaussian Naive Bayes attained 63.93%. Notably, Random Forest outperformed the other algorithms, delivering the most accurate results.</p>
    </li>
</ul>

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
<ul>
    <li>
        <p align="justify">The dataset used in this research collected from the Kaggle website. In this paper there are two types of datasets. One is the IPL Match dataset, and another is the ball-by-ball dataset. The data set is a historical data from 2008 to 2022. Figure 3.1 and 3.2 represents the dataset description. Loading dataset to summarize the datatype and not null counts in Figure 3.3. 
Figure 3.4 represents the extracted features of the batsman's strike rate and average. 
</p>
    </li>
</ul>

<div align="center">
    <img align="center" alt="Match Datasets"  width="full" height="full" src="https://github.com/user-attachments/assets/6e6a41db-cbd3-4706-b8e9-c2b36f024a78">
    <h3>Fig 3.1 Viewing Match Datasets</h3>
</div>
<div align="center">
    <img align="center" alt="Ball-by-Ball Datasets"  width="full" height="full" src="https://github.com/user-attachments/assets/212bdfa7-77cb-425e-97c9-d45cbf778048">
    <h3>Fig 3.2 Viewing Ball-by-Ball Datasets</h3>
</div>
<div align="center">
    <img align="center" alt="Summary"  width="full" height="full" src="https://github.com/user-attachments/assets/313a17c5-ff6a-4bc4-854c-88ebbf128280">
    <h3>Fig 3.3 Data Summary</h3>
</div>
<ul>
    <li>
        <p align="justify">Then Figure 3.5 represents the performance metrics of the match's, runs, balls, batsman strike rate, batsman average, catches, player of the match, bowler strike rate, bowler economy, innings, and not out. Then the above data will be clustered using the K-Means that are shown in Figure 3.7. Finally, predict the winner by comparing four classification algorithms. The results are shown in Table 3.1 and Figure 3.8. Figure 3.9 represents the prediction on test data.</p>
    </li>
</ul>
<div align="center">
    <img align="center" alt="Feature Extraction"  width="full" height="full" src="https://github.com/user-attachments/assets/f61e7858-97e9-4204-84f3-e8c5fc88a740">
    <h3>Fig 3.4 Feature Extraction</h3>
</div>
<div align="center">
    <img align="center" alt="Team Performance"  width="full" height="full" src="https://github.com/user-attachments/assets/6cbd3ff9-587a-4804-8c75-c0a5c322ea6e">
    <h3>Fig 3.5 Team Performance</h3>
</div>
<div align="center">
    <img align="center" alt="Performance metrics"  width="full" height="full" src="https://github.com/user-attachments/assets/af701fe1-2f16-4721-8ad5-ed673717fce2">
    <h3>Fig 3.6 Performance metrics</h3>
</div>
<div align="center">
    <img align="center" alt="K-Means Cluster"  width="full" height="full" src="https://github.com/user-attachments/assets/27ca02a3-2bd6-4ff9-9d4e-de94671a311c">
    <h3>Fig 3.7 K-Means Cluster</h3>
</div>
<div align="center">
    <img align="center" alt="Visualizing Accuracy"  width="full" height="full" src="https://github.com/user-attachments/assets/733a1a16-b205-4429-96a9-97cd84609b84">
    <h3>Fig 3.8 Visualizing Accuracy</h3>
</div>
<div align="center">
    <img align="center" alt="Prediction"  width="full" height="full" src="https://github.com/user-attachments/assets/941b6ea5-a073-4622-80d6-090e2974ee8a">
    <h3>Fig 3.9 Prediction</h3>
</div>

## CONCLUSION
<ul>
    <li>
        <p align="justify">Proposed method used K-Means clustering algorithm to identify top player performances. Four classification algorithms are used to predict the outcomes. From the experiments results, Random Forest and Decision Tree classifiers provides 99.89% and 99.56% accuracy, while the Logistic Regression classifier achieved 80.19% and the Gaussian Naive Bayes classifier achieved 63.93%. The findings suggest that the Random Forest algorithm is the most effective for predicting IPL match winners.</p>
    </li>
</ul>

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

# Word File For Our Paper
 
