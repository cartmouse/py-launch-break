import mido
import time


class Launchpad:
    def __init__(self):
        self.to_prog_msg = mido.Message.from_hex('F0 00 20 29 02 0C 0E 01 F7')
        self.to_live_msg = mido.Message.from_hex('F0 00 20 29 02 0C 0E 00 F7')

        outports = mido.get_output_names()

        index = [i for i, s in enumerate(
            outports) if 'Launchpad X MIDI 2' in s]

        outname = outports[index[0]]

        self.port = mido.open_output(outname)
        print(f'Port opened: "{outname}"')

        print('Entering prog mode...')
        self.port.send(self.to_prog_msg)

    def close(self):
        print('Entering live mode...')
        self.port.send(self.to_live_msg)
        time.sleep(1)
        self.port.close()
        print('Port closed')

    def lp_init(self):
        print('Initialising control pads...')
        self.send_hex('90 2C 15')
        self.send_hex('90 2D 05')
        self.send_hex('90 36 25')
        self.send_hex('90 37 0D')

    def send_hex(self, msg_str):
        msg = mido.Message.from_hex(msg_str)
        self.port.send(msg)
