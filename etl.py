# # Requirements

# - Get Launch Data from SpaceX([https://api.spacexdata.com/v3/launches](https://api.spacexdata.com/v3/launches))
# - We only need the following data:
#     - mission name
#     - mission patch image
#     - launch year
#     - launch success
#         - Launch failure details if launch was unsucessful
#     - Payload Type
# - Load Data into CSV

import requests
import csv


# Extract Here
def get_launch_data(url):
    launch_data = requests.get(url)
    return launch_data.json()
    
# Transform Here
def transform_data(launch_data):
    mission_names = []
    mission_image = []
    mission_id = []
    
    for launch in launch_data:
        mission_names.append(launch["mission_name"])
        mission_image.append(launch["links"]["mission_patch"])
        mission_id.append(launch["mission_id"])
    
    # Loads data to CSV
    with open('flight_data.csv', 'w', newline='') as f:
        for a, b, c in zip(mission_id, mission_names, mission_image):
           
            writer = csv.writer(f)
            writer.writerow([a, b, c])

    print(len(mission_names))
    print(len(mission_image))
    print(len(mission_id))    

# This is where we run the code
result = get_launch_data('https://api.spacexdata.com/v3/launches')

transform_data(result)

