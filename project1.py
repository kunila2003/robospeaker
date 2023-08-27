import os

if __name__ == '__main__':
    print("Welcome to rospeaker 1.1. Created by Kunila")
    while True:
          x = input("Enter what you want to speak: ")
          if x == "q":
               break
          #this command is for male voice
          # command = f'start /MIN cmd /c "echo {x} | powershell -command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())\""'
          #this command is for female voice
          command = f'start /MIN cmd /c "echo {x} | powershell -command \"Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.SelectVoiceByHints([System.Speech.Synthesis.VoiceGender]::Female); $synth.Speak([Console]::In.ReadToEnd())\""'
          os.system(command)
