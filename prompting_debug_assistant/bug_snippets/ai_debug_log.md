Bug 1 – shopping_cart.py
AI Diagnosis: The function apply_discount calculates the correct discount_amount, but subtracts the discount_percentage value itself from the price instead of the calculated amount.

Suggested Fix: Change final_price = price - discount_percentage to final_price = price - discount_amount.

Alternative Fixes Tested: None.

Result: Fix works as expected.

Bug 2 – user_profiles.js
AI Diagnosis: The code attempts to access user.profile.bio without checking if profile exists. Since some users have a null or missing profile, this triggers a "Cannot read properties of null" error.

Suggested Fix: Use optional chaining: const bioText = user.profile?.bio ?? "No bio available";.

Alternative Fixes Tested: Using a standard if check before accessing the property.

Result: Fix works as expected.

Bug 3 – system_diagnostics.py
AI Diagnosis: The if and else statements are missing colons (:), and the subsequent print statements are not indented, causing a SyntaxError and IndentationError.

Suggested Fix: Add colons after conditions and indent the block content by 4 spaces.

Alternative Fixes Tested: None.

Result: Fix works as expected.

Bug 4 – scores_average.c
AI Diagnosis: The loop condition i <= num_elements causes an out-of-bounds access. In a 5-element array (indices 0-4), index 5 points to invalid memory, leading to garbage values in calculations.

Suggested Fix: Change the loop condition to i < num_elements.

Alternative Fixes Tested: None.

Result: Fix works as expected.
