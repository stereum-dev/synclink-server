# WARNING

**CURRENTLY IN DEVELOPMENT - DO NOT USE IN PRODUCTION!**

You can start the SyncLink Server as described in this document however during development we continue implementing changes that could (and very likely will) make some or all of the described operations and tasks below obsolete.

# SyncLink Server

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

Please refer to the [official Python docs](https://www.python.org/doc/) to install Python >= 3.10 on your OS.

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

Optional you can also specify the path to your config file or add/overwrite this arguments on the command line.
Run `python main.py -h` for details.

### Environment variables

You can also configure your app by environment variables. These are identical to the command line arguments but must be prefixed with "SYLI_" and always UPPERCASE.
For example, to specify `addr` as environment variable:

```
export SYLI_ADDR="127.0.0.1"
python main.py
```
will be converted to `python main.py --addr "127.0.0.1"`.

For lists, the environment variables need additionally suffixed with a number, e.g.:
```
export SYLI_NODE_1="10.0.0.1"
export SYLI_NODE_2="10.0.0.2"
python main.py
```
will be converted to `python main.py --node "10.0.0.1"  --node "10.0.0.2"`.

> However, this is just a demo because the SyncLink Server currently has no arguments that require a list!

If you have accidently specified an environment variable that is not suported on the command line, you need to unset the variable to avoid an error. For example:

```
export SYLI_BLA="12345"
python main.py
```
will be converted to `python main.py --bla "12345"`.

and of course results in the error `main.py: error: unrecognized arguments: --bla 12345`.

Therefore, you'd have to remove the environment variable:

```
unset SYLI_BLA
```
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
