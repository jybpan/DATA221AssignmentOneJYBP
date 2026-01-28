def dataframeExtrapolation():
    import pandas as pd

    data = {
        "A": [1, 2, 2, 1],
        "B": [3.1, 4.2, 1.5, 6.3],
        "C": [800, 150, 400, 210]
    }

    df = pd.DataFrame(data=data)
    df['mean'] = df.mean(axis=1)

dataframeExtrapolation()