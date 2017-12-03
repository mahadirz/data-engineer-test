# Data Engineer Assessment


The test consist of 4 questions. Except question 1, all questions consist of sub questions. The time given to solve it, 
is 7 days. 

## For question 2, to view visualization without executing the codes, use this link: https://s3.amazonaws.com/madet/Question%2B1%2Band%2B2.html

#### Question 1
A simple question which I believe to test efficiency to compute array/vector
##### Q1.Write a function in python to sum up a given set of numbers other than itself
Input: An array of n integers nums,<br>
Output: An array output such that output[i] is equal to the sum of all the elements
of nums except nums[i].<br>
For example, given [1,2,3,4], return [9,8,7,6].

#### Question 2
Is the hardest question of all 4, Mostly to test the statistics skill on interpreting data. I believe there are more 
than one way
to solve this question. I really looking forward to see other answers to this question.<br><br>

##### Q2.Sales Data Exploration and Analysis (code in python)
a) Write code to download the following Kaggle dataset:<br>

Weekly Sales Transaction Data: https://www.kaggle.com/crawford/weekly-sales-
transactions<br>

b) Identify the best performing product (based on volume)<br>
c) Identify the most promising product (emerging product)<br>
d) Identify the worst performing product on a biweekly basis<br>
e) Identify outliers from the data and output the corresponding week numbers<br>

#### Question 3
NLP type of questions. The second easier after q1. Not sure though the accuracy is the second 😜, but I think pretty accurate.

#####  Q3.Jobposts Data Exploration and Analysis (code in python)
a) Reuse code from Q2 to download the following Kaggle dataset:
Jobposts Data: https://www.kaggle.com/madhab/jobposts/<br>
b) Extract the following fields from the jobpost column:
1. Job Title
2. Position Duration
3. Position Location
4. Job Description
5. Job Responsibilities
6. Required Qualifications
7. Remuneration
8. Application Deadline
9. About Company<br>

c) Identify the company with the most number of job ads in the past 2 years<br>
d) Identify the month with the largest number of job ads over the years<br>
e) Find median, mean, min and max values for each product<br>
f) Clean text and generate new text from Job Responsibilities column: The new text
shall not contain any stop words, and the plural words shall be converted into
singular words.<br>
g) Store the results in a new Dataframe/SQL table<br>

#### Question 4
I think this one to test pipeline processing of data in distributed manner.

##### Q4.String similarity (code in python):
a) Download test.csv from https://www.kaggle.com/rishisankineni/text-similarity/data<br>
b) Load the data to a Spark/Pandas data frame<br>
c) Calculate similarity between description_x and description_y and store resultant
scores in a new column<br>
d) Parallelise the matching process (bonus)<br>

## Kaggle Dataset downloader
Duplicate the cred.json.example into cred.json and change the username and password.
```
$ cp cred.json.example cred.json
$ vim cred.json
```
