from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from model_training import model, X_test, y_test

# Confusion Matrix
def plot_confusion_matrix(model, X_test, y_test):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

# plot_confusion_matrix(model, X_test, y_test)


# Feature Importance Plot
def plot_feature_importance(model, feature_names):
    importance = np.abs(model.coef_[0])
    idx = np.argsort(importance)
    plt.figure(figsize=(10,7))
    plt.barh(range(len(importance)), importance[idx])
    plt.yticks(range(len(importance)), [feature_names[i] for i in idx])
    plt.xlabel('Absolute Coefficient Magnitude')
    plt.title('Feature Importance in Logistic Regression Model')
    plt.show()

# plot_feature_importance(model)
    


def plot_roc_curve(model, X_test, y_test):
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()
    
plot_roc_curve(model, X_test, y_test)