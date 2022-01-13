import math

class Stream(object):
    def __init__(self, input):
        self.bitstr = "".join(["{0:04b}".format(int(b, 16)) for b in input])
        self.index = 0

    def pop (self, n, as_str=False):
        self.index += n
        result = self.bitstr[self.index-n:self.index]
        if as_str:
            return result
        return int(result, 2)

    def left(self):
        return len(self.bitstr) - self.index


class Packet(object):
    def __init__(self, stream):
        self.version = stream.pop(3)
        self.type_id = stream.pop(3)
        self.literal = 0
        self.packets = []
        if self.type_id == 4:
            self.literal = 0
            while True:
                byte = stream.pop(5)
                self.literal = (self.literal << 4) + (byte & 15)
                if byte < 16: break
        else:
            self.length_id = stream.pop(1)
            if self.length_id == 0:
                bit_length = stream.pop(15)
                bit_position = stream.index
                while stream.index < bit_position + bit_length:
                    self.packets.append(Packet(stream))
            else:
                packet_count = stream.pop(11)
                self.packets = [Packet(stream) for i in range(packet_count)]

    def __str__(self, leading=""):
        s = "{}version: {}\n{}type_id: {}\n".format(leading, self.version, leading, self.type_id)
        if self.type_id == 4:
            s += "{}literal {}\n".format(leading, self.literal)
        else:
            s += "{}packets: {}\n".format(leading, len(self.packets))
            for p in self.packets:
                s += p.__str__(leading+"\t")
        return s

    def evaluate (self):
        funcs = { 0: sum, 1: math.prod, 2: min, 3: max,
                  5: lambda p: 1 if p[0] > p[1] else 0,
                  6: lambda p: 1 if p[0] < p[1] else 0,
                  7: lambda p: 1 if p[0] == p[1] else 0 }
        if self.type_id == 4:
            return self.literal
        else:
            return funcs[self.type_id]([p.evaluate() for p in self.packets])


    def sum_version (self):
        return self.version + sum(p.sum_version() for p in self.packets)


def day1 (input):
    stream = Stream(input)
    packet = Packet(stream)
    # print (packet)
    print (packet.sum_version())
    print (packet.evaluate())


def read_data ():
    with open("day16.txt", "r") as f:
        return f.readline().strip("\n")


if __name__ == "__main__":
    data = read_data()

    day1 ("C200B40A82")
    day1 ("04005AC33890")
    day1 ("880086C3E88112")
    day1 ("CE00C43D881120")

    day1(data)

