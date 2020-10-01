# Enhancements
As currently, the code does not changes all the spoken english text to written english, some functionalities can be added. Currently, the code is simply rule-based, but it can be improved. We can add more and more test cases but it can not ne 100% correct.
It is not a intelligent system, but we can improve it to a certain extent by:
- Improving the code over punctuations
- Adding support for different versions of english language.
- Curreny sign can be added
- Support for every number possible
- Handling white spaces and tab spaces given in the input.
- and many other factors can be included.

## How to achieve it without changing a lot of code

We should make a method such that rules can be added more easily without looking the complete code. This can be done in the following manner:
- Categorize the type of rules
- Add rules specific to each category
- Add relevant lables to each rule
- Convert the word as per its category and the label.

### Making rule addition easy
- Make a seperate method that takes the rule as input.
- User will call the method on terminal to define the rule OR, multiples rules can be added using a table as file input
- The table will look like:

| Rule Key  | Rule Value |     Label      |  Category |
|----------|:-------------:|:-------------:|------:|
| ten |  10 | decimal, number | Number |
| ruppee |   &#8377;   |  currency, indian | Currency|

- In this way, we will easily update the rules based on labels and category.
- Lables will help in determing the version of english language
- Category will help in distinguishing the types of different words
- So, the programmer only needs to make a file of rules with different categories and lables.
- This file would be given as a input to the method(that adds rules)
- And then, the rules will be updated automatically based on the input provided.
