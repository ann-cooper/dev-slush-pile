Title: Disposable test databases and loading test data
Author: AC
Date: 2022-08-04
Tags: db, debugging, notes
Slug: db-notes
Summary: A handful of ways to check and fix local dbs
Status: draft

To enter sqlite shell: `sqlite3`
To open an existing db: `.open filename`

- I have a sqlalchemy model and I'm calling a create_all(), but my table doesn't exist, what's going on?
    - Where are you declaring `Base`? Where are you importing it?
        - Declare it in one place
        - Remember to import it into your model file and your model should be a subclass of Base. This is for non-Flask dbs.