
"""Support Vector Machines machine-learning model

This script receives the clean datasets and trains a SVM machine-learning
model and test it on the clean open test and hidden test datasets. 
The function returns the lithofacies predictions obtained for the training,
open test, and hidden test sets.
"""

def run_SVM(train_norm, test_norm, hidden_norm):
  
  """Returns the predicted lithology classes for the training,
  open test, and hidden test obtained by SVM.

  Parameters
  ----------
  cleaned_traindata: Dataframe
    Starndardized training dataframe.
  cleaned_testdata: Dataframe
    Starndardized open test dataframe.
  cleaned_hiddendata: Dataframe
    Starndardized hidden test dataframe.

  Returns
  ----------
  train_pred_svm: one-dimentional array
    Predicted lithology classes obtained from the training dataset.
  test_pred_svm: one-dimentional array
    Predicted lithology classes obtained from the open test dataset.
  hidden_pred_svm: one-dimentional array
    Predicted lithology classes obtained from the hidden test dataset.
  """

  from sklearn.model_selection import train_test_split
  from sklearn.svm import SVC

  x_train = train_norm.drop(['LITHO'], axis=1)
  y_train = train_norm['LITHO']

  x_test = test_norm.drop(['LITHO'], axis=1)
  y_test = test_norm['LITHO']

  x_hidden = hidden_norm.drop(['LITHO'], axis=1)
  y_hidden = hidden_norm['LITHO']

  x_train_strat, X2, y_train_strat, Y2 = train_test_split(x_train,
                                                          y_train,
                                                          train_size=0.1,
                                                          shuffle=True,
                                                          stratify=y_train,
                                                          random_state=0
                                                          )
  # Definng SVM model with optimal hyper-parameters
  model_svm = SVC(kernel='rbf',
                  C=0.5,
                  cache_size=5000,
                  decision_function_shape='ovr'
                  )
  # fitting SVM model
  model_svm.fit(x_train_strat, y_train_strat)

  # predicting
  train_pred_svm = model_svm.predict(x_train)
  test_pred_svm = model_svm.predict(x_test)
  hidden_pred_svm = model_svm.predict(x_hidden)

  return train_pred_svm, test_pred_svm, hidden_pred_svm