# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:50:44 2020

@author: Ghulam Mursaleen
"""

from sklearn.metrics import confusion_matrix
y_true = [1, -1, 1, 1, -1]
y_pred = [-1, -1, -1, -1, -1]
print(confusion_matrix(y_true, y_pred))


from sklearn.metrics import confusion_matrix
y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, -1, -1, -1]
print(confusion_matrix(y_true, y_pred))

from sklearn.metrics import confusion_matrix
y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, 1, 1, -1]
print(confusion_matrix(y_true, y_pred))

from sklearn.metrics import confusion_matrix
y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, 1, 1, 1]
print(confusion_matrix(y_true, y_pred))


##########𝑇 𝑃 𝑅
#𝑇 𝑃
#𝑇 𝑃 𝐹 𝑁 
# 𝐹 𝑃 𝑅
#𝐹 𝑃
###𝐹 𝑃 𝑇 �

print( "TPR =>",3.0/(3+5)  )
print( "FPR =>",2.0/(2)  )


print( "TPR =>",3.0/(3+3)  )
print( "FPR =>",2.0/(2+2)  )

print( "TPR =>",3.0/(3+1)  )
print( "FPR =>",2.0/(2+4)  )

print( "TPR =>",3.0/(3+0)  )
print( "FPR =>",2.0/(2+5)  )



import numpy as np
from sklearn import metrics
y_true = [1, -1, 1, 1, -1]
y_pred = [-1, -1, -1, -1, -1]
y = np.array(y_true)
scores = np.array(y_pred)
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr, tpr, thresholds)


y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, -1, -1, -1]
y = np.array(y_true)
scores = np.array(y_pred)
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr, tpr, thresholds)


y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, 1, 1, -1]
y = np.array(y_true)
scores = np.array(y_pred)
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr, tpr, thresholds)


y_true = [1, -1, 1, 1, -1]
y_pred = [1, 1, 1, 1, 1]
y = np.array(y_true)
scores = np.array(y_pred)
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
print(fpr, tpr, thresholds)


from sklearn.metrics import confusion_matrix
y_true = [1, 1, -1, 1, -1,-1]
y_pred = [1, 1, 1, -1, -1,-1]
print(confusion_matrix(y_true, y_pred))