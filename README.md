# spoken-english-to-written-english
Converts Spoken English to Written English

A python module that converts spoken english to written english. For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

## Steps to run:

### Download the code

- Download the code or clone the repository
- Open Terminal and go to project directory

### Installing the module
   ```
   >>python3 setup.py install
   ```

### Example

Run the following commands:
   ```
>>> from spokenEng2WrittenEng import convertor
>>> convertor.convert_sp_to_wr()

Enter spoken english:
 hundred dollars.

Converted Written English Paragraph: 

 " $100"
>>> 

```
