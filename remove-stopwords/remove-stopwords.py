def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    
    # Your code here
    arr=[]
    ss=set(stopwords)
    for token in tokens:
        if token not in stopwords:
            arr.append(token)
    return arr
    pass