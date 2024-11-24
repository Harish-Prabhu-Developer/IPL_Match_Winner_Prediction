"# IPL_Match_Winner_Prediction" 





#Use Payload on the Following example
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


#And only use the Team Name Must on the Following Content

'Rajasthan Royals',
'Royal Challengers Bangalore',
'Sunrisers Hyderabad',
'Delhi Capitals',
'Chennai Super Kings',
'Gujarat Titans',
'Lucknow Super Giants',
'Kolkata Knight Riders',
'Punjab Kings',
'Mumbai Indians'








'# ABOUT THE PROJECT'


PREDICTING IPL MATCH WINNER USING MACHINE LEARNING TECHNIQUES
Mr. S. Harish Prabhu
I MCA,
Department of Computer Applications, 
Ayya Nadar Janaki Ammal College,
Sivakasi, Tamil Nadu, India	



ABSTRACT
Predicting the outcome of Indian Premier League (IPL) matches using machine learning algorithms has significant interest due to its potential to enhance strategic decision-making and fan engagement. In this paper, K-Means clustering are used to group the players based on their performance. Four classifiers namely, Random Forest, Decision Tree, Gaussian Naïve Bayes and Logistic Regression are used to develop predictive models. 

Keywords: Classification, Clustering, IPL, K-Means Cluster, Random Forest, Decision Tree Classifier.

I. INTRODUCTION
In computer science, machine learning is a subfield of artificial intelligence that employs statistical techniques to let computers learn from data without requiring explicit programming. The Indian Premier League (IPL) stands as one of the most captivating and widely-followed cricket tournaments globally. This work is useful for the predictive models by knowing the strengths and weaknesses of the teams. Team management can use this knowledge to develop game plans, change team compositions, and make decisions.

II. LITERATURE REVIEW
Tripathi et al. [1] have focused on machine learning to predict winners in IPL matches, addressing the growing need for accurate forecasts due to increased viewership and advertising. It employs various methods to define a dataset, extract essential features, and tackle issues like data symmetry. Tree-based classifiers, particularly Random Forest, outperformed other algorithms, offering 60.043% accuracy and addressing model ambiguity. Kamel et al. [2] have Cancer, a global menace, remains without a definitive cure. Early detection is paramount for patient survival, as late-stage diagnosis drastically reduces chances of recovery. Hence, accurate and timely diagnosis is critical. This study employs Gaussian Naive Bayes algorithm for cancer classification, achieving 98% accuracy in predicting breast cancer and 90% in predicting lung cancer across two datasets. Jayaprakash et al. [3] have surge in education sector demands has spurred research on student academic performance and behavior analysis. Machine learning in Education Data Mining extracts insights, forecasts student performance, and identifies influential factors. Implementing predictive mechanisms aids prompt intervention. 

Kavitha et al. [4] have proposed a multivariable linear regression model to predict IPL match outcomes. Multivariable linear regression provides the improved performance over traditional linear regression. Zelaya has [5] addresses the machine learning models, particularly focusing on algorithmic transparency and fairness and highlighted the significance of decisions made during data preprocessing. Sinha [6] has introduced a machine learning model for predicting IPL match outcomes using Naive Bayes and Euler's Formula. 
Ghazal et al. [7] Clustering involves grouping data based on similar properties, categorizing them into clusters where elements share similarities. K-means, a popular clustering algorithm, measures distances between data points and centroids to assign them to the nearest cluster. Various distance metrics, such as Manhattan distance, impact execution time and cluster creation. Evaluation of K-means with different metrics reveals Manhattan distance achieves optimal results in most cases, highlighting the influence of distance metrics on algorithm performance. 
Sameer et al. [8] have predicted cardiovascular diseases using feature extraction and Decision Tree and K-nearest neighbor algorithms. Reddy et al. [9] have proposed a logistic regression and extra gradient boost techniques to enhance human activity recognition, specifically for walking and sitting. Mustafa et al. [10] have predicted cricket match winners using total tweets for each team, fan sentiment, and fan score predictions. The study shown the Support Vector Machine (SVM) outperforms than other classifiers.

