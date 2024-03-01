class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def winner(left, right, turn):
            if left == right:
                if turn == 0:
                    player1 = nums[left] 
                    player2 = 0
                else:
                    player2 = nums[left]
                    player1 = 0
                return player1, player2
            if turn == 0:
                player1, player2 = winner(left+1, right, 1)
                player1r,player2r = winner(left, right-1, 1)
                player1 += nums[left]
                player1r += nums[right]
                max_val1 = (max(player1,player1r))
                min_val2 = (min(player2, player2r))
                return max_val1, min_val2
            else:
                player1, player2 = winner(left+1, right, 0)
                player1r,player2r = winner(left, right-1, 0)
                player2 += nums[left]
                player2r += nums[right]
                max_val2 = (max(player2,player2r))
                min_val1 = (min(player1, player1r))
                return min_val1, max_val2
        player1, player2 = winner(0, len(nums)-1, 0)
        if player1 >= player2:
            return True
        return False
