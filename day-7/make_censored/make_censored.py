def make_censored(text,stop_words):
    words = text.split()
    result_words = ['$#%!' if word in stop_words else word for word in words]
    return ' '.join(result_words)

