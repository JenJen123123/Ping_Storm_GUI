
import customtkinter as ctk
import subprocess
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Ping Storm GUI")
app.geometry("600x400")

script_dir = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    output_box.delete('1.0', ctk.END)
    script_path = os.path.join(script_dir, script_name)
    try:
        output = subprocess.check_output(['bash', script_path], stderr=subprocess.STDOUT, text=True)
        output_box.insert(ctk.END, output)
    except subprocess.CalledProcessError as e:
        output_box.insert(ctk.END, f"Error:\n{e.output}")

# GUI elements for scripts
scripts = ['ping.sh', 'control.sh', 'Res_analyzing.sh', 'ps.sh', 'show.sh']
for script in scripts:
    btn = ctk.CTkButton(app, text=f"Run {script}", command=lambda s=script: run_script(s))
    btn.pack(pady=5)

# Output display
output_box = ctk.CTkTextbox(app, width=580, height=200)
output_box.pack(pady=10)

app.mainloop()
