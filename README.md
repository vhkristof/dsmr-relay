
# dsmr-relay
*dsmr-relay is a script to provide raw DSMR telegram data via HTTP for others to consume (e.g. an Alfen charge point). The data can be provided by [DSMR-reader](https://github.com/dsmrreader/dsmr-reader).*

## Run dsmr-relay
### Without Docker

    git clone https://github.com/vhkristof/dsmr-relay.git
    cd dsmr-relay
    pip install -r requirements.txt
    python dsmr-relay.py <port> # default port is 8000

### With Docker

    git clone https://github.com/vhkristof/dsmr-relay.git
    cd dsmr-relay
    docker build -t dsmr-relay .
    docker run -p 8000:8000 -d -v $(pwd)/dsmr-relay.py:/app/dsmr-relay.py --name dsmr-relay --restart always dsmr-relay


## Provide data via DSMR-reader
In my situation I use DSMR-reader as a [remote data logger](https://github.com/xirixiz/dsmr-reader-docker?tab=readme-ov-file#remote-dsmr-datalogger---api_client) on a Raspberry Pi.
Make sure you add the URL on which the relay is listening to `DSMRREADER_REMOTE_DATALOGGER_API_HOSTS`. Also add a dummy key to `DSMRREADER_REMOTE_DATALOGGER_API_KEYS`.

Mine looks like this (first entry is my Home Assistant, second is the relay):   

    DSMRREADER_REMOTE_DATALOGGER_API_KEYS=6Z9YIWF5SJP6DTCO2DWGL82FXXXXXXXOXFN5UCCG0TNOHYYLFOVS1TI5S9VTW,bla
    DSMRREADER_REMOTE_DATALOGGER_API_HOSTS=http://192.168.5.99:8888,http://192.168.5.108:8000



