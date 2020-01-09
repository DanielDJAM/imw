from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from vm import VirtualMachine
 
app = Flask(__name__)
vmachine = VirtualMachine(1)
 
 
@app.route("/")
def index():
    return render_template("index.html", vmachine=vmachine)
 
 
@app.route("/change_status/<new_status>")
def change_status(new_status):
    if new_status == "0":
        vmachine.stop()
    elif new_status == "1":
        vmachine.start()
    else:
        vmachine.suspend()
    return redirect("/")
 
 
@app.route("/run_process", methods=["GET", "POST"])
def run_process():
    if request.method == "POST":
        vmachine.run(
            int(request.form["pid"]),
            float(request.form["ram"]),
            float(request.form["cpu"]),
            float(request.form["hdd"]),
        )
        return redirect("/")
    else:
        return render_template("run_process.html")
 
 
if __name__ == "__main__":
    app.run(debug=True)
