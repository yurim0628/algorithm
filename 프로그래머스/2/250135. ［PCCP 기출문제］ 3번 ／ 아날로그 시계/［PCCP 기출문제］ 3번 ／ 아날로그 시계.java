class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int answer = 0;

        int startTime = h1 * 3600 + m1 * 60 + s1;
        int endTime = h2 * 3600 + m2 * 60 + s2;

        if (startTime == 0 || startTime == 43200) {
            answer++;
        }

        while (startTime < endTime) {
            double hCurAngle = startTime / 120.0 % 360;
            double mCurAngle = startTime / 10.0 % 360;
            double sCurAngle = startTime * 6.0 % 360;

            double hNextAngle = ((startTime + 1) / 120.0 % 360 == 0) ? 360 : (startTime + 1) / 120.0 % 360;
            double mNextAngle = ((startTime + 1) / 10.0 % 360 == 0) ? 360 : (startTime + 1) / 10.0 % 360;
            double sNextAngle = ((startTime + 1) * 6.0 % 360 == 0) ? 360 : (startTime + 1) * 6.0 % 360;

            if (sCurAngle < hCurAngle && sNextAngle >= hNextAngle) {
                answer++;
            }
            if (sCurAngle < mCurAngle && sNextAngle >= mNextAngle) {
                answer++;
            }
            if (sNextAngle == hNextAngle && hNextAngle == mNextAngle) {
                answer--;
            }

            startTime++;
        }

        return answer;
    }
}
