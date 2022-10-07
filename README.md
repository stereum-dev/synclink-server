# SyncLink Server PoC

A very basic implementation of the [SyncLink Server](https://github.com/stereum-dev/synclink-spec/wiki/SyncLink-Server).

## Supported clients

| Client     | Support |
| ---------- | ------- |
| Teku       | ✅      |
| Nimbus     | ✅      |
| Lodestar   | ✅      |
| Lighthouse | ✅      |
| Prysm      | ✅      |

## Install Python 3

Please refer to the [official Python docs](https://www.python.org/doc/) to install Python >= 3.6 on your OS.

## Install additional Requirements on Windows

Start a virtual environment and install or update required Python packages:

```
python -m venv .venv
".venv/scripts/activate.bat"
pip install -r requirements.txt
```

## Install additional Requirements on Linux / MacOS

On Debian or Ubuntu you first need to install venv:

```
apt install pythonX.Y-venv
```

> Replace `X.Y` with the python MAJOR and MINOR version retrieved by `python -V`

Then start a virtual environment and install or update required Python packages:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configure the App

1. Copy `config.yaml.example` to `config.yaml`
2. Define settings in `config.yaml` as desired

| Name            | Description                                      | Default               | Required |
| --------------- | ------------------------------------------------ | --------------------- | -------- |
| addr            | The IP address or domain for the SyncLink server | 0.0.0.0               | No       |
| port            | The port for the SyncLink server                 | 8000                  | No       |
| eth_api_address | The url to your beacon node API                  | http://localhost:5051 | Yes      |

## Run the App

Activate the virtual environment and run the app.

On Windows:

```
".venv/scripts/activate.bat"
python main.py
```

On Linux / MacOS:

```
source .venv/bin/activate
python main.py
```

## Open API Docs

After the app is started you can visit the API docs (depending on your settings in `config.yaml`) by default at <http://127.0.0.1:8000/docs>.

## Stop the App

If you're done you can stop the Python process and deactivate the virtual environment by typing the following in your active terminal:

```
CTRL+C
deactivate
```
