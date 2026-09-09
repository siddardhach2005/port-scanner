# 🔍 Network Port Scanner

A simple and lightweight **TCP Network Port Scanner** built with Python. This project scans a target IP address or hostname for open ports and attempts to identify the services running on those ports.

The scanner uses Python's built-in `socket` module for network communication and `ThreadPoolExecutor` for concurrent port scanning.

---

## 📌 Features

* Scan a target IP address or hostname
* Resolve hostnames to IPv4 addresses
* Scan ports from **1 to 1024**
* Detect open TCP ports
* Identify common services associated with open ports
* Uses multithreading for faster scanning
* Handles invalid hostnames/IP addresses
* Configurable connection timeout
* Simple command-line interface

---

## 🛠️ Technologies Used

* **Python 3**
* **Socket Programming**
* **TCP/IP**
* **IPv4**
* **Multithreading**
* **Concurrent Programming**

### Python Modules

* `socket`
* `concurrent.futures`

No external Python packages are required.

---

## 📂 Project Structure

```text
Network-Port-Scanner/
│
├── port_scanner.py
└── README.md
```

---

## ⚙️ How It Works

The scanner follows these basic steps:

```text
User enters target
        ↓
Resolve hostname to IP
        ↓
Create TCP socket
        ↓
Attempt connection to each port
        ↓
Check connection result
        ↓
If successful → Port is OPEN
        ↓
Identify common service
        ↓
Display result
        ↓
Close socket
```

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/network-port-scanner.git
```

### 2. Navigate to the project

```bash
cd network-port-scanner
```

### 3. Check Python installation

```bash
python --version
```

Python 3 or later is recommended.

---

## ▶️ Running the Project

Run:

```bash
python port_scanner.py
```

You will be asked to enter an IP address or hostname:

```text
Enter target IP or hostname: 127.0.0.1
```

The scanner will then check ports **1–1024**.

---

## 📊 Example Output

```text
Scanning 127.0.0.1 (127.0.0.1)...

Port 135   OPEN    Service: epmap
Port 139   OPEN    Service: netbios-ssn
Port 445   OPEN    Service: microsoft-ds
Port 8080  OPEN    Service: Unknown

Scan completed.
```

---

## 🧠 Core Concepts

### 1. Socket Programming

The project uses Python's `socket` module to create TCP connections.

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

* `AF_INET` → IPv4
* `SOCK_STREAM` → TCP

---

### 2. Port Scanning

The scanner attempts to connect to individual ports:

```python
result = sock.connect_ex((target_ip, port))
```

A result of:

```text
0
```

indicates that the connection was successful.

Therefore, the port is reported as **OPEN**.

---

### 3. Timeout

The scanner uses a timeout:

```python
sock.settimeout(0.5)
```

This prevents the program from waiting indefinitely for a response.

---

### 4. Multithreading

The project uses:

```python
ThreadPoolExecutor(max_workers=100)
```

This allows multiple ports to be scanned concurrently instead of checking every port sequentially.

This significantly improves scanning speed.

---

### 5. Service Detection

The scanner attempts to identify the standard service associated with an open port:

```python
socket.getservbyport(port)
```

For example:

```text
22  → SSH
25  → SMTP
53  → DNS
80  → HTTP
443 → HTTPS
```

If Python cannot identify the service, it displays:

```text
Unknown
```

---

## 🔐 Security & Ethical Usage

This project is intended for **educational and authorized security testing purposes**.

Only scan:

* Your own computer
* Your own network
* Systems you have explicit permission to test
* Lab environments designed for security testing

Do **not** scan systems without authorization.

---

## 🚀 Future Improvements

Possible improvements include:

* Allow users to specify custom port ranges
* Add UDP port scanning
* Add banner grabbing
* Detect more services
* Add command-line arguments
* Export scan results to a file
* Add colored terminal output
* Add logging
* Improve error handling
* Add a graphical user interface
* Display scan duration
* Add configurable thread count

---

## 🎯 Learning Objectives

Through this project, you can learn:

* Python socket programming
* TCP/IP fundamentals
* IPv4 networking
* Client-server communication
* TCP port concepts
* Network reconnaissance fundamentals
* Exception handling
* Multithreading
* Concurrent programming
* Basic cybersecurity concepts

---

## 📈 Project Outcome

The completed project provides a basic tool for identifying **open TCP ports** on an authorized target and displaying the likely services associated with those ports.

It demonstrates practical knowledge of **Python programming, computer networking, socket programming, and basic cybersecurity reconnaissance**.

---

## 👨‍💻 Author

**Siddardha Chennamsetti**

Computer Science Engineering – CyberSecurity

GitHub: `github.com/siddardhach2005`

---

## ⭐ Conclusion

The Network Port Scanner is a beginner-friendly cybersecurity project that demonstrates how network connections can be tested programmatically using Python.

It provides a foundation for understanding more advanced network security tools and concepts.
