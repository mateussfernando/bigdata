import pandas as pd

class Transform:
    def clean_data(self, universities):
        """Converte lista JSON em DataFrame e trata campos."""
        df = pd.DataFrame(universities)
        df = df.drop_duplicates(subset=["name", "country"])
        df["web_pages"] = df["web_pages"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
        df["domains"] = df["domains"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
        df["state-province"] = df["state-province"].fillna("N/A")
        return df
