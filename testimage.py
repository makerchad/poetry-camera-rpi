# Test Print Photo on receipt.

from escpos.printer import Usb

# Set up printer
global printer
# USB Printers can  have different 'in_ep' and 'out_ep' check in your usb settings
printer = Usb(0x0485, 0x5741, in_ep=0x81, out_ep=0x03)

#logo divider and top of receipt
printer.text("\n\n\n")
printer.image("logo.gif")
printer.text("\n\n")
printer.image("line.gif")
printer.text("\n\n\n")

#poem
printer.text("Testing 1..2..3..\n")
printer.text("This is a poem.\n")
printer.text("It's made just for you.\n")

#divider and bottom of receipt
printer.text("Enjoy\n\n\n")
printer.image("line.gif")
printer.text("\n\n")
printer.text("On CURRENT_DATE_AND_TIME\n")
printer.text("This poem was written by\n")
printer.text("Verse-O-Matic AI\n")
printer.text("\n\n\n")
printer.cut()
