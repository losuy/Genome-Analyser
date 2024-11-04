# Genome-Analyser Project

## Overview
This project aims to create a graphical user interface (GUI) application for analyzing genomic data, specifically FASTA files. Below are the main tasks and features that need to be implemented.

---

## To-Do List

### 1. GUI Development
- [ ] **Set Up Main File**
  - Use `gui.py` as the main application file.
  - Import any required images for the interface.

### 2. File Selection and Display
- [ ] **Enable FASTA File Selection**
  - Implement a GUI file picker to select a FASTA file.
- [ ] **Display FASTA Content**
  - Create a pseudo text editor to display the content of the selected FASTA file.

### 3. Search Functionality
- [ ] **Implement Search Feature**
  - Add a "find" feature to search for specific nucleotide sequences within the FASTA file using Python’s `re` library.
  - **Determine Necessity**: Assess if this feature is essential for the initial version.

### 4. Dropdown Menu Options
- [ ] **Create Operation Dropdown**
  - Implement a dropdown menu for various sequence operations.
  - Add restrictions for options based on valid nucleotide characters (A, G, T, C).

### 5. Output Display
- [ ] **Implement Output Window**
  - Create a separate window to display results or outputs from selected operations.

### 6. Graph Display
- [ ] **Add Graph Visualization**
  - Decide between displaying nucleotide base frequencies or protein-related information in a graphical format.

### 7. Command Line Interface (CLI)
- [ ] **Implement CLI Functionality**
  - Add a command-line option to execute operations alongside the GUI.

### 8. JSON Configuration
- [ ] **Save User Settings**
  - Implement functionality to save user settings or function parameters in a JSON file.
  - Determine the best method for loading and saving these configurations.

### 9. Sequence Reset Function
- [ ] **Implement Reset Feature**
  - Add functionality to revert changes to the most recent version of the sequence.

### 10. UI Enhancements
- [ ] **Animation in Directory Tab**
  - Implement a simple animation to enhance user experience in the Directory tab.
- [ ] **Status Label**
  - Add a label to indicate the success or failure of operations in the Directory tab.
- [ ] **Success Window Trigger**
  - Automatically bring a secondary window to the front upon successful operation.

### 11. Optional Features
- [ ] **Evaluate Additional Enhancements**
  - Assess remaining tasks and potential enhancements if time permits.

---

## How to Use
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Genome-Analyser.git
