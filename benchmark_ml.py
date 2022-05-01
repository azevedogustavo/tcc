#Benachmark ml
##smallml.py
# teste na VM
vagrant@ubuntu-focal:~/Downloads/tcc/beanchmark$ python3 smallml.py 
/home/vagrant/.local/lib/python3.8/site-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
  from pandas import MultiIndex, Int64Index
X_train dimensions:  (6400000, 4) y_train:  (6400000,)
X_test dimensions: (1600000, 4) y_validation:  (1600000,)
X_train Percentage: 80.0 %
X_test Percentage: 20.0 %
/home/vagrant/.local/lib/python3.8/site-packages/xgboost/sklearn.py:1224: UserWarning: The use of label encoder in XGBClassifier is deprecated and will be removed in a future release. To remove this warning, do the following: 1) Pass option use_label_encoder=False when constructing XGBClassifier object; and 2) Encode your labels (y) as integers starting with 0, i.e. 0, 1, 2, ..., [num_class - 1].
  warnings.warn(label_encoder_deprecation_msg, UserWarning)
[17:32:08] WARNING: ../src/learner.cc:1115: Starting in XGBoost 1.3.0, the default evaluation metric used with the objective 'binary:logistic' was changed from 'error' to 'logloss'. Explicitly set eval_metric if you'd like to restore the old behavior.
XGB accuracy using Sklearn: 99.0 %
21.687929153442383 seconds

23.305925130844116 seconds

23.648573637008667 seconds

24.067704916000366 seconds

24.14048457145691 seconds

23.984363794326782 seconds

24.158748865127563 seconds

# beanchmark docker
/usr/local/lib/python3.8/dist-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
  from pandas import MultiIndex, Int64Index
X_train dimensions:  (6400000, 4) y_train:  (6400000,)
X_test dimensions: (1600000, 4) y_validation:  (1600000,)
X_train Percentage: 80.0 %
X_test Percentage: 20.0 %
/usr/local/lib/python3.8/dist-packages/xgboost/sklearn.py:1224: UserWarning: The use of label encoder in XGBClassifier is deprecated and will be removed in a future release. To remove this warning, do the following: 1) Pass option use_label_encoder=False when constructing XGBClassifier object; and 2) Encode your labels (y) as integers starting with 0, i.e. 0, 1, 2, ..., [num_class - 1].
  warnings.warn(label_encoder_deprecation_msg, UserWarning)
[18:03:41] WARNING: ../src/learner.cc:1115: Starting in XGBoost 1.3.0, the default evaluation metric used with the objective 'binary:logistic' was changed from 'error' to 'logloss'. Explicitly set eval_metric if you'd like to restore the old behavior.
XGB accuracy using Sklearn: 99.0 %
23.620540380477905 seconds

23.850480556488037 seconds

20.39276123046875 seconds

20.854780912399292 seconds

21.60218834877014 seconds

23.074546337127686 seconds


### singularitm smallml.py

/usr/local/lib/python3.8/dist-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
  from pandas import MultiIndex, Int64Index
X_train dimensions:  (6400000, 4) y_train:  (6400000,)
X_test dimensions: (1600000, 4) y_validation:  (1600000,)
X_train Percentage: 80.0 %
X_test Percentage: 20.0 %
/usr/local/lib/python3.8/dist-packages/xgboost/sklearn.py:1224: UserWarning: The use of label encoder in XGBClassifier is deprecated and will be removed in a future release. To remove this warning, do the following: 1) Pass option use_label_encoder=False when constructing XGBClassifier object; and 2) Encode your labels (y) as integers starting with 0, i.e. 0, 1, 2, ..., [num_class - 1].
  warnings.warn(label_encoder_deprecation_msg, UserWarning)
[18:35:51] WARNING: ../src/learner.cc:1115: Starting in XGBoost 1.3.0, the default evaluation metric used with the objective 'binary:logistic' was changed from 'error' to 'logloss'. Explicitly set eval_metric if you'd like to restore the old behavior.
XGB accuracy using Sklearn: 99.0 %
24.44339108467102 seconds

25.985453128814697 seconds

25.49546980857849 seconds

26.127426624298096 seconds

25.740644693374634 seconds

26.244760274887085 seconds

26.021884202957153 seconds

25.322711944580078 seconds

25.781932830810547 seconds


###

