# Lowenstein-SleepHQ-Integration
A project to upload the data from a Lowenstein medical device SD card to Sleep HQ web site.

This project builds upon the work by mstone672 sleephq-lowenstein-api:

https://github.com/mstone672/sleephq-lowenstein-api

This above script is the main part of the project to import the data from a Lowenstein Prisma 20a cpap device into an account at Sleep HQ using their api. You will need a paid account for this:

https://www.sleephq.com/

I have had to hard code the Team ID portion of this script as I had errors when executing it with the 'get_team_id' function being called.

Refer to overview file and individual txt files for further information on how to perform the integration. You may wish to leave out parts not required for your purpose. You will also have to adjust paths and variables to suite your installation.

I used the following hardware items in this project:

https://www.yepkit.com/product/300115/YKUSHXS

https://www.amazon.com.au/waveshare-Raspberry-Pre-Soldered-Quad-Core-Cortex-A53/dp/B09LTDQY2Z/ref=sr_1_5?crid=3JTLKEB7S29XT&sprefix=pi+zero+kit%2Caps%2C252&sr=8-5

https://www.altronics.com.au/p/h0201-ub1-157lx95wx53hmm-black-abs-jiffy-box/

https://www.altronics.com.au/p/s0950a-spst-vandal-resistant-screw-terminal-pushbutton-switch/

https://www.altronics.com.au/p/p0836-neutrik-usb-2.0-type-a-type-b-chassis-silver-nausb/

https://www.altronics.com.au/p/p0634a-2.1mm-female-line-strain-relief-dc-power-plug-9.5mm/

https://www.altronics.com.au/p/p0628-2.1mm-female-plastic-chassis-mount-dc-power-socket/

https://core-electronics.com.au/raspberry-pi-3-power-supply.html

USB A male to USB mini B male cable

USB A male to USB micro B USB male cable

USB A male to USB B male cable

10k ohm 1/4 W resistor

3 x wired female Dupont connectors for pi pin headers to switch connection

Refer jpeg of finished enclosure that houses equipment used.

My intent was to have a system, that upon the press of a button, will open a USB connection to the Prisma thus allowing the pi to scan for the SD card files and upload them automatically to Sleep HQ. Upon completion the USB connection will be closed thus returning the Prisma to normal operational state (it locks when USB connected).

Process timing is important as the Prisma will turn off after around 12 minutes of inactivity. Typically you would operate the button, after waking and finishing the nights cpap therapy, before the machines gets a chance to shutdown. The machine will stay awake while it is connected to an active USB host. 

The Ykush XS board not only connects/disconnects the USB power lines but also connects/disconnects the USB data lines, so there is no harm in leaving the cabling permanently connected.

The collected project files, scripts and documentation represents the production version of the project.


