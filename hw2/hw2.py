from sklearn import datasets
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
import argparse


def load_iris_data():
    # loads iris dataset 

    iris = datasets.load_iris()

    return (iris.data, iris.target, iris.target_names)


def knn(X_train, y_train, k_neighbors = 3):
    # method returns a kNN object called clf with methods:
    #     score(X_test, y_test) --> to score the model using a test
    #     predict(X_classify, y_test) --> to predict a result using

    clf = KNeighborsClassifier(k_neighbors)
    clf.fit(X_train, y_train)

    return clf

def naive_bayes(X_train, y_train):
    # method returns a NB object called clf with methods

    clf = GaussianNB()
    clf.fit(X_train, y_train)

    return clf


def log_reg(X_train, y_train,C_param):
    # method returns a logistic regression object called clf

    clf = LogisticRegression(C=C_param)
    clf.fit(X_train, y_train)

    return clf



def cross_validate(XX, yy, classifier, k_fold,c):
    # function returns generic cross validation

    # derive a set of random training and testing indices
    k_fold_indices = KFold(len(XX), n_folds=k_fold, indices=True, shuffle=True, random_state=0)

    k_score_total = 0
    # for each training and testing slice, run the classifier and score
    for train_slice, test_slice in k_fold_indices:

        model = classifier(XX[[ train_slice ]],
                           yy[[ train_slice ]],c)

        k_score = model.score(XX[[ test_slice ]],
                              yy[[ test_slice ]])

        # score each slice and average to determine performance of model
        k_score_total += k_score

    return k_score_total*1.0/k_fold


