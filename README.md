# PiRouser

Simple script to arouse a remote machine based on a state of mains power and UPS charge.

## Motivation

It is common for many operating systems to be able to shut itself down when UPS battery level becomes low. However, the challenge is to power the system back on safely. One option may be to set up the system to power on when power is restored, however, this has risks:
* The power outage may not drain the UPS fully, thus never triggering the event
* There may be another outage following the first event, which may catch the system mid-boot, without enough battery reserve to finish booting up and then to shut down again safely.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

The project is work in progress

## Deployment

The recommendation is to install it on a RO raspberry PI to minimise chance of data corruption on power loss.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* WIP
