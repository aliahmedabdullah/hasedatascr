import subprocess

# List of scripts to run
scripts = ['script1.py', 'script2.py', 'script3.py']

# Loop through each script and run it
for script in scripts:
    try:
        result = subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")

