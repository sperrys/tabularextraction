# DB

## Description

In the content-based extraction and validation phase, the database represents a persistant store of data
related to content validation. 

In this store, 2 main concepts are tracked. 

* Vocabulary
   - Adding a new vocabulary is done at a point of intervention when no translation is needed,
     but a value gets flags as invalid.
   - If a vocab word already exists for a given `field`, then the program will properly validate it, the second
     time it appears

* Translations
   - Mapping from a bad value for a given `field`, to a representative good value
   - Adding a new translation is done at a point of intervention
   - If a translation already exists for a known bad input of a given `field`, then the program does the mapping itself



### Getting Started with a MongoDb backend 


Depending on what machine you are using, the database setup will be slightly different. If trying to run the database locally (as default), 
follow the instructions [here](https://docs.mongodb.com/manual/installation/#mongodb-community-edition).

Once mongodb is installed and running, enter the following commands to properly configure the database. 

1. Enter the mongo shell with the command `mongo`
2. Once in, create and connect to the metco database with the command `use metco`

That's it! Everything else will be handled by the current database driver. 


### Extending / Changing 

If for whatever reason, it seems to make sense to change the database from mongo to a different database, 
convert the function bodies logic to the other database's python driver equivalent.


### Privacy Concerns

Given the sensitive nature of the data, it's imperative that peristant storage is done locally so as to not leak 
any potentially compromising data to 3rd party entities.
