import numpy as np
from scipy import stats

class WeatherStats:
    def __init__(self):
        pass
    
    def calculate_correlation(self, weather_data):
        """Calculate correlation between weather parameters"""
        def get_correlation_matrix():
            temp = weather_data.get_field_values('temperature')
            humidity = weather_data.get_field_values('humidity')
            precip = weather_data.get_field_values('precipitation')
            
            data = np.array([temp, humidity, precip])
            return np.corrcoef(data)
        
        return get_correlation_matrix()
    
    def calculate_distribution_stats(self, weather_data):
        """Calculate distribution statistics for weather parameters"""
        def calculate_parameter_stats(values):
            return {
                'skewness': stats.skew(values),
                'kurtosis': stats.kurtosis(values)
            }
        
        return {
            'temperature': calculate_parameter_stats(weather_data.get_field_values('temperature')),
            'humidity': calculate_parameter_stats(weather_data.get_field_values('humidity')),
            'precipitation': calculate_parameter_stats(weather_data.get_field_values('precipitation'))
        }
    
    def calculate_summary_stats(self, weather_data):
        """Calculate summary statistics for weather parameters"""
        def get_parameter_summary(values):
            return {
                'mean': np.mean(values),
                'std': np.std(values),
                'min': np.min(values),
                'max': np.max(values)
            }
        
        return {
            'temperature': get_parameter_summary(weather_data.get_field_values('temperature')),
            'humidity': get_parameter_summary(weather_data.get_field_values('humidity')),
            'precipitation': get_parameter_summary(weather_data.get_field_values('precipitation'))
        }