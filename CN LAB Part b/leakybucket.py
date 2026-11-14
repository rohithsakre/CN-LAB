
# Leaky Bucket Algorithm

def min_value(x, y):
    if x < y:
        return x
    else:
        return y


drop = 0
count = 0
inp = []

cap = int(input("Enter the bucket size: "))
process = int(input("Enter the processing rate: "))
nsec = int(input("Enter the number of seconds you want to simulate: "))

for i in range(nsec):
    packet = int(input(f"Enter the size of the packet entering at {i + 1} sec: "))
    inp.append(packet)

print("\nSecond | Packet Received | Packet Sent | Packet Left | Dropped")
print("--------------------------------------------------------------")

for i in range(nsec):
    count += inp[i]

    if count > cap:
        drop = count - cap
        count = cap

    mini = min_value(count, process)

    print(f"{i + 1}\t {inp[i]}\t\t {mini}\t\t {count - mini}\t\t {drop}")

    count -= mini
    drop = 0

# Process remaining packets
while count != 0:
    mini = min_value(count, process)

    print(f"{i + 2}\t 0\t\t {mini}\t\t {count - mini}\t\t {drop}")

    count -= mini
    i += 1

