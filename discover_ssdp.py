import socket

SSDP_ADDRESS = "239.255.255.250"
SSDP_PORT = 1900
SSDP_REQUEST = (
    "M-SEARCH * HTTP/1.1\r\n"
    + "HOST: 239.255.255.250:1900\r\n"
    + 'MAN: "ssdp:discover"\r\n'
    + "MX: 1\r\n"
    + "ST: roku:ecp\r\n"
    + "\r\n"
)


def discover_roku_via_ssdp(timeout=5):
    socket.setdefaulttimeout(timeout)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(SSDP_REQUEST.encode(), (SSDP_ADDRESS, SSDP_PORT))

    roku_devices = []
    while True:
        try:
            _, addr = sock.recvfrom(65507)
            roku_devices.append(addr[0])
        except socket.timeout:
            break

    return roku_devices


if __name__ == "__main__":
    devices = discover_roku_via_ssdp()
    if devices:
        print(f"Roku devices found: {devices}")
    else:
        print("No Roku devices found via SSDP.")
