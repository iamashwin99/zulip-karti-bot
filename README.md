# Kartoffel Bot - MPSD Zulip

Assuming the repo is cloned at `~/sandbox/zulip-karti-bot` create the following systemd service:

```bash
[Unit]
Description=Karti Zulip Bot
After=network.target

[Service]
Type=simple
User=karnada
WorkingDirectory=/home/karnada/sandbox/zulip-karti-bot
ExecStart=/bin/bash -c "source /home/karnada/sandbox/zulip-karti-bot/zulip-api-py3-venv/bin/activate && zulip-run-bot karti --config-file zuliprc"
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
To use this service, save the file as `karti-zulip-bot.service` in the `/etc/systemd/system` directory. Then, you can start the service using the following command:
```
sudo systemctl start karti-zulip-bot
```
To enable the service to start automatically at boot, use the following command:

```
sudo systemctl enable karti-zulip-bot```

Note: Make sure to replace `/sandbox/zulip-karti-bot/zulip-api-py3-venv/bin/activate` with the actual path to the script that activates your virtual environment, and `zulip-run-bot karti --config-file zuliprc` with the actual command you want to run.


# Zulip API

[![Build status](https://github.com/zulip/python-zulip-api/workflows/build/badge.svg)](https://github.com/zulip/python-zulip-api/actions?query=branch%3Amain+workflow%3Abuild)
[![Coverage status](https://img.shields.io/codecov/c/github/zulip/python-zulip-api)](https://codecov.io/gh/zulip/python-zulip-api)

This repository contains the source code for Zulip's PyPI packages:

* `zulip`: [PyPI package](https://pypi.python.org/pypi/zulip/)
  for Zulip's API bindings.
* `zulip_bots`: [PyPI package](https://pypi.python.org/pypi/zulip-bots)
  for Zulip's bots and bots API.
* `zulip_botserver`: [PyPI package](https://pypi.python.org/pypi/zulip-botserver)
  for Zulip's Flask Botserver.

The source code is written in *Python 3*.

## Development

This is part of the Zulip open source project; see the
[contributing guide](https://zulip.readthedocs.io/en/latest/overview/contributing.html)
and [commit guidelines](https://zulip.readthedocs.io/en/latest/contributing/version-control.html).

1. Fork and clone the Git repo, and set upstream to zulip/python-zulip-api:

   ```
   git clone https://github.com/<your_username>/python-zulip-api.git
   cd python-zulip-api
   git remote add upstream https://github.com/zulip/python-zulip-api.git
   git fetch upstream
   ```
2. Make sure you have [pip](https://pip.pypa.io/en/stable/installing/).
3. Run:

   ```
   python3 ./tools/provision
   ```

   This sets up a virtual Python environment in `zulip-api-py<your_python_version>-venv`,
   where `<your_python_version>` is your default version of Python. If you would like to specify
   a different Python version, run

   ```
   python3 ./tools/provision -p <path_to_your_python_version>
   ```
4. If that succeeds, it will end with printing the following command:

   ```
   source /.../python-zulip-api/.../activate
   ```

   You can run this command to enter the virtual environment.
   You'll want to run this in each new shell before running commands from `python-zulip-api`.
5. Once you've entered the virtualenv, you should see something like this on the terminal:

   ```
   (zulip-api-py3-venv) user@pc ~/python-zulip-api $
   ```

   You should now be able to run any commands/tests/etc. in this
   virtual environment.

### Running tests

You can run all the tests with:

`pytest`

or test individual packages with `pytest zulip`, `pytest zulip_bots`,
or `pytest zulip_botserver` (see the [pytest
documentation](https://docs.pytest.org/en/latest/how-to/usage.html)
for more options).

To run the linter, type:

`./tools/lint`

To check the type annotations, run:

`./tools/run-mypy`
