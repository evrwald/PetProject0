import pandas as pd


class DataProvider:
    @staticmethod
    def get_credentials(user):
        df = pd.read_excel('./assets/data/credentials.xlsx')
        user = df.loc[df['user'] == user]
        return {
            'username': user.username.to_string(index=False),
            'password': user.password.to_string(index=False),
            'profile': user.profile.to_string(index=False)
        }
