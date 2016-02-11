all: install

install:
	install -m 755 sfe-com-11629-clockd.py /usr/local/bin
	install -m 644 sfe-com-11629-clockd.service /etc/systemd/system
