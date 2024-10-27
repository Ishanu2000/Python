import csv

#Represent weather data for a week
class WeatherData:
    def __init__(self, temperatures):
        if len(temperatures) != 7:
            raise ValueError("Temperature data must contain exactly 7 values.")
        self.temperatures = tuple(temperatures)  #Store data in a tuple for immutability

    #Calculate the average temperature
    def average_temperature(self):
        return sum(self.temperatures) / len(self.temperatures)

    #Find the highest temperature
    def highest_temperature(self):
        return max(self.temperatures)

    #Find the lowest temperature
    def lowest_temperature(self):
        return min(self.temperatures)

    #Save temperature data to a CSV file
    def save_to_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Day", "Temperature"])
                for i, temp in enumerate(self.temperatures, start=1):
                    writer.writerow([f"Day {i}", temp])
            print(f"\nWeather data saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    #Load temperature data from a CSV file
    @classmethod
    def load_from_csv(cls, filename):
        temperatures = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  #Skip the header
                for row in reader:
                    temperatures.append(float(row[1]))  #Read temperature values
            if len(temperatures) != 7:
                raise ValueError("CSV file must contain exactly 7 temperature values.")
            return cls(temperatures)
        except FileNotFoundError:
            print(f"{filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading from CSV: {e}")
            return None

#Example
#Create WeatherData instance with temperature data for a week
weather_data = WeatherData([21.5, 25.0, 21.4, 27.6, 23.1, 23.3, 26.4])

#Calculate and display the average, highest, and lowest temperatures
print(f"Average Temperature: {weather_data.average_temperature():.2f}")
print(f"Highest Temperature: {weather_data.highest_temperature()}")
print(f"Lowest Temperature: {weather_data.lowest_temperature()}")

#Save the temperature data to a CSV file
weather_data.save_to_csv("weather_data.csv")

#Load temperature data from a CSV file
loaded_weather_data = WeatherData.load_from_csv("weather_data.csv")
if loaded_weather_data:
    print(f"\n----- Loaded Data -----")
    print(f"Average Temperature: {loaded_weather_data.average_temperature():.2f}")
    print(f"Highest Temperature: {loaded_weather_data.highest_temperature()}")
    print(f"Lowest Temperature: {loaded_weather_data.lowest_temperature()}")
