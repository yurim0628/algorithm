class Solution {
    public String solution(String videoLength, String currentPosition, String operationStart, String operationEnd, String[] commands) {
        int currentSeconds = parseTimeToSeconds(currentPosition);
        int operationStartSeconds = parseTimeToSeconds(operationStart);
        int operationEndSeconds = parseTimeToSeconds(operationEnd);
        int videoLengthSeconds = parseTimeToSeconds(videoLength);

        currentSeconds = skipIfInOperation(currentSeconds, operationStartSeconds, operationEndSeconds);

        for (String command : commands) {
            if (command.equals("next")) {
                currentSeconds = moveNext(currentSeconds, videoLengthSeconds, operationStartSeconds, operationEndSeconds);
            } else if (command.equals("prev")) {
                currentSeconds = movePrev(currentSeconds, operationStartSeconds, operationEndSeconds);
            }
        }

        return formatTime(currentSeconds);
    }

    private int parseTimeToSeconds(String time) {
        String[] timeParts = time.split(":");
        return Integer.parseInt(timeParts[0]) * 60 + Integer.parseInt(timeParts[1]);
    }

    private int skipIfInOperation(int currentSeconds, int operationStartSeconds, int operationEndSeconds) {
        if (operationStartSeconds <= currentSeconds && currentSeconds <= operationEndSeconds) {
            return operationEndSeconds;
        }
        return currentSeconds;
    }

    private int moveNext(int currentSeconds, int videoLengthSeconds, int operationStartSeconds, int operationEndSeconds) {
        currentSeconds += 10;
        if (currentSeconds > videoLengthSeconds) {
            currentSeconds = videoLengthSeconds;
        }
        return skipIfInOperation(currentSeconds, operationStartSeconds, operationEndSeconds);
    }

    private int movePrev(int currentSeconds, int operationStartSeconds, int operationEndSeconds) {
        currentSeconds -= 10;
        if (currentSeconds < 0) {
            currentSeconds = 0;
        }
        return skipIfInOperation(currentSeconds, operationStartSeconds, operationEndSeconds);
    }

    private String formatTime(int totalSeconds) {
        return String.format("%02d:%02d", totalSeconds / 60, totalSeconds % 60);
    }
}
