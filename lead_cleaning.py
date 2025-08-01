import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset cargado correctamente.")
    return df

def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["email"], inplace=True)
    df["email"] = df["email"].str.strip().str.lower()
    return df

if __name__ == "__main__":
    df = load_data("customers_1000.csv")
    clean_df = clean_data(df)
    clean_df.to_csv("customers_clean.csv", index=False)
    print("Datos limpios exportados.")
