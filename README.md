# Linear-Regression
The attached dataset “diabetic_kidney_disease.csv” contains 110 records of patients with 
diabetic kidney disease. We need to examine the relation between fasting blood glucose (FBG) 
and urinary albumin creatinine ratio (UACR) because kidney disease is a common complication 
of diabetes.
Write a python program that uses linear regression with gradient descent to predict the value 
of UACR based on the FBG of a patient since this value can be used for early detection of kidney 
disease in diabetic patients.
Note: You will need to normalize the data before applying linear regression. You can use minmax 
normalization where z is the normalized value and z = (x – min) / (max – min).
So, given the hypothesis function Y = C1 + C2 X;
Y (target variable) = UACR, X (predictor) = FBG, C1 and C2 are the parameters of the function:
1. Split the data into 2 parts: training and testing. Choose the value of learning rate and the 
number of iterations.
2. Implement gradient descent to optimize the parameters of the function (C1 and C2).
3. Calculate the error of the hypothesis function to see how it changes with every iteration. 
(Hint: You will need to calculate the error in every iteration.)
4.Use optimized hypothesis function to make predictions on new data.
5. Try different values of the learning rate and the iterations to see how this changes the 
accuracy of the model. 
6. Plot the initial line that you started with and at the end, plot the line produced from linear 
regression (the line that best fits the data).
