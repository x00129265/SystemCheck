# SystemCheck
Interview Q

We require a new framework example for scripting to diagnose issues with the local OS and a local database. It does not need to solve anything report in an ASCII table results of work or settings it finds. Please write  at least 300 words, on the strategy you would have for building a template script (single file) that can do the following:
 
Must have a pluggable inheritance allowing adding of new "plugins" to determine how to gather and display a new report
Must use a singleton class to manage database connections called DBManager
Must have simple help functions such as  buildTable, disaplayTable
Must collect memory, CPU, and disk information ( think top, df) from the OS and display them in 3 OS reports
Must get a list of 3 random database metric and display them
Must get a list of DB users and present them.
