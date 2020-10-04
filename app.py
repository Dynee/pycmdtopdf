import subprocess, sys
from fpdf import FPDF

class App():
    def __init__(self, command, flags=[]):
        self.command = command
        self.flags = flags
    def run(self):
        try:
            flag = " ".join(self.flags)
            process = subprocess.Popen(
                [self.command, flag], 
                universal_newlines=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            if stderr:
                raise Exception(stderr)
            try:
                filename = f"{self.command}"
                with open(f"{filename}.txt", "w") as f:
                    f.write(stdout);
                    
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size = 15) 

                with open(f"{filename}.txt", "r") as f:
                    for entry in f:
                        pdf.cell(200, 10, txt = entry,  ln = 1, align = 'L')
                        
                pdf.output(f"{self.command}.pdf") 
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
                
f, command, *flags = sys.argv
app = App(command=command, flags=flags)
app.run()
