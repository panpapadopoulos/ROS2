# ROS 2 Beginner Tutorials

Panagiotis Papadopoulos (papadop@purdue.edu)

These are my implementations of the beginner tutorials from https://docs.ros.org/en/foxy/Tutorials.html. I wrote the nodes in Python. The pluginlib tutorial is C++ only, so that part is in C++.

I used Ubuntu on WSL 2 with ROS 2 Lyrical, the version installed on my machine, so a few commands differ slightly from the Foxy pages (noted at the end).

## Packages

| Package | Type | Tutorials |
|---|---|---|
| `ros2_beginner_py` | Python | publisher/subscriber, service/client, parameters, launch files, using custom interfaces |
| `tutorial_interfaces` | CMake | creating custom msg and srv files (`Num.msg`, `Sphere.msg`, `AddThreeInts.srv`) |
| `more_interfaces` | CMake | implementing custom interfaces (`AddressBook.msg` used in the same package) |
| `beginner_plugins` | C++ | creating and using plugins (pluginlib) |

## Step 1: Open a terminal

Open the **Ubuntu** app from the Windows Start menu, or type `wsl` in PowerShell. All commands below run in this Ubuntu terminal, not in PowerShell.

## Step 2: Build (once)

Go to the folder that contains this README and the `src` folder, then build:

```bash
cd ~/projects/ros2_beginner_assignment
source /opt/ros/lyrical/setup.bash
colcon build
```

It should end with `Summary: 4 packages finished`.

## Step 3: Set up every terminal

Most tutorials need two terminals. **Every time you open a new terminal**, run these three lines first, or `ros2 run` will say the package is not found:

```bash
cd ~/projects/ros2_beginner_assignment
source /opt/ros/lyrical/setup.bash
source install/setup.bash
```

Press **Ctrl+C** to stop a running node before moving to the next tutorial.

## Step 4: Run the tutorials

### Publisher and subscriber

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run ros2_beginner_py publisher` | `ros2 run ros2_beginner_py subscriber` |

Terminal 1 prints `Publishing: "Hello ROS 2: 0"`, `1`, `2`, ... and Terminal 2 prints `Received: "Hello ROS 2: ..."` with the same numbers.

### Service and client

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run ros2_beginner_py service` | `ros2 run ros2_beginner_py client 2 3` |

The client prints `Result: 2 + 3 = 5` and exits. The service prints `Incoming request: a=2 b=3`.

### Custom message (Num.msg)

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run ros2_beginner_py custom_publisher` | `ros2 run ros2_beginner_py custom_subscriber` |

Terminal 2 prints `I heard: "0"`, `"1"`, `"2"`, ...

### Custom service (AddThreeInts.srv)

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run ros2_beginner_py custom_service` | `ros2 run ros2_beginner_py custom_client 2 3 1` |

The client prints `Result: 2 + 3 + 1 = 6`.

### Interface defined and used in the same package

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run more_interfaces publish_address_book` | `ros2 topic echo /address_book` |

Terminal 2 shows `first_name: John`, `last_name: Doe` and `phone_type: 2` (the `PHONE_TYPE_MOBILE` constant).

### Parameters

| Terminal 1 | Terminal 2 |
|---|---|
| `ros2 run ros2_beginner_py parameters` | `ros2 param set /parameter_demo my_parameter earth` |

Terminal 1 prints `Hello world!` every second, then `Hello earth!` after the `param set`.

Setting the parameter from a launch file (one terminal, stop the node above first):

```bash
ros2 launch ros2_beginner_py parameters_demo.launch.py greeting:=earth
```

It prints `Hello earth!`.

### Launch file

One terminal. Starts the publisher and subscriber together:

```bash
ros2 launch ros2_beginner_py beginner_demo.launch.py
```

You see both `Publishing:` and `Received:` lines in the same terminal.

### Plugins (C++)

One terminal:

```bash
ros2 run beginner_plugins area_demo
```

It prints `Square area: 100.00` and `Triangle area: 43.30`. The program only knows the `Polygon` base class; pluginlib loads `Square` and `Triangle` from the plugin library at runtime.

## CLI tutorials

These tutorials only use existing ROS tools, so there is no code for them. Do the setup from Step 3 in each terminal first.

**Turtlesim and rqt**

| Terminal 1 | Terminal 2 | Terminal 3 |
|---|---|---|
| `ros2 run turtlesim turtlesim_node` | `ros2 run turtlesim turtle_teleop_key` | `rqt` |

A turtle window opens. Click on Terminal 2 and use the arrow keys to drive the turtle.

**Nodes, topics, services, parameters and actions.** Keep turtlesim running and use Terminal 3:

```bash
ros2 node list
ros2 node info /turtlesim
ros2 topic list -t
ros2 topic echo /turtle1/cmd_vel
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
ros2 service call /spawn turtlesim_msgs/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
ros2 param list
ros2 param set /turtlesim background_r 150
ros2 param dump /turtlesim > turtlesim.yaml
ros2 action list -t
ros2 action send_goal /turtle1/rotate_absolute turtlesim_msgs/action/RotateAbsolute "{theta: 1.57}" --feedback
```

`topic echo` and `topic pub` keep running; stop them with Ctrl+C before the next command.

**rqt_console and ros2doctor**

```bash
ros2 run rqt_console rqt_console
ros2 doctor --report
```

**Recording and playing back data (ros2 bag)**

`ros2 bag record` saves the messages sent on a topic into a folder, and `ros2 bag play` sends them again later, so the turtle repeats the movement.

1. Terminal 1: `ros2 run turtlesim turtlesim_node`
2. Terminal 2: `ros2 run turtlesim turtle_teleop_key`
3. Terminal 3: start recording:
   ```bash
   ros2 bag record --topics /turtle1/cmd_vel
   ```
4. Click on Terminal 2 and drive the turtle with the arrow keys for a few seconds.
5. Go back to Terminal 3 and press Ctrl+C to stop recording. This creates a folder named after the date and time, for example `rosbag2_2026_10_18-21_13_44`. Run `ls` to see its real name.
6. Check that it recorded something (`Messages` should not be 0):
   ```bash
   ros2 bag info rosbag2_2026_10_18-21_13_44
   ```
7. Play it back, using your folder's name (type `rosbag2_` and press Tab to fill in the rest):
   ```bash
   ros2 bag play rosbag2_2026_10_18-21_13_44
   ```
   The turtle repeats the same moves without you touching the keyboard. It starts from where it is now, so the path is the same shape but in a different place.

## Differences from Foxy

- The turtlesim interfaces are in `turtlesim_msgs` instead of `turtlesim`.
- `ros2 bag record` takes `--topics` before the topic names.
