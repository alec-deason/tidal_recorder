This is an experiment with recording [TidalCycles](https://tidalcycles.org) sessions in a machine readable way and replaying them.

## Setup
Install https://pexpect.readthedocs.io/en/stable/
In whatever editor you are using add a hook which calls the `record.py` command each time you send a message to tidal. `record.py` expects two arguments, the first is the path to a log file where it will record the messages and the second is the message itself exactly as it should be sent to tidal.

It will write the messages with timestamps to the log file as a json array.

## Playback
Playback with `python replayer /path/to/log.json`. Assuming you have tidal and ghc installed in a standard way and you have SuperDirt running it should start playing back the recorded log.

## Stability
This is about ten minutes worth of prototype and has been tested on exactly one computer (running linux) so don't expect it to work too well.
