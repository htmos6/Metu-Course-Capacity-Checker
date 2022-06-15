# metu-sis-course-capacity-for-requested-courses

For the course capacity of metu, we need to check course capacities manually. We may find courses which have capacity. 
In order to check course capacities automatically, I have designed course capacity questioning bot by selenium. 
It visits webpages, and find requested course on a page. If It has capacity, python code plays a warning sound, and 
prints available course sections to a command line like in the following lines.

 5670312 DIGITAL ELECTRONICS Section: 2 Capacity: 6

 5670312 DIGITAL ELECTRONICS Section: 4 Capacity: 2

 4600486 PROBLEM SOLVING IN MATHEMATICS Section: 1 Capacity: 1


Add your warning sound path --> metu-sis-capacity.py --> Line 7
Add your geckodriver.exe path --> metu-sis-capacity.py --> Line 11
Add your url from metu-sis website under --> metu-sis-capacity.py --> if __name__ == "__main__":  and add your course-code-to-search
