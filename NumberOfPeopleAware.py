class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10 ** 9 + 7
        def mod(x):
            return (x+MOD) % MOD
        start = [0] * (n+1)
        stop = [0] * (n+1)
        start[delay+1] = 1
        stop[forget+1] = 1
        peopleSharing = 0
        totalPeopleAware = 1
        for i in range(n+1): #still want to check the last day

            #Forgetting (Stopped Sharing)
            peopleSharing -= stop[i]
            peopleSharing = mod(peopleSharing)
            totalPeopleAware -= stop[i]
            totalPeopleAware = mod(totalPeopleAware)

            #People sharing (started talking)
            peopleSharing += start[i]
            peopleSharing = mod(peopleSharing)
            totalPeopleAware += peopleSharing
            totalPeopleAware = mod(totalPeopleAware)



            if i + delay < n + 1:
                start[i+delay] += peopleSharing

            if i + forget < n + 1:
                stop[i+forget] += peopleSharing

        
        return totalPeopleAware




        

        