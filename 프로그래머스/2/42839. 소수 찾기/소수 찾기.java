import java.util.*;

class Solution {
    String numbers;
    boolean[] visited;
    Set<Integer> primeNumber = new HashSet<>();
    
    public int solution(String numbers) {
        this.numbers = numbers;
        visited = new boolean[numbers.length()];
        findPrimeNumber(0);
        return primeNumber.size();
    }
    
    private void findPrimeNumber(int currentNumber) {
        if(isPrimeNumber(currentNumber)){
            primeNumber.add(currentNumber);
        }
        
        for(int i = 0; i < numbers.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                findPrimeNumber(Integer.parseInt(String.valueOf(currentNumber) + numbers.charAt(i)));
                visited[i] = false;
            }
        }
    }
    
    private boolean isPrimeNumber(int number) {
        if(number < 2) {
            return false;
        }
        
        for(int i = 2; i <= Math.sqrt(number); i++) {
            if(number % i == 0) {
                return false;
            }
        }
        
        return true;
    }
}