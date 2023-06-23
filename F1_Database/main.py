from F1_Database import FileHandler
from F1_Database import connection
from F1_Database.FilesHandlers import circuits, constructor_results, constructor_standings, constructors, \
    driver_standings, drivers, lap_times, pit_stops, qualifying, races, seasons, results, sprint_results, status

#FileHandler.connection('localhost','root', 'bernardo', 'formula1')
circuits.insertDataFrom_csv('circuits.csv')
constructor_standings.insertDataFrom_csv('constructor_standings.csv')
constructors.insertDataFrom_csv('constructors.csv')
driver_standings.insertDataFrom_csv('driver_standings.csv')
drivers.insertDataFrom_csv('drivers.csv')
lap_times.insertDataFrom_csv('lap_times.csv')
pit_stops.insertDataFrom_csv('pit_stops.csv')
qualifying.insertDataFrom_csv('qualifying.csv')
races.insertDataFrom_csv('races.csv')
results.insertDataFrom_csv('results.csv')
seasons.insertDataFrom_csv('seasons.csv')
sprint_results.insertDataFrom_csv('sprint_results.csv')
status.insertDataFrom_csv('status.csv')

