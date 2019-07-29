print("Preparing...")
print("Preparing to install package...")
import platform 
if platform.system().upper() == 'DARWIN':
  print("OS: DARWIN")
  print("PKG: HOMEBREW")
  print("Installing package HOMEBREW...")
  print("Install:\n1: HOMEBREW_LATEST\n2: ")
  op = input("INSTALL")
  if op.upper() == "1" or op.upper() == "HOMEBREW_LATEST":
    import os
    import subprocess
    os.system("/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
    print("Ok. Rerun software and strike 2")
    
  else:
    import subprocess
    import os
    print("BREW: CHECKING FOR BREW...")
    subprocess.popen(["brew", "--help"])
    except:
      print("BREW REQUIRED TO CONTINUE.")
      input()
      exit()
    print("Installing Python3")
    os.system("brew install python3")
    print("Action: Installing kivy")
    os.system("python -m pip install kivy")
    print("Action: Installing buildozer")
    os.system("pip install buildozer")
    print("Action: User: INSTALL: Complete: Please run buildozer init in directory to build in and hit enter")
    input()
    devdir = input("Enter full directory: ")
    print("OK.")
    os.system("cd " + devdir + " && buildozer deploy android")
    print("OK. APK in " + devdir + "/bin")
   
    
    
    
