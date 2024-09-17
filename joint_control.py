from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np
 
def main():
    # Define a list of multiple sets of joint angles in radians
    joint_positions_list = [
        [np.radians(90), np.radians(0), np.radians(0), np.radians(0)],   # First set of joint positions
        [np.radians(-90), np.radians(0), np.radians(0), np.radians(0)],  
        [np.radians(0), np.radians(45), np.radians(0), np.radians(0)],  # second joint movements
        [np.radians(0), np.radians(-45), np.radians(0), np.radians(0)],    
        [np.radians(0), np.radians(0), np.radians(90), np.radians(0)],    # third joint movements
        [np.radians(0), np.radians(0), np.radians(-90), np.radians(0)],
        [np.radians(0), np.radians(0), np.radians(0), np.radians(90)],    # fourth joint movements
        [np.radians(0), np.radians(0), np.radians(0), np.radians(-90)]
    ]
 
    # Initialize the robot object
    bot = InterbotixManipulatorXS(robot_model='px100', group_name='arm', gripper_name='gripper')
 
    # Move the robot to home position at the start
    bot.arm.go_to_home_pose()
 
    # Loop through each set of joint positions
    for joint_positions in joint_positions_list:
        print(f"Setting joint positions to: {joint_positions}")
        # Set the joint positions
        bot.arm.set_joint_positions(joint_positions)
       
        # Pause to allow the robot to reach the position
        bot.arm.go_to_sleep_pose()
       
    # Return to home pose after completing all movements
    bot.arm.go_to_home_pose()
 
    # Move the robot to sleep pose at the end
    bot.arm.go_to_sleep_pose()
 
    # Shutdown the robot object
    bot.shutdown()
 
if __name__ == '__main__':
    main()