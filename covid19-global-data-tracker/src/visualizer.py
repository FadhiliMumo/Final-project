class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        import matplotlib.pyplot as plt
        
        # Example: Plotting confirmed cases over time for a specific country
        country_data = self.data[self.data['country'] == 'CountryName']  # Replace 'CountryName' with actual country
        plt.figure(figsize=(10, 5))
        plt.plot(country_data['date'], country_data['confirmed'], label='Confirmed Cases', color='blue')
        plt.xlabel('Date')
        plt.ylabel('Number of Cases')
        plt.title('COVID-19 Confirmed Cases Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def show_summary(self):
        summary = {
            'total_confirmed': self.data['confirmed'].sum(),
            'total_deaths': self.data['deaths'].sum(),
            'total_recoveries': self.data['recoveries'].sum(),
            'latest_date': self.data['date'].max()
        }
        print("COVID-19 Data Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")