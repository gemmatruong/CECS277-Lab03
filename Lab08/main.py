""" LAB #08
    10/15/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that Create a game where the user must choose a vehicle, either a Car, Motorcycle, or Truck and then
race against the remaining choices.
"""

from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from truck import Truck
import check_input
import random

def create_track(num_vehicles, track_length):
    track = []
    """
        One lane per vehicle and 2 obstacles per lane,
        place obstacles on track, 2 in each lane at random column
        (but not at start or end points)
    """
    if track_length <= 2:
        raise ValueError("The length of track must be greater than 2!")

    for i in range(num_vehicles):
        lane = ['-'] * track_length
        
        obs_locs = sorted(random.sample(range(1, track_length - 2), 2))
        
        for pos in obs_locs:
            lane[pos] = 'O'

        track.append(lane)

    return track

def display_track(track, track_length, vehicles):
    """ 
        Place the vehicle's initials at its current position. Player is a 'P',
        display the updated track
    """
    for i, vehicle in enumerate(vehicles):
        lane = track[i]
        pos = vehicle.position

        if pos >= track_length:
            pos = track_length - 1

        for j, column in enumerate(lane):
            if column == vehicle.initial:
                lane[j] = '*'
        if lane[pos] == 'O':
            lane[pos+1] = vehicle.initial
        else:
            lane[pos] = vehicle.initial

        print(''.join(lane))

def find_obs_position(lane, current_pos):
    """
    Find the next obstacle location after current_pos in lane_list.
    Returns index of obstacle or None if none found.
    """
    try:
        return lane.index('O', current_pos + 1)
    except ValueError:
        return 100  # out of range, there is no more obstacle in the lane

def main():
    vehicle_names = ["Lightning Car", "Swift Bike", "Bohemoth Truck"]
    vehicle_letters = ["C", "M", "T"]
    vehicle_speed = [7, 8, 6]

    # Player selection
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    player = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)
    player_veh = player - 1

    # Create track
    track = create_track(3, 100)

    # Change initial of the vehicle has been chosen by player to 'P':
    vehicle_letters[player_veh] = "P"
    
    # Initialize 3 objects for 3 vehicles
    vehicles = [Car(vehicle_names[0], vehicle_letters[0], vehicle_speed[0]), 
                Motorcycle(vehicle_names[1], vehicle_letters[1], vehicle_speed[1]),
                Truck(vehicle_names[2], vehicle_letters[2], vehicle_speed[2])]
    winners = []

    # Run the game
    while len(winners) < len(vehicles):
        # display the vehicles and track
        print()
        for veh in vehicles:
            print(veh)
        display_track(track, 100, vehicles)

        # move vehicles
        # do not ask if player already arrived the finished line
        if vehicles[player_veh] not in winners:
            move = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
            player_pos = vehicles[player_veh].position

            # Call function to find the nearest obstacle ahead of vehicle
            player_obs_pos = find_obs_position(track[player_veh], player_pos)

            if move == 1:
                print(vehicles[player_veh].fast(player_obs_pos))
            elif move == 2:
                print(vehicles[player_veh].slow(player_obs_pos))
            else:
                print(vehicles[player_veh].special_move(player_obs_pos))

        # move opponents
        for i in range(len(vehicles)):
            if i != (player - 1) and vehicles[i] not in winners:
                obs_pos = find_obs_position(track[i], vehicles[i].position)

                r = random.random() # 0.0 < r < 1.0
                if r <= 0.3:
                    # fast
                    print(vehicles[i].fast(obs_pos))
                elif 0.3 < r < 0.6:
                    # special move
                    print(vehicles[i].special_move(obs_pos))
                else: # 0.6 > 1.0
                    # slow
                    print(vehicles[i].slow(obs_pos))
        
        # check for winners
        for veh in vehicles:
            if veh.position >= 99 and veh not in winners:
                winners.append(veh)

    display_track(track, 100, vehicles)

    # print the winners
    placements = ["1st", "2nd", "3rd"]
    for i, veh in enumerate(winners):
        print(f"{placements[i]} place: {veh}")


if __name__ == "__main__":
    main()