"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 8       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    '''
    Description:
    1. Set up initial attributes.
    2. Create graphical window
    3. Create a paddle & filled ball in the graphical window
    4. Draw bricks
    5. Default initial velocity for the ball & Initialize our mouse listeners
    6. Make method to check collision between ball and wall or bricks
    '''
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):   # 方便改constant

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height)
        self.paddle_offset = paddle_offset
        self.paddle.filled = True
        self.paddle.color = 'gray'
        self.paddle.fill_color = 'gray'

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'pink'
        self.ball.fill_color = 'pink'
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)                    # Set up one velocity randomly, then change
        self.__dy = INITIAL_Y_SPEED                                   # direction of velocity by conditions of methods

        # Initialize our mouse listeners
        onmousemoved(self.track)
        onmouseclicked(self.switch)
        self.is_in_a_move = False

        # Draw bricks
        self.brick_r = brick_rows
        self.brick_c = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset
        self.draw_bricks()

        # Ball's attributes
        self.ball.r = ball_radius

        # maybe_brick attributes
        self.maybe_brick = self.window.get_object_at(self.ball.x,self.ball.y)
        self.brick_x0 = 0
        self.brick_y0 = 0

        # Setup label
        self.score = 0                                      # 小心!! 要放在method之前
        self.label = GLabel('Scores:' + str(self.score))
        self.setup_label()

        # Setup life
        self.setup_life()
        self.rect0 = GRect(12, 12)
        self.time = 0
        self.ball_is_out = False

        # Minus life

    def setup_label(self):
        # self.score = 0                          # 為什麼要有這一行??
        # print(self.score)
        self.label = GLabel('Scores:'+str(self.score))  # 跨method 所以要再上面寫
        self.label.color = 'black'
        self.label.font = 'Courier-12-bold'
        self.window.add(self.label, x=10, y=30)

    def setup_life(self):
        for i in range(3):
            self.rect0 = GRect(12, 12)
            self.rect0.filled = True
            self.rect0.color = 'magenta'
            self.rect0.fill_color = 'magenta'
            self.window.add(self.rect0, x=420-20*i, y=15)
        # remove1 = self.window.get_object_at(x=420-20*1, y=610)       # 如果用loop製造多個物件，電腦"當下"只會儲存最新的一個物件
        # self.window.remove(remove1)                                  # 要移除其餘物件的話要先用get_object_at 來取得物件，再移除

    def check_wall(self):
        print('time:', self.time)
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        elif self.ball.x <= 0:
            self.__dx = -self.__dx

        elif self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx

        elif self.ball.y >= self.window.height:   # For testing
            self.ball_is_out = True
            remove1 = self.window.get_object_at(x=380+20*self.time, y=15)
            self.window.remove(remove1)
            self.time += 1
            print('New time:', self.time)

    def check_brick2(self):                                # Set up four corners to determine whether there is an object  # 碰到板子就直接把球往上移就不會抖
        self.left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        self.right_up = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        self.left_down = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.right_down = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y + self.ball.height)

        if self.ball.y + self.ball.height < self.paddle.y:     # Brick
            if self.left_up is not None and self.left_up is not self.label:
                self.window.remove(self.left_up)
                self.__dy = -self.__dy
                self.score += 1
            elif self.right_up is not None and self.right_up is not self.label:
                self.window.remove(self.right_up)
                self.__dy = -self.__dy
                self.score += 1
            elif self.left_down is not None and self.left_down is not self.label:
                self.window.remove(self.left_down)
                self.__dy = -self.__dy
                self.score += 1
            elif self.right_down is not None and self.right_down is not self.label:
                self.window.remove(self.right_down)
                self.__dy = -self.__dy
                self.score += 1
            self.label.text = 'Scores:' + str(self.score)
            # print(self.score)
            return self.score

        elif self.ball.y + self.ball.height >= self.paddle.y:                                                # Paddle
            if self.left_up is not None:
                self.__dy = -self.__dy
            elif self.right_up is not None:
                self.__dy = -self.__dy
            elif self.left_down is not None:
                self.__dy = -self.__dy
            elif self.right_down is not None:
                self.__dy = -self.__dy

    def check_brick(self):                  # 要設四個corner，還有 if 跟 else if 來檢查。才不會同時偵測到兩個，因此速度負負得正而沒有反彈
        num = 0
        for i in range(2):
            for j in range(2):
                self.maybe_brick = self.window.get_object_at(self.ball.x+i*self.ball.height,self.ball.y+j*self.ball.height)
                if self.maybe_brick is not None:
                    if self.ball.y + self.ball.height <= self.paddle.y:                              # brick
                        self.window.remove(self.maybe_brick)
                        self.__dy *= -1
                        num += 1
                    elif self.ball.y + self.ball.height >= self.paddle.y:                            # paddle
                        self.__dy = -self.__dy

    def switch(self, m):
        self.is_in_a_move = True
        print('----------')
        # self.set_ball_velocity()

    def set_ball_velocity(self):                      # Increase the fun of game
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            # print(random.random())                  # Each random.random is different from 0 to 1
            self.__dx = -self.__dx
            self.__dy = self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def track(self, m):                                                   # Function in onmousemoved, m is data of mouse
        # 用 if 設兩個 x 與 y 的邊界
        self.paddle.x = m.x - self.paddle.width / 2
        if m.x <= self.paddle.width / 2:                                  # left m.x boundary
            self.paddle.x = 0
        if m.x >= self.window.width - self.paddle.width / 2:              # right m.x boundary
            self.paddle.x = self.window.width - self.paddle.width

        self.paddle.y = self.window.height - self.paddle_offset           # paddle.y is a constant
        self.window.add(self.paddle, x=self.paddle.x, y=self.paddle.y)

    def draw_bricks(self):
        for i in range(self.brick_r):  # 上限不包含
            for j in range(self.brick_c):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                if 0 <= j < 2:
                    brick.fill_color = 'red'
                    brick.color = 'red'
                elif 2 <= j < 4:
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                elif 4 <= j < 6:
                    brick.fill_color = 'yellow'
                    brick.color = 'yellow'
                elif 6 <= j < 8:
                    brick.fill_color = 'green'
                    brick.color = 'green'
                else:
                    brick.fill_color = 'blue'
                    brick.color = 'blue'
                self.window.add(brick, x=0 + i * self.brick_width + i * self.brick_spacing, \
                                y=self.brick_offset + j * self.brick_height + j * self.brick_spacing)

    def the_end(self):
        num = 0
        vx = 1
        vy = 0
        if self.score <= 4:
            gameover = GLabel('Game Over')
            gameover.color = 'goldenrod'
            gameover.font = 'Courier-35-bold'
            self.window.add(gameover, x=80, y=400)
            while True:
                pause(1000 / 120)
                if num == 10:
                    break
                else:
                    gameover.move(vx,vy)
                    if gameover.x + gameover.width >= self.window.width or gameover.x == 0:
                        vx = -vx
                        num += 1
        elif self.score >= 5:
            goodgame = GLabel('Congratulation!')
            goodgame.color = 'red'
            goodgame.font = 'Courier-30-bold'
            self.window.add(goodgame, x=30, y=400)
            while True:
                pause(1000 / 120)
                if num == 100:
                    break
                else:
                    goodgame.move(vx,vy)
                    if 0 <= goodgame.x <= 20:
                        goodgame.color = 'red'
                    elif 20 <= goodgame.x <= 40:
                        goodgame.color = 'orange'
                    elif 40 <= goodgame.x <= 60:
                        goodgame.color = 'yellow'
                    elif 60 <= goodgame.x <= 80:
                        goodgame.color = 'green'
                    elif 80 <= goodgame.x <= 100:
                        goodgame.color = 'blue'
                    elif 100 <= goodgame.x <= 109:
                        goodgame.color = 'purple'
                    if goodgame.x + goodgame.width >= self.window.width or goodgame.x == 0:
                        vx = -vx
                        num += 1
                        print(goodgame.x)





