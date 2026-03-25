#!/usr/bin/python3

# INET4031
# Nahome Elias
# Tuesday March 24
# Tuesday March 24

# Imports used for interacting with the system (os), pattern matching (re), and reading input (sys)
import os
import os
import re
import sys

def main():
    for line in sys.stdin:

	# Check if the line starts with '#' which indicates a comment and should be ignored
        match = re.match("^#",line)

	#  Remove whitespace and split the line into fields using ':' as the delimiter
        fields = line.strip().split(':')

	#  Skip processing if the line is a comment (identified by '#') or if it is improperly formatted 
	# (does not contain exactly 5 colon-separated fields required for user creation)
        if match or len(fields) != 5:
            continue

	# Extract user information: username, password, and format the GECOS field (full name info for /etc/passwd
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

	# Split the group field into a list since a user can belong to multiple groups separated by commas
        groups = fields[4].split(',')

        # Prints out the user that a new account is being created
        print("==> Creating account for %s..." % (username))
        # Build the command to create a new user with no password login and specified GECOS information
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Shows the command to be executed to the terminal and has the system run that command.
        print(cmd)
        os.system(cmd)

        # Print out the user that the password is being set
        print("==> Setting the password for %s..." % (username))
        # Build the command to set the user's password by passing it twice into the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Shows the command to be executed to the terminal and has the system run that command.
        print(cmd)
        os.system(cmd)

        for group in groups:
        # Check that the group is valid (not '-') before assigning the user to it
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
