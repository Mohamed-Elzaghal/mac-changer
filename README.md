🛠️ MAC Changer Tool

A professional Python tool for changing the MAC address on Linux systems (Kali, Ubuntu, ParrotOS…).
Useful for penetration testers, bug bounty hunters, researchers, and privacy-focused users.

🚀 Features

Change MAC address to a custom value

Random MAC generator (optional)

Error handling (permission issues, interface checks)

Colorful terminal output

Works on all Linux distros

📸 Example Usage

    sudo python3 mac_changer.py -i eth0 -m 00:22:33:44:55:61

output:

<img width="1292" height="208" alt="kali-linux-2025 2-virtualbox-amd64  Running  - Oracle VirtualBox 11_15_2025 12_11_03 AM" src="https://github.com/user-attachments/assets/d12620a8-0617-42b6-b307-27c4c86ff43c" />


⚙️ Installation

    git clone https://github.com/USERNAME/mac-changer.git
    cd mac-changer

🧪 Usage
Change to a specific MAC

    sudo python3 mac_changer.py -i eth0 -m 00:22:33:44:55:66
    

🖥️ Requirements

Python 3.x

Root privileges

Linux-based OS

📦 Create Executable

    sudo cp mac_changer.py /usr/local/bin/macchanger
    sudo chmod +x /usr/local/bin/macchanger

🧩 Error Handling

If you get:

    SIOCSIFFLAGS: Operation not permitted

It means:

    You didn't run with sudo

    Or Kali VM network is "Bridged" / "NAT" blocking MAC changing

    Or interface controlled by NetworkManager
    
🏷️ License

MIT — Free to use, modify and distribute.

⭐ Support

If you like this tool, give it a ⭐ on GitHub!


