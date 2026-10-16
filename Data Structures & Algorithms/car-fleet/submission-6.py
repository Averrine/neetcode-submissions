class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # lumps car sorted(position + speed) in a list, descending other
        sorted_positions = sorted([(p, s) for p,s in zip(position, speed)], key=lambda t: -t[0])
        # calculate individual times
        individual_times = [(target - p) / s for p,s in sorted_positions]

        # keep track of number of fleets
        num_fleet = 0 
        # keep track of last fleet time 
        LFT = 0 

        for time in individual_times:
            if time > LFT:
                num_fleet += 1
                LFT = time
        return num_fleet