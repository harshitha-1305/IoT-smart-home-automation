# IoT-based Smart Home Automation (Raspberry Pi Pico W)

Community Service Project, B.Tech ECE, Vasireddy Venkatadri Institute of Technology. Team project (4 members).

The project came out of a village survey (Pedakakani, June 2025) where people reported wasted electricity from
appliances left on, no remote control, and little home security. This prototype shows how a low-cost IoT
system can monitor and control home appliances from a phone.

## What it does
- Reads temperature and humidity with a **DHT11** sensor and shows them live on the **Blynk** cloud dashboard.
- Controls two appliances (a bulb and a fan) through a **2-channel relay module** from the Blynk mobile app.
- Runs on a **Raspberry Pi Pico W** (RP2040, built-in Wi-Fi) programmed in **MicroPython**.

## Hardware
| Part | Use |
|------|-----|
| Raspberry Pi Pico W | Microcontroller with Wi-Fi |
| DHT11 | Temperature and humidity sensor |
| 2-channel relay module | Switches the bulb and the fan |
| Bulb and fan | Appliances |

Take care when wiring mains-voltage loads to the relay.

## Setup
1. Flash the Pico W with MicroPython firmware (hold BOOTSEL, copy the `.uf2` file).
2. Install **Thonny** and select the MicroPython (Raspberry Pi Pico) interpreter.
3. Create a Blynk template with datastreams V0 (temperature), V1 (humidity), V2 (bulb switch), V3 (fan switch).
4. Copy `BlynkLib.py` from [blynkkk/lib-python](https://github.com/blynkkk/lib-python) onto the Pico W.
5. Copy `secrets_example.py` to `secrets.py` on the Pico W and fill in your Wi-Fi and Blynk details.
6. Save `main.py` on the Pico W and run it.

## Tech
IoT, Raspberry Pi Pico W, MicroPython, Blynk, DHT11, relay module
