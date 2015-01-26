from construct import construct_array

def collect(X):
    small = []
    medium = []
    large = []
    for x in X:
        if x < 10:
            small.append(x)
        elif x >= 10 and x < 100:
            medium.append(x)
        else:
            large.append(x)

    return (small,medium,large)

def mean(X):
    return sum(X)/float(len(X))

def st_dev(X):
    a = mean(X)
    Y = [(x-a)**2 for x in X]
    return (sum(Y)/float(len(Y)))**0.5

if __name__ == "__main__":
    X = construct_array(200,10)
    """print collect(X)"""
    print mean(X),st_dev(X)
