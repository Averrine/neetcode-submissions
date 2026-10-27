class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find individual positions
        # find times from those positions
        # group speed/position relevant to each other

        # find fleet number and return 
        # edit new fleet times

        sorted_positions = sorted([(p,s) for p,s in zip(position, speed)], key=lambda t: -t[0])
        individual_times = [(target - p)/s for p,s in sorted_positions]


        


        num_fleet = 0
        time_last_fleet = 0

        for time in individual_times:
            if time > time_last_fleet:
                time_last_fleet = time
                num_fleet += 1

        return num_fleet