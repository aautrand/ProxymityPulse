from sqlalchemy import create_engine, select

from scapy.all import *
from scapy.layers.dot11 import Dot11
from models import Friend, Detection
from collections import Counter

from sqlalchemy.orm import declarative_base, sessionmaker

c = Counter()

conf.iface = "wlan1"

v = 0
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

Base = declarative_base()


# Create a session
Session = sessionmaker(bind=engine)
session = Session()
# ALWAYS KEEP THIS IN FALSE
CURRENT_FRIENDS = session.query(Friend.mac_address).filter(Friend.disabled is False).all()


def wireless_card_available():
    # TODO write this code. Try to do it without chatgpt

    return True
0

def is_monitor_mode(interface):
    # TODO Write this code. Try not to use chatgpt
    return True


def packet_handler(p):
    global v

    if p.haslayer(Dot11):

        if p.addr2 is not None:
       
            v += 1
            print(p.addr2)
            f = session.query(Friend).filter(Friend.mac_address == p.addr2).first()

            if not f:
                # Create a new Friend object with the first detection
                friend = Friend(mac_address=p.addr2, detections=[Detection()])
                session.add(friend)
                session.commit()
                CURRENT_FRIENDS.append(p.addr2)
                print(friend.mac_address, friend.detection_count)
            else:
                # Add a new detection to the existing friend using the relationship
                detection = Detection(friend=f)
                session.add(detection)
                session.commit()
                print("\t", f.mac_address, f.detection_count)
        friends_stmt = select(Friend)
        macs = session.execute(friends_stmt).fetchall()

        for mac in macs:
            print(mac.mac_address, mac.detection_count)
    else:
        print("no layer11")


if __name__ == "__main__":
    print("initializing")
    if wireless_card_available():
        interface = "wlan1"  # TODO make this dynamic
        if is_monitor_mode(interface):
            sniff(iface=interface, prn=lambda pkt: packet_handler(pkt), store=False)
        # TODO add log msg that interface is not in monitor mode
    # TODO add log that wireless card is not available
