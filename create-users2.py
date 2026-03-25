#!/usr/bin/python3

# Script to create users from input with optional dry-run mode

import os      # run system commands
import re      # detect comment lines
import sys     # read input from stdin

def main():
    # Ask user if they want dry-run (no actual changes)
    choice = input("Run in dry-run mode? (Y/N): ").strip().lower()
    dry_run = True if choice == 'y' else False

    # Read each line from input file
    for line in sys.stdin:

        # Check for comment lines starting with '#'
        match = re.match("^#", line)

        # Split line into 5 expected fields
        fields = line.strip().split(':')

        # Skip comments or invalid lines (not 5 fields)
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("Skipping comment line:", line.strip())
                else:
                    print("Invalid line:", line.strip())
            continue

        # Extract user info
        username = fields[0]
        password = fields[1]

        # Format full name (GECOS field)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups (comma-separated)
        groups = fields[4].split(',')

        # Create user
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # Set password
        print(f"==> Setting password for {username}...")
        cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # Assign groups (skip '-')
        for group in groups:
            if group != '-':
                print(f"==> Adding {username} to {group}...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
