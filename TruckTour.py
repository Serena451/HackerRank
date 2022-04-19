# QUESTION DESCRIPTION

# Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to N-1 (both inclusive).
# You have two pieces of information corresponding to each of the petrol pump:

# (1) the amount of petrol that particular petrol pump will give, and
# (2) the distance from that petrol pump to the next petrol pump.

# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps.
# The truck will move one kilometer for each litre of the petrol.

# LET'S SOLVE IT
# The function accepts 2D-ingeter-array petrolpumps as parameter.

def truckTour(petrolpumps):

    n = len(petrolpumps)

    # Let us define a new array containing the differences between the amount of petrol that each petrol pump will give us
    # and the petrol that we need to reach the next petrol station (equal to the distance from our position to the next petrol pump).

    differences = [a-b for [a,b] in petrolpumps]

    for i in range(n):
        summa = 0
        flag = True
        for j in range(n):
            summa = summa + differences[(i+j)%n]

            if (summa < 0):
                # Ihe petrol is out. From this index the truck will not be able to complete the circle.

                flag = False
                break

        if flag:
            return i

    return 'impossible
