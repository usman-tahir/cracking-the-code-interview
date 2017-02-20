# cracking-the-code-interview
A collection of code snippets and reference for interview-type programming questions

### Challenge 1 (Arrays: Left Rotation)
##### Implementation Language: Python
This challenge involved shifting elements of an array a certain number of times (k), based the array (a) and its length (n). This was done by removing the first element of the list and appending it to the end of the list (k) times. The final array (a) was then returned and printed on one line, with a space separating the elements.

### Challenge 2 (Trees: Is This a Binary Search Tree?)
##### Implementation Language: Python
This challenge involved Binary Search Trees (BST), and determining if a given BST (supplied from the computer) was in fact a BST or not. As this algorithm shows, the main determination factor for a BST is that, given an in-order traversal of its nodes, all data elements of those nodes are returned in strict ascending order, with no repeating data elements. The function that determines if the input is a BST returns true if it is, and false if not.

### Challenge 3 (Tries: Contacts)
##### Implementation Language: Python
In this challenge, a contact storing/accessing mini application was created, to store new contacts and find contacts based on a search string (known as a partial). Since this application should be able to handle large amounts of data, it needed to be optimized, and as such, both a contact (ContactNode) and the contact application itself (ContactApp) were separated into two distinct classes, with the ContactApp referencing contacts in the context of a ContactNode.

### Challenge 4 (Hash Tables: Ransom Note)
This challenge required determining if a given ransom note could be created out of the words available from a magazine. Each word from the magazine could only map to one word in the ransom note, and so a dictionary was created for both the available words from the magazine and the ransom note, to see if the words (and their quantity available) was sufficient to create the ransom note.
