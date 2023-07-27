class Mileage :
    def route_mileage(time, del1, del2, del3):
        # calculate miles unless query time is less than delivery start time
        # Space-Time Complexity: O(1)
        def get_miles(delivery, time):
            miles = 0
            hours = time.hour + time.minute / 60 + time.second / 3600
            if hours > delivery[3]:
                miles = min((hours - delivery[3]) * 18, delivery[1])
                miles = float("{:.2f}".format(min((hours - delivery[3]) * 18, delivery[1])))
                return miles
            return miles
    
        del1_miles = get_miles(del1, time)
        del2_miles = get_miles(del2, time)
        del3_miles = get_miles(del3, time)
        total_miles = float("{:.2f}".format(del1_miles + del2_miles + del3_miles))
        return del1_miles, del2_miles, del3_miles, total_miles
        
    