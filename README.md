# sfe-com-11629-clockd
Degital Clock with external 7-segment display

<img src="https://raw.githubusercontent.com/wiki/yukkeorg/sfe-com-11629-clockd/image.jpg">

### Required Hardware
- Raspberry Pi
- SparkFun 7-Segment Serial Display
  - [Original](https://www.sparkfun.com/products/11441)
  - [Agency on Japan](https://www.switch-science.com/catalog/1159/)
  
### Required Software
- Python 2.7 or higher
  - SMBus
  - python-daemon

### Quick Start
(in Raspbian)
```
git clone https://github.com/yukkeorg/sfe-com-11629-clockd
cd sfe-com-11629-clockd
sudo make install
sudo sfe-com-11629-clockd.py -f
```

### License
Public Domain
