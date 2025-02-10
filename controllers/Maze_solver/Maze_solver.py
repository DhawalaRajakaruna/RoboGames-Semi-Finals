"""flood_fill_py controller."""

"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
#my modules
from Constants import *
import main_functions as main_f
import move_functions as move_f
import algorithm_functions as algorithms



def run_robot(robot):
    main_f.floodfill_main(robot)
    # match mode_params.ALGORITHM:
    #     case algorithms.KEYBOARD:
    #         print("Keyboard mode")
    #         main_f.keyboard_main(robot)
    #     case algorithms.FLOODFILL:
    #         print("Floodfill mode")
    #         main_f.floodfill_main(robot)
    #     case algorithms.DFS:
    #         print("DFS mode")
    #         main_f.DFS_main(robot)
    #     case algorithms.BFS:
    #         print("BFS mode")
    #         main_f.BFS_main(robot)
    #     case algorithms.A_STAR:
    #         print("A* mode")
    #         main_f.A_star_main(robot)
    #     case algorithms.A_STAR_MOD:
    #         print("A* modified mode")
    #         main_f.A_star_main_modified(robot)
    

if __name__ == "__main__":
    
    robot = Robot()
    
    run_robot(robot)