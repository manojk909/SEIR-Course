# SEIR-Course

## ASSIGNMENT 01
### Web Page Analysis & Simhash

#### Problem Statement

PART-01: Write a Python program that takes a URL from the command line and outputs:
   * Page Title (without HTML tags)
   * Page Body (plain text)
   * All URLs the page links to

The webpage is fetched using an HTTP GET request, and HTML parsing is done
to extract the required content.

PART-02: Extend the program to:
   * Count word frequency in the page body (case-insensitive, alphanumeric words)
   * Implement a 64-bit polynomial rolling hash for words (`p = 53`, `m = 2⁶⁴`)
   * Compute Simhash for a document
   * Take two URLs as input and print how many bits are common in their simhashes

The logic for constructing Simhash and calculating the number of common bits
between two URLs has not been fully implemented.

--------------------------------------------------
How to Run
--------------------------------------------------
For webpage fetching:
python fileName.py URL

For the hashing attempt (partial):
python fileName.py URL1 URL2
