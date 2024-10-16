class WeatherData:
    def __init__(self):
        self.data = []
    
    def __str__(self):
        return f"WeatherData: {len(self.data)} records"
    
    def __repr__(self):
        return f"WeatherData(records={len(self.data)})"
    
    def add_data(self, location, temperature, humidity, precipitation):
        """Add weather data for a location"""
        self.data.append({
            'location': location,
            'temperature': temperature,
            'humidity': humidity,
            'precipitation': precipitation
        })
    
    def get_data(self, *args, **kwargs):
        """
        Get weather data with flexible filtering options
        args: list of fields to return
        kwargs: filtering conditions
        """
        result = self.data
        
        # Apply filters from kwargs
        for key, value in kwargs.items():
            result = [r for r in result if r.get(key) == value]
        
        # Select specific fields if provided
        if args:
            result = [{k: r[k] for k in args if k in r} for r in result]
            
        return result
    
    def has_data(self):
        """Check if there is any data available"""
        return len(self.data) > 0
    
    def get_field_values(self, field):
        """Get all values for a specific field"""
        return [record[field] for record in self.data]