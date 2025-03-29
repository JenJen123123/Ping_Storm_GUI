
import customtkinter as ctk
import subprocess
import os
from functools import partial


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Ping Storm GUI")
app.geometry("600x400")

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    output_box.delete('1.0', ctk.END)
    output_box.insert(ctk.END, f"Button clicked: {script_name}\n\n")
    
    script_path = os.path.join(script_dir, script_name)

    if not os.path.isfile(script_path):
        output_box.insert(ctk.END, "Error: Script file not found.\n")
        return
    if not os.access(script_path, os.X_OK):
        output_box.insert(ctk.END, "Error: Script is not executable.\n")
        return
    
    try:
        result = subprocess.run(
            ['bash', script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=script_dir
        )
        output_box.insert(ctk.END, result.stdout if result.stdout else "Script ran with no output.")
    except Exception as e:
        output_box.insert(ctk.END, f"Exception occurred:\n{str(e)}")




# GUI elements for scripts
scripts = ['ping.sh', 'control.sh', 'Res_analyzing.sh', 'ps.sh', 'show.sh', 'test.sh']
for script in scripts:
    btn = ctk.CTkButton(app, text=f"Run {script}", command=partial(run_script, script))
    btn.pack(pady=5)


# Output display
output_box = ctk.CTkTextbox(app, width=580, height=200)
output_box.pack(pady=10)

app.mainloop()
