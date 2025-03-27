import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int totalServers = 0; 
        int activeServers = 0;
        int[] serverRelease = new int[24]; 
        
        for (int i = 0; i < 24; i++) {
            activeServers -= serverRelease[i];
            
            int requiredServers = players[i] / m; 
            
            if (requiredServers > activeServers) {
                int newServers = requiredServers - activeServers;
                
                totalServers += newServers;
                activeServers += newServers;

                if (i + k < 24) {
                    serverRelease[i + k] = newServers;
                }
            }
        }

        return totalServers;
    }
}
