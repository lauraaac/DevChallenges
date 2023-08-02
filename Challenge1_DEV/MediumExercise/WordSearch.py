import time

class Solution:

    def exist(self, board, word) -> bool:
      return self.searchFirst(word, len(board), len(board[0]), board)

    def searchFirst(self, word, rows, columns, board):
      for i in range(rows):
        for j in range(columns):
          #If find match with the first word letter
          if(word[0] == board[i][j]): 

            #Instanciate a axiliar varible to know when the word has been found     
            counter = 0
            #Auxiliar board to allocate used letters
            checkedLetters = [[0]*len(board[0]) for i in range (len(board))]
            #search
            if(self.depthSearch(word, i, j, board, checkedLetters, counter)):
              return True
      return False

    def depthSearch(self, word, row, column, board, checkedLetters, counter):

      #Check if the word was already found
      if(len(word)  == counter):
        return True

      #Evaluate borders
      if(row < 0 or column < 0 or row >= len(board) or column >= len(board[0])):
        return False        

      #If there is match with the current letter and current letter of board and if the letter has not been already used
      if(board[row][column] == word[counter] and checkedLetters[row][column] == 0):

        #Udpate auxiliar board
        checkedLetters[row][column] = 1

        #Update counter of read letters
        counter += 1
        
        #Search in adjacent row above, Search in adjacent column forward, Search in adjacent row below, Search in adjacent column back
        result = (self.depthSearch(word, row + 1, column, board, checkedLetters, counter) or 
                self.depthSearch(word, row, column + 1, board, checkedLetters, counter) or 
                self.depthSearch(word, row - 1, column, board, checkedLetters, counter) or 
                self.depthSearch(word, row, column - 1, board, checkedLetters, counter))
        
        #Update auxiliar board 
        checkedLetters[row][column] = 0
        return result
        

solution = Solution()

start = time.time()
solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")

end = time.time()
#print execution time
print("Execution time:", "{:.20f}".format(end-start))