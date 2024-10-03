import requests
from flask import Flask, render_template, request, redirect, url_for
from discover_ssdp import discover_roku_via_ssdp

app = Flask(__name__)


class RokuController:

    roku_port = 8060

    def __init__(self):
        discovered_addresses = discover_roku_via_ssdp()
        if not len(discovered_addresses) == 1:
            raise Exception('more than 1 roku you rich person.')
        else:
            ip = discovered_addresses[0]
        self.base_url = f"http://{ip}:{self.roku_port}"

    def send_command(self, command):
        url = f"{self.base_url}/{command}"
        print(url)
        response = requests.post(url)
        return response.status_code

    def keypress(self, key):
        return self.send_command(f"keypress/{key}")

    def launch_app(self, app_id):
        return self.send_command(f"launch/{app_id}")

    def search(self, query):
        return self.send_command(f"search/browse?keyword={query}")

    def play_pause(self):
        return self.keypress("Play")

    def home(self):
        return self.keypress("Home")

    def select(self):
        return self.keypress("Select")

    def volume_up(self):
        return self.keypress("VolumeUp")

    def volume_down(self):
        return self.keypress("VolumeDown")

    def mute(self):
        return self.keypress("VolumeMute")

    def power_off(self):
        return self.keypress("PowerOff")

    def power_on(self):
        return self.keypress("PowerOn")

    def right(self):
        return self.keypress("Right")

    def left(self):
        return self.keypress("Left")

    def up(self):
        return self.keypress("Up")

    def down(self):
        return self.keypress("Down")
    
    def back(self):
        return self.keypress("Back")
    
    def info(self):
        return self.keypress('Info')


@app.route("/")
def remote():
    return render_template("interactive_remote.html")


@app.route("/send_command", methods=["POST"])
def send_command():
    command = request.form.get("command")
    if command:
        if command == "power_on":
            roku.power_on()
        elif command == "power_off":
            roku.power_off()
        elif command == "up":
            roku.up()
        elif command == "down":
            roku.down()
        elif command == "left":
            roku.left()
        elif command == "right":
            roku.right()
        elif command == "select":
            roku.select()
        elif command == "volume_up":
            roku.volume_up()
        elif command == "volume_down":
            roku.volume_down()
        elif command == "mute":
            roku.mute()
        elif command == "home":
            roku.home()
        elif command == "play_pause":
            roku.play_pause()
        elif command == 'back':
            roku.back()
    return "OK", 200



if __name__ == "__main__":
    app.run(host="localhost", port=6969)