III.METHODOLOGY
The proposed method has four phases namely i. Data Cleaning, ii. Feature Extraction, iii. Clustering Players based on the performance, and iv. Prediction. In this work, K-Means clustering algorithm is considered for finding the best player based performance. Four classification algorithms namely Random Forest, Decision Tree, Gaussian Naive Bayes and Logistic Regression are considered for the results and experiments. Figure 3.1 represents the flow diagram of proposed method. 








Fig. 3.1 Methodology
i. Data Cleaning
Data cleaning [5] is the process of removing unwanted columns and missing values from the raw data. In this phase, if the row contains null values, missing values and NaN values then the columns are removed. The cleaned data is fed into the feature extraction phase. 

ii. Feature Extraction
In this phase, significant features are extracted using the pandas library. The features are extracted based on the player faced the balls, innings, runs, player out, batting average of batsman and  batting strike rate of batsman. The selected features are used to find the best players using k-means clustering.  

iii. Clustered Best player based on performance
In this phase, the players are grouped using K-Means clustering [7] based on their performance metrics namely batting average and bowling economy. K-Means Cluster Algorithm is explained in Procedure 1. 
Procedure - 1
Step-1: Select the number K to decide the number of clusters.
Step-2: Select random K points or centroids. 
Step-3: Assign each data point to their closest centroid, which will form the predefined K clusters.
Step-4: Calculate the variance and place a new centroid of each cluster.
Step-5: Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.
Step-6: If any reassignment occurs, then go to step-4 else go to FINISH.
Step-7: The model is ready.

iv. Winning Prediction
In this phare, four classification algorithms were employed to forecast the output of clustered phare data. Random Forest yielded an accuracy of 99.89% in our experiments, followed by Decision Tree with 99.56%. Logistic Regression achieved an accuracy of 80.19%, while Gaussian Naive Bayes attained 63.93%. Notably, Random Forest outperformed the other algorithms, delivering the most accurate results.
6.1 Decision Tree Algorithm
Decision Tree [8] is a supervised learning technique that can be used for classification. Decision tree algorithm is explained in Procedure 2.
Procedure 2
Step-1: Begin the tree with the root node S, which contains the complete dataset.
Step-2: Find the best attribute in the dataset.
Step-3: Divide the S into subsets that contains possible values for the best attributes.
Step-4: Generate the decision tree node using the best attribute.
Step-5: Repeat step-3. Continue this process until a stage is reached.
6.2 Random Forest Algorithm
Random Forest is [3] a popular machine learning algorithm that belongs to the supervised learning technique. 
Random forest algorithm is explained in Procedure 2. 
Procedure 2
Step-1: Select random K data points from the training set.
Step-2: Build the decision trees associated with the selected data points.
Step-3: Choose the number N for decision trees that the user want to build.
Step-4: Repeat Step 1 & 2.
Step-5: find the predictions of each decision tree, and assign the new data points to the category.
6.3 Logistic Regression Algorithm
Logistic regression algorithm [9] is used for predicting the categorical dependent variable using a given set of independent variables. Logistic regression predicts the output of a categorical dependent variable. Logistic regression algorithm is explained in Procedure 3.
Procedure 3 
Step-1: Convert the given dataset into frequency tables.
Step-2: Generate Likelihood table by finding the probabilities of given features.
Step-3: Finding the prior probability value. 
Step-4: Calculating the conditional probability value.
Step-5: By comparing the conditional probability values we will predict the results.
6.4 Gaussian Naive Bayes Algorithm
Gaussian Naive Bayes [2] is a type of Naive Bayes method where continuous attributes are considered and the data features follow a Gaussian distribution throughout the dataset. 
IV. Results and Discussion
The dataset used in this research collected from the Kaggle website. In this paper there are two types of datasets. One is the IPL Match dataset, and another is the ball-by-ball dataset. The data set is a historical data from 2008 to 2022. Figure 3.1 and 3.2 represents the dataset description. Loading dataset to summarize the datatype and not null counts in Figure 3.3. 
Figure 3.4 represents the extracted features of the batsman's strike rate and average. 

 

