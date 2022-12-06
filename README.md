# Parental Limit Service

Python service for limiting computer usage

## Usage

Run install script as sudo, this will install the service in your system

## Change play times

You only need to update install script to something like this:

```shell
sed "s+ExecStart\=+ExecStart\=${SCRIPT_PATH}/play.py --play_time 3 /tmp/kid.txt+g " "${SCRIPT_PATH}"/parental-limit.service
```

**NOTE: Each play time duration is 35 minutes**