# Neural Networks 

## Logistic Regression 

- Used for Binary Classification 
- y = wx + b need to be set on the given points 
- `sigmoid activation function` basically gives value between 0 to 1 
- In vector form, y = sigmoid(w(transpose)x). b is accomadted another w0 

- ## Loss function and Cost function 
- loss is for each data point and cost is for all the data points
- we however dont use this, since it gives local optimum points 
    - we instead make use of ```L(y',y) = - (y*log(y') + (1-y)*log(1-y')```

- Cost Function: ```J(w,b) = (1/m) * Sum(L(y'[i],y[i]))```

- ## Gradient Descent 

- We essentailly want to minimize the Cost function using the w and b value
 

