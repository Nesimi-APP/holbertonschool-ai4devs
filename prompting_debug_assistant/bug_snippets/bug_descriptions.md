## Bug 1 - bug1.py
**Intended Behavior:** Calculate the total price of shopping cart items after applying a percentage discount.
**Issue Type:** Logical error.
**Notes:** The code subtracts the discount rate as a flat number instead of calculating the percentage of the price.

## Bug 2 - bug2.js
**Intended Behavior:** Display user bios from a list of objects, handling missing profiles gracefully.
**Issue Type:** Runtime exception.
**Notes:** The function crashes when trying to access `.bio` on a null or undefined `profile` object.

## Bug 3 - bug3.py
**Intended Behavior:** Check the operating system and print a diagnostic report.
**Issue Type:** Syntax error.
**Notes:** Missing colons (:) after `if` and `else` statements, and incorrect indentation.

## Bug 4 - bug4.c
**Intended Behavior:** Iterate through a 5-element array to print scores and calculate their sum.
**Issue Type:** Off-by-one error.
**Notes:** The loop condition `i <= num_elements` causes the program to access an index outside the array bounds.