Fig 3.1 Viewing Match Datasets

 

Fig 3.2 Viewing Ball-by-Ball Datasets


 

Fig 3.3 Data Summary



Then Figure 3.5 represents the performance metrics of the match's, runs, balls, batsman strike rate, batsman average, catches, player of the match, bowler strike rate, bowler economy, innings, and not out. Then the above data will be clustered using the K-Means that are shown in Figure 3.7. Finally, predict the winner by comparing four classification algorithms. The results are shown in Table 3.1 and Figure 3.8. Figure 3.9 represents the prediction on test data.

 

Fig 3.4 Feature Extraction

 
Fig 3.5 Team Performance

 

Fig 3.6 Performance metrics
 
Fig 3.7 K-Means Cluster
 
Fig 3.8 Visualizing Accuracy  
               
Fig 3.9 Prediction

Table 3.1 Comparing four algorithms.
S.No.	Classifier Algorithms	Accuracy
1.	Decision Tree 	99.56
2.	Logistic Regression 	80.19
3.	Random Forest 	99.89
4.	Gaussian Naïve Bayes 	63.93

V.CONCLUSION
Proposed method used K-Means clustering algorithm to identify top player performances. Four classification algorithms are used to predict the outcomes. From the experiments results, Random Forest and Decision Tree classifiers provides 99.89% and 99.56% accuracy, while the Logistic Regression classifier achieved 80.19% and the Gaussian Naive Bayes classifier achieved 63.93%. The findings suggest that the Random Forest algorithm is the most effective for predicting IPL match winners.
VI.REFERENCES
[1] Tripathi, A., Islam, R., Khandor, V., & Murugan, V. (2020). Prediction of IPL matches using Machine Learning while tackling ambiguity in results. Indian J. Sci. Technol, 13(38), 4013-4035.
[2] Kamel, H., Abdulah, D., & Al-Tuwaijari, J. M. (2019, June). Cancer classification using gaussian naive bayes algorithm. In 2019 international engineering conference (IEC) (pp. 165-170). IEEE.
[3] Jayaprakash, S., Krishnan, S., & Jaiganesh, V. (2020, March). Predicting students academic performance using an improved random forest classifier. In 2020 international conference on emerging smart computing and informatics (ESCI) (pp. 238-243). IEEE.
[4] Kavitha, P. V., Sai Pavitra, R., Suwetha, K., & Uvashree, P. (2022). IPL Win Prediction Using Machine Learning. In Disruptive Technologies for Big Data and Cloud Applications: Proceedings of ICBDCC 2021 (pp. 457-465). Singapore: Springer Nature Singapore.
[5] Zelaya, C. V. G. (2019, April). Towards explaining the effects of data preprocessing on machine learning. In 2019 IEEE 35th international conference on data engineering (ICDE) (pp. 2086-2090). IEEE.
[6] Sinha, A. (2020). Application of Machine Learning in Cricket and Predictive Analytics of IPL 2020.
[7] Ghazal, T. M. (2021). Performances of k-means clustering algorithm with different distance metrics. Intelligent Automation & Soft Computing, 30(2), 735-742.
[8] Sameer, S. K. L., & Sriramya, P. (2024, February). Improving the prediction accuracy in detection of heart disease patients with novel feature extraction scheme and classifying the patient records by decision tree classifier comparing with KNN classifier algorithms. In AIP Conference Proceedings (Vol. 2729, No. 1). AIP Publishing.
[9] Reddy, L. A. K., & Padmakala, S. (2024). Human Activity Recognition on Smartphones using Innovative Logistic Regression and Comparing Accuracy of Extra Gradient Boost Algorithm. In E3S Web of Conferences (Vol. 491, p. 03024). EDP Sciences.
[10] Mustafa, R. U., Nawaz, M. S., Lali, M. I. U., Zia, T., & Mehmood, W. (2017). Predicting the cricket match outcome using crowd opinions on social networks: A comparative study of machine learning methods. Malaysian Journal of Computer Science, 30(1), 63-76.

