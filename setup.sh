set -x
sudo apt update
sudo apt upgrade -y

sudo apt install \
	python3-pip \
	i2c-tools \
	libjpeg-dev zlib1g-dev libfreetype6-dev libtiff5 libatlas-base-dev \
	lm-sensors \
	wiringpi \
	docker.io \
	libffi-dev \
	-y

sudo ln -s /usr/bin/python3 /usr/bin/python
sudo ln -s /usr/bin/pip3 /usr/bin/pip

sudo pip install \
	docker-compose \
	smbus2 \
	RPi.GPIO \
	pipenv

sudo adduser ubuntu i2c
sudo i2cdetect -y 1
sudo touch  /etc/udev/rules.d/99-gpio.rules
sudo echo 'KERNEL=="ic2-1", GROUP="i2c", MODE="0660"' >> /etc/udev/rules.d/99-gpio.rules
sudo echo 'KERNEL=="gpiomem", GROUP="gpio", MODE="0660"' >> /etc/udev/rules.d/99-com.rules

sudo groupadd gpio
sudo chown root:gpio /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
sudo adduser ubuntu gpio
sudo adduser ubuntu docker

sudo cp poe_hat.service /etc/systemd/user/
cd poe_hat && pipenv install
systemctl --user enable poe_hat.service
systemctl --user start poe_hat.service


sudo shutdown -r now
