# IPL Match Winner Prediction 

## ABSTRACT
<p style="text-align: justify;">Predicting the outcome of Indian Premier League (IPL) matches using machine learning algorithms has significant interest due to its potential to enhance strategic decision-making and fan engagement. In this paper, K-Means clustering are used to group the players based on their performance. Four classifiers namely, Random Forest, Decision Tree, Gaussian Naïve Bayes and Logistic Regression are used to develop predictive models. </p>

## METHODOLOGY
<p style="text-align: justify;">The proposed method has four phases namely i. Data Cleaning, ii. Feature Extraction, iii. Clustering Players based on the performance, and iv. Prediction. In this work, K-Means clustering algorithm is considered for finding the best player based performance. Four classification algorithms namely Random Forest, Decision Tree, Gaussian Naive Bayes and Logistic Regression are considered for the results and experiments. Figure 3.1 represents the flow diagram of proposed method.</p>

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
