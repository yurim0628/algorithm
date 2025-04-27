class Solution {
    public int[] solution(int n, int m) {
        int gcd = getGCD(n, m);
        int lcm = (n * m) / gcd;
        
        return new int[]{gcd, lcm};       
    }
    
    private int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2, num1%num2);
    }
}