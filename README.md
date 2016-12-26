# Klik aan Klik uit Controller


# Protocol of klikaanklikuit A-series devices

Copied from Wieltje, http://www.circuitsonline.net/forum/view/message/1181410#1181410,
but with slightly different timings, as measured on my device.

```
'0':   | |_| |_____ (T,T,T,5T)
        _       _
'1':   | |_____| |_ (T,5T,T,T)
        _   _
'dim': | |_| |_     (T,T,T,T)

T = short period of ~260µs. Use the ShowReceivedCodeNewRemote example to find the
actual period length for your devices.

A full frame looks like this:

- start pulse: 1T high, 10.44T low
- 26 bit:  Address
- 1  bit:  group bit
- 1  bit:  on/off/[dim]
- 4  bit:  unit
- [4 bit:  dim level. Only present of [dim] is chosen]
- stop pulse: 1T high, 40T low
```