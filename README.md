# 🖧 FTP Client-Server in Python

**Course:** CNT 5106 - Computer Networks  
**Project:** Individual Project – FTP Protocol Simulation  
**Language:** Python  
**Deadline:** February 27

---

## 📌 Description

This project implements a basic FTP client-server system using **Python socket programming**. It allows file transfers over TCP through two core operations:

- `get <filename>` – download a file from the server to the client
- `upload <filename>` – upload a file from the client to the server

The client and server communicate by transferring files in **1KB chunks** to ensure robust and memory-efficient operation for large files.

---

## 📂 Project Structure

```
FTP/
├── ftpclient.py               # Client-side code
├── ftpserver.py               # Server-side code
├── downloadTestFile.pptx      # Sample file to download from server
├── uploadTestFile.pptx        # Sample file to upload from client
├── Run.txt                    # Basic run instructions
```

---

## 🧪 How to Run

1. **Open two terminal windows.**

2. **Start the server in the first terminal:**
   ```bash
   python ftpserver.py 5106
   ```

3. **Start the client in the second terminal:**
   ```bash
   python ftpclient.py 5106
   ```

4. **From the client terminal, enter one of the commands:**
   - `get downloadTestFile.pptx`  
     → Downloads file and saves as `newDownloadTestFile.pptx`
   - `upload uploadTestFile.pptx`  
     → Uploads file to server and saves as `newUploadTestFile.pptx`

---

## 💡 Features

- TCP-based file transfer using Python's `socket` module
- File chunking in **1KB blocks**
- Ensures file integrity using continuous read/write and flush
- Avoids overwriting by renaming downloaded and uploaded files
- Compatible with any file format, including `.pptx` and `.txt`
- Simple command-line interface

---

## 🛠 Technologies Used

- Python 3.x
- Socket Programming
- File I/O Operations
- TCP/IP Networking

---

## ⚠️ Notes

- Place both `ftpclient.py` and `ftpserver.py` along with test files in the **same directory**.
- Ensure the server is started **before** the client attempts to connect.
- For large files, ensure chunking logic is working by validating file size and completeness.
- Rename logic helps prevent original test files from being overwritten.

---

## 👨‍💻 Author

[MAYANK GARG]  
University of Florida  
Course: CNT 5106 – Computer Networks

---

## 📎 Example Test Files

- `downloadTestFile.pptx`: Used for download testing  
- `uploadTestFile.pptx`: Used for upload testing  
- Output files will be generated as:
  - `newDownloadTestFile.pptx`
  - `newUploadTestFile.pptx`
