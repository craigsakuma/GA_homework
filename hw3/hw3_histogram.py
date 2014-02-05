import matplotlib
matplotlib.use("AGG")
from matplotlib import pyplot as plt
import numpy as np

plt.figure(1)

for t,marker,c in zip(xrange(2),"ox","rb") :
    # We plot each class on its own to get different colored markers
    # zip creates tuples
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])

    plt.savefig('iris_plot1.png')
    #plt.close()

plt.figure(2)

for t,marker,c in zip(xrange(3),">ox","rgb") :
    plt.scatter(features[target == t,0],
                features[target == t,2],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[2])

    plt.savefig('iris_plot2.png')
    #plt.clf()

plt.figure(3)

for t,marker,c in zip(xrange(3),">ox","rgb") :
    plt.scatter(features[target == t,0],
                features[target == t,3],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[3])

    plt.savefig('iris_plot3.png')
    #plt.clf()

plt.figure(4)

for t,marker,c in zip(xrange(3),">ox","rgb") :
    plt.scatter(features[target == t,1],
                features[target == t,2],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[1])
    plt.ylabel(feature_names[2])

    plt.savefig('iris_plot4.png')
    #plt.clf()

plt.figure(5)

for t,marker,c in zip(xrange(3),">ox","rgb") :
    plt.scatter(features[target == t,1],
                features[target == t,3],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[1])
    plt.ylabel(feature_names[3])

    plt.savefig('iris_plot5.png')

plt.figure(6)

for t,marker,c in zip(xrange(3),">ox","rgb") :
    plt.scatter(features[target == t,2],
                features[target == t,3],
                marker=marker,
                c=c)
    plt.xlabel(feature_names[2])
    plt.ylabel(feature_names[3])

    plt.savefig('iris_plot6.png')