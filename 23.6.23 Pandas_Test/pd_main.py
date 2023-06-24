import pandas as pd


def func(x):
    if x["price"] > 16000:
        return "expensive"
    return "cheap"


# Read data
fpath = "./car_price.csv"
df = pd.read_csv(fpath)
# Giving Columns' names :
# df = pd.read_csv(fpath, names=[name1,name2,……])

# Show dataframe
print(df)
print(df.dtypes)

# Show whether has empty value
print(df.notnull().value_counts())


# Show specific column
print(df["CarName"].value_counts())

# Show specific row
print(df.loc[0])

# Show specific colums & rows
print(df.loc[1:5, ["CarName", "price"]])

# Show price > 16000, and sort by price
print(df.loc[df["price"] > 16000, :].sort_values(by="price", ascending=False))

# Add new column
df.loc[:, "Comment"] = df.apply(func, axis=1)
print(df.head())
print(df["Comment"].value_counts())

# See statistics' info
print(df.describe())
print(df.cov())
print(df.corr())

# Save to excel
toPath = "./out.csv"
df.to_csv(toPath, index=False)
corrPath = "./out_corr.csv"
df.corr().to_csv(corrPath)
