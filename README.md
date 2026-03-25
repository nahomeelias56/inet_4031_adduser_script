# Inet 4031 Adduser Script

# Program Description

This program automates the process of creating user accounts on a Linux system. Instead of manually running multiple commands for each user, the script allows a user to provide all required information in a single input file and processes it automatically. This saves time, reduces human error, and ensures consistency when creating multiple accounts.

Normally, a system administrator would create users manually using commands such as `/usr/sbin/adduser`, `/usr/bin/passwd`, and `/usr/sbin/adduser <user> <group>` to assign group memberships. This script uses those same commands behind the scenes, but automates them by reading structured input and executing the commands programmatically. This allows bulk user creation with a single command.

---

# Program User Operation

This program reads user data from an input file and creates accounts accordingly. The user prepares the input file, runs the script, and selects whether to execute in dry-run mode or normal mode. The script processes each line, creates users, sets passwords, and assigns groups automatically.

---

## Input File Format

Each line in the input file represents one user and must contain exactly five fields separated by colons (`:`):

### Field Breakdown:
- **username** → The login name for the new user  
- **password** → The password assigned to the user  
- **last_name** → User’s last name  
- **first_name** → User’s first name  
- **groups** → Comma-separated list of groups (e.g., `group01,group02`)  

### Special Cases:
- To **skip a line**, begin it with `#` (treated as a comment)  
- To **avoid assigning groups**, use `-` in the group field  

## Dry Run

When the program starts, the user is prompted to choose dry-run mode by entering **Y** or **N**.

- If **Y (Yes)** is selected:
  - The script does **not execute any system commands**
  - It prints the commands that *would have been executed*
  - It displays messages when a line is skipped (e.g., comment lines)
  - It shows errors if a line does not contain the required number of fields  

- If **N (No)** is selected:
  - The script executes all commands normally  
  - Users are created, passwords are set, and groups are assigned  
  - No extra error or skipped-line messages are displayed  

Dry-run mode is useful for testing and verifying the input file before making actual changes to the system.
