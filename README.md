# ASCIIEncoderDecoder

A program that implements lossless encoding and decoding of files containing ASCII art.

## Instructions

Below are the steps that describe how the ASCII Transport Format is to be used:

Import the file:

  `from from ASCIIEncoderDecoder import ASCIIFormatTransporter`

Build the object that will contain the data from the ASCII art file:

  `object = object = ASCIIFormatTransporter(file_name)`

Encode the object:

  `object.encode()`
  
  This function encodes the ASCII file data. It has O(n) space and time complexity.

Decode the object:

  `object.decode()`
  
  This function decodes the ASCII file data. It has O(n_ space and time complexity.

## Unit Testing

The test suit illustrates the basic behavior of the `encode` and `decode` functionality. The tests include empty files as well as files that are comprised of various characters. The tests also check for users who attempt to encode/decode already encoded/decoded data.

In order to test the robustness of the program use the following command:

`python3 ASCIItests.py`

## Run Length Encoding Data Compression Algorithm

This algorithm consists of replacing large sequences of repeating data with only one item of this data and a counter that indicates the number of times the item is repeated. Below is an example:

  `aaaaabbbbcccc`

Using the run-length algorithm we produce the following output:

  `5a 4b 4c`

This can be interpreted as a sequence of five as, four bs, and four cs.

### Justification

This algorithm is simple to implement and does not incur large CPU overhead. It is an ideal algorithm for files that contain a lot of repetitive data (which is the case for certain ASCII art). In the example file provided there were 5496 characters before compression. After using the run length encoding algorithm, the file was compressed to 3458 characters, which indicates a 37.1% improvement. In the best case RLE can reduce the original data to two values. However, it must be noted that there are certain flaws with this algorithm. The most important flaw would be if the file does not contain any repeated characters. This would result in double the space usage. Another advantage of this algorithm is that it is a lossless compression technique. 

### Modifications

One of the drawbacks of RLE is if there is only a single byte to encode, you have to add an extra byte for the length byte. Although we can encode 256 repetitons of a single byte, this does not occur often in practice. Individual bytes in ASCII can be encoded in 7 bits. The 8th bit of all bytes in a text file is 0. Thus we can use the last bit as a flag to indicate whther a byte should be repeated or not. If the bit is set to 1 then the decoder will write the number of byte repetitions. 



