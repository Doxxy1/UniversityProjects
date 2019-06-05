# A2IoT
COSC2674 &amp; COSC2755 (PIoT) Semester 1, 2019 Assignment 2 Specification (Building a Smart Library) 

This is a libary application created for the raspberry pi in python for Assignment 2, Programming Internet of Things.

This program has a reception pi and a master pi.

A user may register with text or text and facial recognition, they are also allowed to login with the facial recognition or a good ol' password.

Once a user logs in (through sockets), they may list all of the books in the library, search for a book (by id, author and title) - with text or speach recognition, borrow as many books as they please or return books (based on the id or a QR code).

Also on the master pi is a flask admin dashboard that is included, this allows the admin to generate graphs regarding the trend in borrowing / returning, add books and delete books.
