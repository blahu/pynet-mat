ifconfig tap0
sudo ifconfig tap0 inet 10.1.1.254/24 up
ping -c 3 10.1.1.1

