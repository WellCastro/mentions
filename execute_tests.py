"""Call tests from docker compose."""
from subprocess import call

call("cd tests && pytest tests.py ", shell=True)