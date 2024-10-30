#include <iostream>
#include <vector>

int countElementsBruteForce(const std::vector<std::vector<int>>& matrix, int i1, int j1, int i2, int j2) {
    int n = matrix.size(), m = matrix[0].size();
    int lower = matrix[i1][j1], upper = matrix[i2][j2];
    int result = 0, nops = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] < lower || matrix[i][j] > upper)
                result++;
            nops++;
        }
    }
    std::cout << "Full computation number of ops: " << nops << ". Result: " << result << std::endl;
    return result;
}

int countElements(const std::vector<std::vector<int>>& matrix, int i1, int j1, int i2, int j2) {
    int n = matrix.size(), m = matrix[0].size();
    int lower = matrix[i1][j1], upper = matrix[i2][j2];
    int result = 0, nops = 0;

    // Count rows smaller than i1
    for (int i = 0; i < i1; i++) {
        for (int j = 0; j < m; j++) {
            nops++;
            if (matrix[i][j] >= lower) {
                result += j;
                break;
            } else if (j == m - 1)
                result += m;
        }
    }

    // Count columns smaller than j1
    for (int j = 0; j < j1; j++) {
        for (int i = i1 + 1; i < n; i++) {
            nops++;
            if (matrix[i][j] >= lower) {
                result += i - i1;
                break;
            } else if (i == n - 1)
                result += n - i1;
        }
    }

    // Count rows greater than i2
    for (int i = i2 + 1; i < n; i++) {
        for (int j = m - 1; j >= 0; j--) {
            nops++;
            if (matrix[i][j] <= upper) {
                result += m - j - 1;
                break;
            } else if (j == 0)
                result += m;
        }
    }

    // Count columns greater than j2
    for (int j = j2 + 1; j < m; j++) {
        for (int i = i2 - 1; i >= 0; i--) {
            nops++;
            if (matrix[i][j] <= upper) {
                result += i2 - i;
                break;
            } else if (i == 0)
                result += i2 + 1;
        }
    }

    std::cout << "Reduced computation number of ops: " << nops << ". Result: " << result << std::endl;
    return result;
}

int main() {
    std::vector<std::vector<int>> matrix = {{1, 3, 7, 10, 15, 20},
                                           {2, 6, 9, 14, 22, 25},
                                           {3, 8, 10, 15, 25, 30},
                                           {10, 11, 12, 23, 30, 35},
                                           {20, 25, 30, 35, 40, 45}};

    std::cout << countElementsBruteForce(matrix, 1, 1, 3, 3) << std::endl; // 14
    std::cout << countElements(matrix, 1, 1, 3, 3) << std::endl; // 14
    return 0;
}