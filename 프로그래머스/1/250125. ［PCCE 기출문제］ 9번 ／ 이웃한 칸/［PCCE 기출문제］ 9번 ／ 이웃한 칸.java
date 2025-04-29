public class Solution {
    public int solution(String[][] boardGrid, int h, int w) {
        Board board = new Board(boardGrid);
        Position position = new Position(h, w);
        return board.countAdjacentSameColorTiles(position);
    }
}

enum Direction {
    UP(-1, 0),
    DOWN(1, 0),
    LEFT(0, -1),
    RIGHT(0, 1);

    final int deltaX;
    final int deltaY;

    Direction(int deltaX, int deltaY) {
        this.deltaX = deltaX;
        this.deltaY = deltaY;
    }

    public Position move(Position position) {
        return new Position(position.x + deltaX, position.y + deltaY);
    }
}

class Position {
    int x; 
    int y; 

    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public boolean isWithinBounds(int maxRows, int maxCols) {
        return x >= 0 && x < maxRows && y >= 0 && y < maxCols;
    }
}

class Board {
    private final String[][] grid;

    public Board(String[][] grid) {
        this.grid = grid;
    }

    public String getColor(Position position) {
        return grid[position.x][position.y];
    }

    public boolean hasSameColor(Position pos1, Position pos2) {
        return getColor(pos1).equals(getColor(pos2));
    }

    public int countAdjacentSameColorTiles(Position center) {
        int sameColorCount = 0;
        int totalRows = grid.length;
        int totalCols = grid[0].length;

        for (Direction direction : Direction.values()) {
            Position neighbor = direction.move(center);
            if (neighbor.isWithinBounds(totalRows, totalCols) && hasSameColor(center, neighbor)) {
                sameColorCount++;
            }
        }

        return sameColorCount;
    }
}