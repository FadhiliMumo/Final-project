class DataProcessor:
    def clean_data(self, df):
        # Handle missing values
        df.fillna(method='ffill', inplace=True)
        df.dropna(inplace=True)

        # Remove outliers (example: removing rows where confirmed cases are negative)
        df = df[df['confirmed_cases'] >= 0]

        return df

    def analyze_data(self, df):
        # Perform statistical analysis
        summary = {
            'total_confirmed': df['confirmed_cases'].sum(),
            'total_deaths': df['deaths'].sum(),
            'total_recoveries': df['recoveries'].sum(),
            'average_daily_cases': df['confirmed_cases'].mean(),
            'average_daily_deaths': df['deaths'].mean(),
        }
        return summary