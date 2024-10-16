import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from weather_data import WeatherData
from statistical_analysis import WeatherStats
from data_visualization import WeatherVisualizer

class WeatherForecastingSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Forecasting System")
        self.root.geometry("800x600")
        
        self.weather_data = WeatherData()
        self.stats = WeatherStats()
        self.visualizer = WeatherVisualizer()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main frames
        input_frame = ttk.LabelFrame(self.root, text="Data Input", padding="10")
        input_frame.pack(fill="x", padx=10, pady=5)
        
        analysis_frame = ttk.LabelFrame(self.root, text="Analysis Options", padding="10")
        analysis_frame.pack(fill="x", padx=10, pady=5)
        
        visualization_frame = ttk.LabelFrame(self.root, text="Visualization", padding="10")
        visualization_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input fields
        ttk.Label(input_frame, text="Location:").grid(row=0, column=0, padx=5, pady=5)
        self.location_entry = ttk.Entry(input_frame)
        self.location_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Temperature (°C):").grid(row=1, column=0, padx=5, pady=5)
        self.temp_entry = ttk.Entry(input_frame)
        self.temp_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Humidity (%):").grid(row=2, column=0, padx=5, pady=5)
        self.humidity_entry = ttk.Entry(input_frame)
        self.humidity_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Precipitation (mm):").grid(row=3, column=0, padx=5, pady=5)
        self.precip_entry = ttk.Entry(input_frame)
        self.precip_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Buttons
        ttk.Button(input_frame, text="Add Data", command=self.add_data).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Analysis options
        analysis_options = ["Correlation Analysis", "Distribution Analysis", "Box Plot", "Histogram"]
        self.analysis_var = tk.StringVar()
        analysis_dropdown = ttk.Combobox(analysis_frame, textvariable=self.analysis_var, values=analysis_options)
        analysis_dropdown.set("Select Analysis")
        analysis_dropdown.pack(side="left", padx=5)
        
        ttk.Button(analysis_frame, text="Perform Analysis", command=self.perform_analysis).pack(side="left", padx=5)
        
        # Visualization area
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=visualization_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def add_data(self):
        try:
            location = self.location_entry.get()
            temperature = float(self.temp_entry.get())
            humidity = float(self.humidity_entry.get())
            precipitation = float(self.precip_entry.get())
            
            self.weather_data.add_data(location, temperature, humidity, precipitation)
            messagebox.showinfo("Success", "Weather data added successfully!")
            
            # Clear entries
            for entry in [self.location_entry, self.temp_entry, self.humidity_entry, self.precip_entry]:
                entry.delete(0, tk.END)
                
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values!")
    
    def perform_analysis(self):
        analysis_type = self.analysis_var.get()
        
        if not self.weather_data.has_data():
            messagebox.showwarning("Warning", "No data available for analysis!")
            return
            
        self.ax.clear()
        
        if analysis_type == "Correlation Analysis":
            corr = self.stats.calculate_correlation(self.weather_data)
            self.visualizer.plot_correlation_matrix(corr, self.ax)
        elif analysis_type == "Distribution Analysis":
            stats = self.stats.calculate_distribution_stats(self.weather_data)
            self.visualizer.plot_distribution_stats(stats, self.ax)
        elif analysis_type == "Box Plot":
            self.visualizer.create_box_plot(self.weather_data, self.ax)
        elif analysis_type == "Histogram":
            self.visualizer.create_histogram(self.weather_data, self.ax)
            
        self.canvas.draw()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherForecastingSystem()
    app.run()