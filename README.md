# python-readwrite-locks
Implementation of read-write lock in python using threading.Lock! The one where concurrent reads are allowed but writes are isolated.

A lock interface and two different implementations to explain mutex. 
A shared resource, Book, is being read and written. Multiple users are allowed to read a book, but when book needs to be written/updated, there should be no reader reading or another writer writing.

## Simple lock
- Readers keep coming and start reading if there is no writer else they will wait for writer to complete its job.
- Writer waits if reader is reading. Once the book is free, writer writes.
- If first reader comes and then readers keep coming, writer will not get free slot and readers will keep reading stale data and writer starves. How to solve this?

## Lock which prefers writer
- Reader comes and checks if there is any writer writing or waiting to write. If any writer is not waiting or writing, it will start reading else will wait.
- Write comes and marks that it is waiting. When reader who is reading leaves, writer gets preference over readers if any.
- This solves problem of writer starvation and helps keep the book updated.
