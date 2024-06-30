# kinematics
Simple control script for Physcial Sun Simulator. Note that the following guide was written for linux.
## How to install
1. Clone the kinematics repository:
  ```bash
  git clone https://github.com/Physical-Sun-Simulator/kinematics
  ```
2. Make a virtual environment:
  ```bash
  python3 -m venv venv
  ```
3. Start the virtual environment:
  ```bash
  source venv/bin/activate
  ```
3. Install the requirements:
  ```bash
  pip install -r requirements.txt
  ```
## How to run
1. Start the virtual environment:
  ```bash
  source venv/bin/activate
  ```
2. Execute the file:
  ```bash
  python3 kinematics.py
  ```
## Control flow
1. Initializes the arm and table
2. Prompts the user for:
- Table angle
- Table direction
- Table speed
- Arm angle
- Arm direction
- Arm speed
3. Moves the machine to the specified configuration in the specified manner.
