function solution(matrix) {
  /**
   *   This function finds the maximum sum of points achievable by 
   * placing two non-attacking rooks on a chessboard represented by a matrix.
  Args:
      matrix: A 2D list representing the chessboard, where each element is the 
      point value of a square.
  Returns:
      The maximum sum of points achievable by placing two non-attacking rooks.
   * 
   */
  let max_score = 0;
  let a = {};
  let b = [];

  for (let i = 0; i < matrix.length; i++) 
  {
      for (let j = 0; j < matrix[i].length; j++) 
      {
          a['' + i + j] = matrix[i][j];
          b.push([i, j]);
      }
  }

  for (let i = 0; i < b.length; i++) 
    { 
      for (let j = i + 1; j < b.length; j++) 
      {
          let sum = a[b[i].join('')] + a[b[j].join('')];
          if (b[j][0] !== b[i][0] && b[j][1] !== b[i][1] && sum > max_score) 
          {
              max_score = sum;
          }
      }
  }

  return max_score;
}

test_1 = [[1, 4],
          [2, 3]];


test_2 = [[15, 1, 5],
          [16, 3, 8],
          [2, 6, 4]];

test_3 = [[12, 12],
          [12, 12],
          [0, 7]];

test_4 = [[1, 2, 14],
          [8, 3, 15]];


console.log(solution(test_1))
console.log(solution(test_2))
console.log(solution(test_3))
console.log(solution(test_4))