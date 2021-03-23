# Spoken English to Written English
This is a Python reusable library that can convert a paragraph of spoken English to written English.

For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

## Installation
Please make sure that you have updated pip3 to the latest version before installing SpokenToWritten.
You can install the module using Python Package Index using the below command.
```
>>pip3 setup.py install
```

## Usage
```
>>python3
>>from SpokenToWritten import spoken_to_written_eng
>>spoken_to_written_eng.convert_spoken_to_written_eng()
>>
Enter Your paragraph of spoken english:
Tom has bought a pen for three dollars. He made the online transaction in an e-commerce site at 10 A M. He had also purchased a triple A title game.
The input Spoken English Paragraph:
 Tom has bought a pen for three dollars. He made the online transaction in an e-commerce site at 10 A M. He had also purchased a triple A title game.

Converted Written English Paragraph:
  Tom has bought a pen for $3. He made the online transaction in an e-commerce site at 10 AM. He had also purchased a AAA title game.
```
  
## Future Improvements
1. Upto 10 dollars has been implemented. We can increase the dollars beyond $10 in future versions.
2. Only dollar as a currency is implemented. We can include other currencies in future versions.
3. More abbreviations can be included in future versions.
4. Single, double and triple is implemented. We can include other tuples in future versions.
