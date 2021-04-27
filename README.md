# workweek_scheduler

## Overview

There are several companies that often struggle to schedule their installation crew efficiently. The goal of this program is to help with the scheduling of the installation crew when given different types of buildings and various types of employees.

## Task

Given a list of buildings and a list of employees, generate the schedule for the coming work week by implementing the method _schedule(buildings, employees)_ and providing some proof that it works, i.e. generates the correct results. If you weren’t able to complete the entire task, list the parts you left out and how long you think it would take you to finish them. 

## Requirements & Constraints

* The output schedule is for the next 5 days: assume Monday through Friday.
* All employees work full days, but can be unavailable on certain days (sick/vacation etc.) 
* Assume buildings are given in the order of their importance -- no need for anything but a simple in-order scheduling 
* There are 3 types of employees: 
  * Certified installers 
  * Installers pending certification 
  * Handymen 
* There are 3 types of buildings, each requiring a different set of employees. All installs are done in 1 day. 
  * Single story homes require: 
    * 1 certified installer 
  * Two story homes require: 
    * 1 certified installer AND 
    * 1 installer pending certification OR a handyman 
  * Commercial buildings require: 
    * 2 certified installer AND 
    * 2 installers pending certification AND 
