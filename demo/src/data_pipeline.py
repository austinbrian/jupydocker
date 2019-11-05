import pandas as pd


def make_data():
    data = {
        "A": list(range(10)),
        "B": pd.np.arange(2, 22, 2),
        "C": ["cat", "bat", "fat", "cat", "spat", "scat", "bat", "vat", "gnat", "wat"],
    }
    df = pd.DataFrame(data)
    df.to_csv("data/raw_data.csv", index=False)
    return df


def transform_data(df):
    if "C" in df:
        return pd.get_dummies(df["C"])
    else:
        return df


if __name__ == "__main__":
    df = make_data()
    new_df = transform_data(df)
    new_df.to_pickle("data/transformed_df.pkl")
