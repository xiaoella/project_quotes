def postcode_anonymisation(df, column):
    df[column] = df[column].str[:-3] + "***"
    return df

def director_anonymisation(df, column):
    directors = sorted(df[column].unique())
    director_encoded = {directors[0]: "A", directors[1]: "B"}
    df[column] = df[column].replace(director_encoded)
    return df