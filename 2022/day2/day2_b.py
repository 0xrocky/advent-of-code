#  First Col   #  Second Col
## A = Rock    ## X = Lose
## B = Paper   ## Y = Draw
## C = Scissor ## Z = Win

# Score
## 1 = Rock
## 2 = Paper
## 3 = Scissors
## 0 = lost
## 3 = draw
## 6 = won

###################
#####|_A_|_B_|_C_|#
#|_X_|3+0|1+0|2+0|#
#|_Y_|1+3|2+3|3+3|#
#|_Z_|2+6|3+6|1+6|#
###################

matrix_move_score = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]

def ord_first_col(chr):
	# ASCII: A = 65
	return ord(chr) - 65
def ord_second_col(chr):
	# ASCII: X = 88
	return ord(chr) - 88

with open('input') as f:
# reading from the file without '\n'
	lines = [line.rstrip() for line in f]

sum = 0
for line in lines:
	sum += matrix_move_score[ord_first_col(line[0])][ord_second_col(line[2])]
print(sum)
