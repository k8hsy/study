class BoardGame: # base class
  def __init__(self, width, height):
    self.board = []
    self.width = width
    self.height = height
    self.stone = {
      0: chr(0x26AA),
      1: chr(0x1F315)
    }

    for y in range (height):
      tmp = ['.']*width
      self.board.append(tmp)

   
  def print_board(self):
    for line in self.board:
      print(line)
    print('+'*self.width*5)

  def put_stone(self, player):
    # pseudo code 수도코드:
    # : 코드는 아닌데, 코드처럼 보이는 논리순서 메모
    '''
    [1] 좌표입력(x, y)
    [2] 빈자리인지 좌표 확인
      2-1) 빈자리이라면?
        put stone 후에 procedure 종료
      2-2) 이미 stone이 있다면?
        다시하라고 하고 [1]로 이동   
    '''
   
    while True: #입력이 되는 데이터를 예상할 수 없어서 에러 발생을 예측할 수 있을때 사용
      try: # 시도
        x,y = map(int, input('(x,y) 좌표 입력: ').split())
        if self.board[y][x] != '.':
          raise ValueError
        if x<0 or x>self.height or y<0 or y>self.width:
          raise ValueError
      except Exception: #에러
        print('warning! try again')
      else: #정상
        self.board[y][x] = self.stone[player]
        break

  def is_player_win(self):
    
    '''
    player가 이기는 경우
    x좌표가 같은 3점 (세로)
    y좌표가 같은 3점 (가로)
    3점이 모두 x+y가 2인 경우(오른쪽 대각선)
    3점이 모두 x=y일때 (왼쪽 대각선)

    player 1, 2의 좌표들을 dictionary에 저장
    위의 경우 중 하나라도 있으면 게임 종료

    '''
    #가로
    for y in range(3):
      if self.board[y][0] != '.':
        if self.board[y][0]==self.board[y][1] and self.board[y][1]==self.board[y][2]:
          return True

    #세로
    for x in range(3):
      if self.board[0][x] != '.':
        if self.board[0][x]==self.board[1][x] and self.board[1][x]==self.board[2][x]:
          return True

    #왼쪽 대각선
    if self.board[0][0]!= '.':
      if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
        return True

    #오른쪽 대각선
    if self.board[0][2] != '.':
      if self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]:
        return True

    return False

class TicTacToe(BoardGame):
  def __init__(self):
    super().__init__(3,3)

  def play_game(self):
    turn = 0
    flag = 0
    for i in range (9):
      self.print_board()
      self.put_stone(turn %2)
      turn += 1
      if self.is_player_win():
        self.print_board()
        print ("PLAYER" + str(turn%2) + " WINS!")
        flag = 1
        break
    if flag == 0:
      self.print_board()
      print("TIE")

tictactoe = TicTacToe()
tictactoe.play_game()
