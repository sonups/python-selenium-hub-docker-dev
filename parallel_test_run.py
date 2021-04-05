from subprocess import Popen


processes = []

for counter in range(2):
    chrome_cmd = 'python test.py'
    #firefox_cmd = 'SET BROWSER=firefox && python test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    #processes.append(Popen(firefox_cmd, shell=True))

for counter in range(2):
    processes[counter].wait()
