"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
----------------------
File: breakout.py
Name: Freddy Wu
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    Description: You have three lives to play this breakout game. Enjoy it~
    1. Use class(BreakoutGraphics) to make our window(graphics) and setup some initial parameters
    2. Use "is_in_a_move" controlled by onmouseclick to start the game
    3. Check whether there is a collision between ball and wall
    4. Check whether there is a collision between ball and bricks or paddle
    5. If ball is collided with bricks, remove this brick and turn the direction of velocity
    6. If ball is collided with paddle, just turn the direction of velocity
    7. Repeat step2 to step7 until game over.
    """

    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if lives <= 0 or graphics.score == graphics.brick_c*graphics.brick_r:                                           # If there is no lives, then break
            break
        else:
            if graphics.is_in_a_move:                            # 'is_in_a_move' is a switch controlled by onmouseclick
                graphics.set_ball_velocity()
                print(graphics.window.width, graphics.window.height)
                while True:
                    pause(FRAME_RATE)
                    if graphics.ball_is_out:             # Lives would decrease if ball is out of low boundary
                        graphics.is_in_a_move = False
                        lives -= 1
                        break                                      # If ball is out of low boundary, then break.
                    else:
                        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                        graphics.check_brick2()
                        graphics.check_wall()

                graphics.ball_is_out = False
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball,x=(graphics.window.width-graphics.ball.width)/2,\
                                    y=((graphics.window.height-graphics.ball.height)/2))

    graphics.window.remove(graphics.ball)
    graphics.the_end()


if __name__ == '__main__':
    main()
