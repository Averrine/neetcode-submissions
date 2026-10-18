class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted([(p,s) for p,s in zip(position, speed)], key=lambda t: -t[0])
        individual_time = [(target - p)/s for p,s in sorted_pos]

        num_fleet = 0
        last_fleet_speed = 0

        for time in individual_time:
            if time > last_fleet_speed:
                num_fleet +=1 
                last_fleet_speed = time
        return num_fleet