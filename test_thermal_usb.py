from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
# p = Usb(0x0485, 0x5741, 0, profile="TM-T88III") 
np = Usb(0x0485, 0x5741, in_ep=0x81, out_ep=0x03)
p.text("Hello World\n")
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.cut()
