# Sorting_Assignment
1) Dor Pel - דור פל
  ID: 322916784
2) Liran Krichli - לירן קריכלי
   ID: 211616859
   
We choose to implament Bubble Sort, Insertion Sort And Merge Sort (1,3,4)
python run_experiments.py -a 1 3 4 -s 100 500 3000 -e 1 -r 20 (with 5% noise)

<img width="640" height="480" alt="result1" src="https://github.com/user-attachments/assets/4da697e0-8d21-4b3c-905a-ada08faac793" />

For image 1 we can see that bubble and insertion sort growth rate O(n^2), and Merge sort growth rate is O(nlog(n))
we can see that merge sort runtime is a lot faster than insertion and bubble
For the variance the shaded area represents the standard deviation over 20 reps


<img width="640" height="480" alt="result2" src="https://github.com/user-attachments/assets/2e99e40f-d6d8-43dd-ada0-1947b8871165" />

For image 2 we can see that a Nearly sorted merge sort is stil O(nlog(n)), a Nearly sorted insertion sort is approaching best case which is O(n)
and for a Nearly sorted Bubble sort its still showing O(n^2) complexity
