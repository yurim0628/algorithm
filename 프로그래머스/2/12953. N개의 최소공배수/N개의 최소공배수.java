class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int arrLength = arr.length;
        
        if(arrLength == 1) {
            return arr[0];
        }
        
        int g = gcd(arr[0], arr[1]);
        answer = (arr[0] * arr[1]) / g;
      
        if(arrLength > 2) {
            for(int i = 2; i < arrLength; i++) {
                g = gcd(answer, arr[i]);
                answer = (answer * arr[i]) / g;
            }
        }
        
        return answer;
    }
    
    private int gcd(int a, int b) {
        int r = a % b;
        if (r == 0) {
            return b;
        } else {
            return gcd(b, r);
        }
    }
}