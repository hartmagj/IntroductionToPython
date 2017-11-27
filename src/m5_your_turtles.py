"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Grant Hartman.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg;
window = rg.TurtleWindow();

black_turtle = rg.SimpleTurtle("turtle");
blue_turtle = rg.SimpleTurtle("turtle");
red_turtle = rg.SimpleTurtle("turtle");

black_turtle.pen = rg.Pen("black", 3);
blue_turtle.pen = rg.Pen("blue", 3);
red_turtle.pen = rg.Pen("red", 3);

black_turtle.speed = 100;
blue_turtle.speed = 100;
red_turtle.speed = 100;

bSize = 0;

for k in range(30):
    black_turtle.draw_regular_polygon(3,bSize + (k*10));

    black_turtle.pen_up();
    black_turtle.forward(bSize + k*5);
    black_turtle.right(20);

    black_turtle.pen_down();

for k in range(30):
    blue_turtle.draw_regular_polygon(4,bSize + (k*10));

    blue_turtle.pen_up();
    blue_turtle.forward(bSize + k*5);
    blue_turtle.right(20);

    blue_turtle.pen_down();

for k in range(30):
    red_turtle.draw_regular_polygon(5,bSize + (k*10));

    red_turtle.pen_up();
    red_turtle.forward(bSize + k*5);
    red_turtle.right(20);

    red_turtle.pen_down();

window.close_on_mouse_click()