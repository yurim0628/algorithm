import java.util.*;

public class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, GiftHistory> fromFriendMap = new HashMap<>();
        for (String sender : friends) {
            GiftHistory history = new GiftHistory(sender);
            for (String recipient : friends) {
                if (!sender.equals(recipient)) {
                    history.addGiftRecord(recipient, 0);
                }
            }
            fromFriendMap.put(sender, history);
        }

        Map<String, GiftStats> giftCountByFriend = new HashMap<>();
        for (String friend : friends) {
            giftCountByFriend.put(friend, new GiftStats());
        }

        for (String gift : gifts) {
            String[] pair = gift.split(" ");
            String sender = pair[0];
            String receiver = pair[1];

            GiftHistory senderHistory = fromFriendMap.get(sender);
            senderHistory.addGiftRecord(receiver, 1);

            giftCountByFriend.get(sender).addSent(1);
            giftCountByFriend.get(receiver).addReceived(1);
        }

        Map<String, Integer> nextMonthGifts = new HashMap<>();
        for (String person : friends) {
            nextMonthGifts.put(person, 0);
        }

        for (int i = 0; i < friends.length; i++) {
            for (int j = i + 1; j < friends.length; j++) {
                String a = friends[i];
                String b = friends[j];

                int aToB = 0, bToA = 0;
                for (GiftRecord record : fromFriendMap.get(a).getGiftRecords()) {
                    if (record.getRecipient().equals(b)) {
                        aToB = record.getCount();
                        break;
                    }
                }
                for (GiftRecord record : fromFriendMap.get(b).getGiftRecords()) {
                    if (record.getRecipient().equals(a)) {
                        bToA = record.getCount();
                        break;
                    }
                }

                if (aToB > bToA) {
                    nextMonthGifts.put(a, nextMonthGifts.get(a) + 1);
                } else if (bToA > aToB) {
                    nextMonthGifts.put(b, nextMonthGifts.get(b) + 1);
                } else {
                    int aIndex = giftCountByFriend.get(a).getGiftsSent() - giftCountByFriend.get(a).getGiftsReceived();
                    int bIndex = giftCountByFriend.get(b).getGiftsSent() - giftCountByFriend.get(b).getGiftsReceived();

                    if (aIndex > bIndex) {
                        nextMonthGifts.put(a, nextMonthGifts.get(a) + 1);
                    } else if (bIndex > aIndex) {
                        nextMonthGifts.put(b, nextMonthGifts.get(b) + 1);
                    }
                }
            }
        }

        int answer = 0;
        for (String friend : friends) {
            answer = Math.max(answer, nextMonthGifts.get(friend));
        }
        return answer;
    }

    static class GiftRecord {
        private String recipient;
        private int count;

        public GiftRecord(String recipient, int count) {
            this.recipient = recipient;
            this.count = count;
        }

        public String getRecipient() { return recipient; }
        public int getCount() { return count; }
        public void addCount(int n) { this.count += n; }
    }

    static class GiftHistory {
        private String sender;
        private List<GiftRecord> giftRecords;

        public GiftHistory(String sender) {
            this.sender = sender;
            this.giftRecords = new ArrayList<>();
        }

        public void addGiftRecord(String recipient, int count) {
            for (GiftRecord record : giftRecords) {
                if (record.getRecipient().equals(recipient)) {
                    record.addCount(count);
                    return;
                }
            }
            giftRecords.add(new GiftRecord(recipient, count));
        }

        public List<GiftRecord> getGiftRecords() {
            return giftRecords;
        }

        public String getSender() {
            return sender;
        }
    }

    static class GiftStats {
        private int giftsSent;
        private int giftsReceived;

        public GiftStats() {
            this.giftsSent = 0;
            this.giftsReceived = 0;
        }

        public void addSent(int n) { this.giftsSent += n; }
        public void addReceived(int n) { this.giftsReceived += n; }

        public int getGiftsSent() { return giftsSent; }
        public int getGiftsReceived() { return giftsReceived; }
    }
}
