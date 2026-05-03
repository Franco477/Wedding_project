from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

with open("list/guests.json") as f:
    guests = json.load(f)

@app.route("/invite/<guest_id>")
def invite(guest_id):
    guest = guests.get(guest_id)

    if not guest:
        abort(404)

    return render_template("invite.html", name=guest["name"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
