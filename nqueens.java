"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

"""

import java.util.*;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        solve(0, n, 0, 0, 0, new int[n], res);
        return res;
    }

    private void solve(int row, int n, int cols, int diag, int antiDiag,
                       int[] queens, List<List<String>> res) {
        
        if (row == n) {
            res.add(buildBoard(queens, n));
            return;
        }
        int available = ((1 << n) - 1) & ~(cols | diag | antiDiag);

        while (available != 0) {
            int pos = available & -available;
            available -= pos;

            int col = Integer.numberOfTrailingZeros(pos);
            queens[row] = col;

            solve(row + 1, n,
                  cols | pos,
                  (diag | pos) << 1,
                  (antiDiag | pos) >> 1,
                  queens, res);
        }
    }

    private List<String> buildBoard(int[] queens, int n) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
