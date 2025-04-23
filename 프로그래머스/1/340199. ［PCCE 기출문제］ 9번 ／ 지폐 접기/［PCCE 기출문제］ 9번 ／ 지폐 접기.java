class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        if(wallet[0] >= bill[0] && wallet[1] >= bill[1]) return 0;
        while(true) {
            if(bill[0] > bill[1])
            {
                bill[0] /= 2;
            } else {
                bill[1] /= 2;
            }
            answer++;
            if((wallet[0] >= bill[0] && wallet[1] >= bill[1]) || (wallet[0] >= bill[1] && wallet[1] >= bill[0])) break;
        }
        return answer;
    }
}