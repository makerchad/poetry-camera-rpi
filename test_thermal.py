from escpos.printer import Serial

""" 115200 Baud, 8N1, Flow Control Enabled """
p = Serial(devfile='/dev/serial0',
           baudrate=115200,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=False)

p.text("Hello World\n")
p.qr("You can readme from your smartphone")
p.cut()
