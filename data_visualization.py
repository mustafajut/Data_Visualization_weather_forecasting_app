import numpy as np
import seaborn as sns

class WeatherVisualizer:
    def __init__(self):
        pass
    
    def plot_correlation_matrix(self, correlation_matrix, ax):
        """Plot correlation matrix as a heatmap"""
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   xticklabels=['Temp', 'Humidity', 'Precip'],
                   yticklabels=['Temp', 'Humidity', 'Precip'],
                   ax=ax)
        ax.set_title('Weather Parameter Correlations')
    
    def plot_distribution_stats(self, stats, ax):
        """Plot distribution statistics"""
        parameters = list(stats.keys())
        skewness = [stats[param]['skewness'] for param in parameters]
        kurtosis = [stats[param]['kurtosis'] for param in parameters]
        
        x = np.arange(len(parameters))
        width = 0.35
        
        ax.bar(x - width/2, skewness, width, label='Skewness')
        ax.bar(x + width/2, kurtosis, width, label='Kurtosis')
        
        ax.set_xticks(x)
        ax.set_xticklabels(parameters)
        ax.legend()
        ax.set_title('Distribution Statistics')
    
    def create_box_plot(self, weather_data, ax):
        """Create box plots for weather parameters"""
        data = {
            'Temperature': weather_data.get_field_values('temperature'),
            'Humidity': weather_data.get_field_values('humidity'),
            'Precipitation': weather_data.get_field_values('precipitation')
        }
        
        ax.boxplot(data.values())
        ax.set_xticklabels(data.keys())
        ax.set_title('Weather Parameters Distribution')
    
    def create_histogram(self, weather_data, ax):
        """Create histograms for weather parameters"""
        temp = weather_data.get_field_values('temperature')
        humidity = weather_data.get_field_values('humidity')
        precip = weather_data.get_field_values('precipitation')
        
        ax.hist([temp, humidity, precip], label=['Temperature', 'Humidity', 'Precipitation'],
                alpha=0.5, bins=15)
        ax.legend()
        ax.set_title('Weather Parameters Distribution')